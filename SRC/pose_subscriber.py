import json
import time
import threading
from pathlib import Path
from typing import Iterator

try:
    from .odom_message import Odometry
except ImportError:
    from odom_message import Odometry

DEFAULT_PATH = Path(__file__).parent / "trajectory.json"

class Subscriber:

    def __init__(
        self, name: str, data_class, callback=None, callback_args=None, queue_size=None, buff_size=65536, tcp_nodelay=False
    ) -> None:
        """
        Faux Subscriber ROS à des fins de test.

        Le constructeur a les mêmes paramètres que rospy.topics.Subscriber
        (cf. http://docs.ros.org/en/melodic/api/rospy/html/rospy.topics.Subscriber-class.html)
        """
        self._topic = name
        self._message_type = data_class
        self._callback = callback

        self._stop_event = threading.Event()
        
        self._time_delta = None
        self._message_generator: Iterator[Odometry] = self._get_poses()
        
        self._notifier = threading.Thread(group=None, target=self._notify_poses, args=callback_args or tuple())
        self._notifier.start()

    def is_running(self):
        return not self._stop_event.is_set()

    def stop(self):
        self._stop_event.set()
        self._notifier.join()

    def _get_poses(self, file_path = DEFAULT_PATH) -> Iterator[Odometry]:
        """
        Lit le fichier de données de trajectoire, en extrait la période d'échantillonnage
        et renvoie chaque donnée l'une après l'autre.

        :param file_path: chemin vers le fichier de données en format JSON.
        """
        with open(file_path, "r") as trajectory_file:
            odom_messages = json.load(trajectory_file)
            
            initial_msg = Odometry.from_dict(odom_messages[0])
            next_msg = Odometry.from_dict(odom_messages[1])
            self._time_delta = (
                (next_msg.header.stamp.secs + (next_msg.header.stamp.nsecs * 1e-6))
                - (initial_msg.header.stamp.secs + (initial_msg.header.stamp.nsecs * 1e-6))
            )

            for odom_msg in odom_messages:
                yield Odometry.from_dict(odom_msg)

    def _notify_poses(self, *args):
        """Appelle ``callback`` de facon cyclique dans une tâche de fond."""
        while not self._stop_event.is_set():
            try:
                msg = next(self._message_generator)
                self._callback(msg, *args)
                time.sleep(self._time_delta)
            except StopIteration:
                print("Bonne chance !")
                break



if __name__ == '__main__':

    t_start = time.time()

    def print_pose(msg: Odometry):
        print(f"{time.time() - t_start:.3f}s : x={msg.pose.position.x:.2f}, y={msg.pose.position.y:.2f}")
    
    sub = Subscriber("/odom", Odometry, callback=print_pose)

    while sub.is_running():
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            sub.stop()
