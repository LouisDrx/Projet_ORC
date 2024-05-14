import tkinter as tk

# Fonction pour la commande de mouvement
def move_forward():
    # Code pour envoyer la commande de mouvement "avancer" au robot
    print("Avancer")

def move_backward():
    # Code pour envoyer la commande de mouvement "reculer" au robot
    print("Reculer")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Contrôle du Robot")

# Création des boutons de commande
btn_forward = tk.Button(root, text="Avancer", command=move_forward)
btn_forward.pack()

btn_backward = tk.Button(root, text="Reculer", command=move_backward)
btn_backward.pack()

# Boucle principale de l'interface graphique
root.mainloop()