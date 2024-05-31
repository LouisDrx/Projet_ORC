from dataclasses import dataclass
import math
import numpy as np 
try:
    from . import odom_message
except ImportError:
    import odom_message


@dataclass
class Point:
    x: float
    y: float


class Trajectory:

    def __init__(self, *points: Point):
        """Initialization de la trajectoire à partir de points étapes."""
        self._points: list[Point] = []
        for point in points:
            self.add_point(point)

    def add_point(self, point: Point):
        """Ajoute un point à la trajectoire."""
        self._points.append(point)
    
    def __len__(self):
        return len(self._points)

    def generate(self, n_points: int) -> list[odom_message.Odometry]:
        """Génère la trajectoire avec le nombre donné de points intermédiaires entre 2 étapes."""
        time_interval = 1 / n_points

        pos_x = np.concatenate(
            [np.linspace(self._points[i].x, self._points[i+1].x, n_points) for i in range(len(self) - 1)]
        )
        pos_y = np.concatenate(
            [np.linspace(self._points[i].y, self._points[i+1].y, n_points) for i in range(len(self) - 1)]
        )
        v_x = np.gradient(pos_x, time_interval)
        v_y = np.gradient(pos_y, time_interval)

        angle_x = np.arctan2(pos_y, pos_x)
        angle_y = np.arctan2(pos_x, pos_y)

        return [
            odom_message.Odometry(
                header=odom_message.Header(
                    seq=cnt, 
                    stamp=odom_message.Stamp(
                        secs=math.trunc(cnt * time_interval), 
                        nsecs=int(round(((cnt * time_interval) % 1) * 1e6))
                    ),
                    frame_id=None
                ),
                pose=odom_message.Pose(
                    position=odom_message.Coordinates3D(x, y, 0),
                    orientation=odom_message.Quaternion(0, 0, 0, 0)
                ),
                twist=odom_message.Twist(
                    linear=odom_message.Coordinates3D(vx, vy, 0),
                    angular=odom_message.Coordinates3D(0, 0, 0)
                )
            )
            for cnt, (x, y, vx, vy) in enumerate(
                zip(pos_x, pos_y, v_x, v_y)
            )
        ]

if __name__ == "__main__":
    import json
    from pathlib import Path

    trajectory = Trajectory(
        Point( 0,  0),
        Point( 0, 10),
        Point( 5, 15),
        Point(10, 10),
        Point( 0, 10),
        Point(10,  0),
        Point( 0,  0),
        Point(10, 10),
        Point(10,  0),
    )

    with open(Path(__file__).parent / "trajectory.json", "w") as out_file:
        json.dump(
            [odom.to_dict() for odom in trajectory.generate(n_points=100)], 
            out_file, 
            indent=2
        )

