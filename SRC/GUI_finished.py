import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import threading
import time

class RobotControlApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contrôle du Robot")

        # Zone "Connexion avec le robot"
        self.frame_connexion = ttk.LabelFrame(self, text="Connexion avec le robot")
        self.frame_connexion.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        self.label_ip = ttk.Label(self.frame_connexion, text="Adresse IP:")
        self.label_ip.grid(row=0, column=0, padx=5, pady=5)
        self.entry_ip = ttk.Entry(self.frame_connexion)
        self.entry_ip.grid(row=0, column=1, padx=5, pady=5)

        self.label_port = ttk.Label(self.frame_connexion, text="Port:")
        self.label_port.grid(row=1, column=0, padx=5, pady=5)
        self.entry_port = ttk.Entry(self.frame_connexion)
        self.entry_port.grid(row=1, column=1, padx=5, pady=5)

        self.btn_connect = ttk.Button(self.frame_connexion, text="CONNECT", command=self.check_connection)
        self.btn_connect.grid(row=1, column=2, padx=5, pady=5)
        
        self.label_status = ttk.Label(self.frame_connexion, text="Statut: Déconnecté", foreground="red")
        self.label_status.grid(row=0, column=2, padx=5, pady=5)        

        self.btn_start = ttk.Button(self.frame_connexion, text="START", command=self.start_acquisition)
        self.btn_start.grid(row=2, column=0, padx=5, pady=5)
        self.btn_stop = ttk.Button(self.frame_connexion, text="STOP", command=self.stop_acquisition)
        self.btn_stop.grid(row=2, column=1, padx=5, pady=5)

        self.label_acquisition = ttk.Label(self.frame_connexion, text="Acquisition en cours", foreground="green")
        self.label_acquisition.grid(row=2, column=2, padx=5, pady=5)

        # Zone "Mouvement du robot"
        self.frame_mouvement = ttk.LabelFrame(self, text="Mouvement du robot")
        self.frame_mouvement.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        self.fig, self.ax1 = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_mouvement)
        self.canvas.get_tk_widget().pack()

        # Zone "Commande"
        self.frame_commande = ttk.LabelFrame(self, text="Commande")
        self.frame_commande.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        self.btn_avancer = ttk.Button(self.frame_commande, text="Avancer", command=self.commande_avancer)
        self.btn_avancer.grid(row=0, column=0, padx=5, pady=5)
        self.btn_reculer = ttk.Button(self.frame_commande, text="Reculer", command=self.commande_reculer)
        self.btn_reculer.grid(row=0, column=1, padx=5, pady=5)
        self.btn_gauche = ttk.Button(self.frame_commande, text="Pivoter Gauche", command=self.commande_gauche)
        self.btn_gauche.grid(row=1, column=0, padx=5, pady=5)
        self.btn_droite = ttk.Button(self.frame_commande, text="Pivoter Droite", command=self.commande_droite)
        self.btn_droite.grid(row=1, column=1, padx=5, pady=5)

        self.label_vitesse_lineaire = ttk.Label(self.frame_commande, text="Vitesse linéaire:")
        self.label_vitesse_lineaire.grid(row=2, column=0, padx=5, pady=5)
        self.scale_vitesse_lineaire = ttk.Scale(self.frame_commande, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale_vitesse_lineaire.grid(row=2, column=1, padx=5, pady=5)

        self.label_vitesse_angulaire = ttk.Label(self.frame_commande, text="Vitesse angulaire:")
        self.label_vitesse_angulaire.grid(row=3, column=0, padx=5, pady=5)
        self.scale_vitesse_angulaire = ttk.Scale(self.frame_commande, from_=-100, to=100, orient=tk.HORIZONTAL)
        self.scale_vitesse_angulaire.grid(row=3, column=1, padx=5, pady=5)

        # Variables pour l'état de l'acquisition
        self.acquisition_en_cours = False

    def check_connection(self):
        ip = self.entry_ip.get()
        port = self.entry_port.get()
        try:
            with socket.create_connection((ip, int(port)), timeout=5):
                self.label_status.config(text="Statut: Connecté", foreground="green")
                self.btn_start.config(state=tk.NORMAL)
                self.btn_stop.config(state=tk.NORMAL)
        except (socket.timeout, ConnectionRefusedError, OSError):
            self.label_status.config(text="Statut: Déconnecté", foreground="red")
            self.btn_start.config(state=tk.DISABLED)
            self.btn_stop.config(state=tk.DISABLED)
    
    def start_acquisition(self):
        self.acquisition_en_cours = True
        self.label_acquisition.config(text="Acquisition en cours", foreground="green")
        self.thread_acquisition = threading.Thread(target=self.actualiser_donnees)
        self.thread_acquisition.start()

    def stop_acquisition(self):
        self.acquisition_en_cours = False
        self.label_acquisition.config(text="Acquisition arrêtée", foreground="red")

    def actualiser_donnees(self):
        while self.acquisition_en_cours:
            # Actualiser les données des graphiques
            # Simulation de données pour l'exemple
            x = np.linspace(0, 10, 100)
            y = np.sin(x)
            self.ax1.clear()
            self.ax1.plot(x, y)
            self.canvas.draw()

            # Actualiser la position relative du robot sur un plan 2D
            # Simulation de données pour l'exemple
            time.sleep(0.5)

    def commande_avancer(self):
        vitesse_lineaire = self.scale_vitesse_lineaire.get()
        vitesse_angulaire = self.scale_vitesse_angulaire.get()
        print(f"Commande : Avancer avec vitesse linéaire {vitesse_lineaire} et vitesse angulaire {vitesse_angulaire}")

    def commande_reculer(self):
        vitesse_lineaire = self.scale_vitesse_lineaire.get()
        vitesse_angulaire = self.scale_vitesse_angulaire.get()
        print(f"Commande : Reculer avec vitesse linéaire {vitesse_lineaire} et vitesse angulaire {vitesse_angulaire}")

    def commande_gauche(self):
        vitesse_lineaire = self.scale_vitesse_lineaire.get()
        vitesse_angulaire = self.scale_vitesse_angulaire.get()
        print(f"Commande : Pivoter vers la gauche avec vitesse linéaire {vitesse_lineaire} et vitesse angulaire {vitesse_angulaire}")

    def commande_droite(self):
        vitesse_lineaire = self.scale_vitesse_lineaire.get()
        vitesse_angulaire = self.scale_vitesse_angulaire.get()
        print(f"Commande : Pivoter vers la droite avec vitesse linéaire {vitesse_lineaire} et vitesse angulaire {vitesse_angulaire}")

if __name__ == "__main__":
    app = RobotControlApp()
    app.mainloop()
