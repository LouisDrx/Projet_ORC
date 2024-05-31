#Utilisation Ros connexion

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class TurtlebotGUI:
    #Méthode start :

    def start(self):
        if not self.connected: #Vérifie si la connexion n'est pas déjà établie (if not self.connected:).
            try:
                rospy.init_node('turtlebot_gui', anonymous=True)#Initialise le noeud ROS avec rospy.init_node('turtlebot_gui', anonymous=True).
                rospy.Subscriber('/odom', Odometry, self.update_position)#S'abonne au topic /odom pour recevoir les données de position du robot avec rospy.Subscriber('/odom', Odometry, self.update_position).
                self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)#Initialise un Publisher pour envoyer des commandes de vitesse au robot avec self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10).
                self.connected = True#Met à jour l'état de la connexion (self.connected = True) et change l'indicateur de statut à "Connected" avec une couleur verte (self.status_label.config(text="Status: Connected", fg="green")).
                self.status_label.config(text="Status: Connected", fg="green")
            except rospy.ROSException as e:
                messagebox.showerror("Connection Error", str(e))#En cas d'erreur, affiche un message d'erreur.

    #Méthode stop:

    def stop(self):
        if self.connected:#Vérifie si la connexion est active (if self.connected:).
            self.connected = False#Met à jour l'état de la connexion (self.connected = False) 
            self.status_label.config(text="Status: Disconnected", fg="red")#et change l'indicateur de statut à "Disconnected" avec une couleur rouge (self.status_label.config(text="Status: Disconnected", fg="red")).
            self.reset_position()#Réinitialise la position du robot sur le canvas en appelant self.reset_position().
    
    #Méthode update_position :

    def update_position(self, msg):
        if self.connected:
            x = msg.pose.pose.position.x * 50 + 200  #Met à jour la position du robot sur le canvas lorsque des données de position sont reçues.
            y = msg.pose.pose.position.y * 50 + 200  
            self.canvas.coords(self.robot, x-10, y-10, x+10, y+10)#Utilise une échelle et un décalage pour convertir les coordonnées du robot aux coordonnées du canvas.

    #Méthode reset_position :

    def reset_position(self):
        self.canvas.coords(self.robot, 190, 190, 210, 210)#Réinitialise la position du robot au centre du canvas.

    #Méthode on_closing :

    def on_closing(self):
        if self.connected:#Appelée lors de la fermeture de la fenêtre principale.
            self.stop()#Si la connexion est active, elle appelle self.stop() pour arrêter proprement la connexion.
        self.master.destroy()#Détruit la fenêtre principale (self.master.destroy()).

if __name__ == "__main__":
    root = tk.Tk()
    app = TurtlebotGUI(root)
    root.mainloop()
    #Démarre la boucle principale de l'application Tkinter pour répondre aux événements de l'interface utilisateur.
