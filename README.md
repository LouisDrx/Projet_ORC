# Projet_ORC

Projet python du groupe ORC composé de Farcasiu-Popovici Théo, Khalfi Rayann, Sauzay Erwan et Dreux Louis

Le projet a été réalisé pendant l'année scolaire 2023-2024 lors de la 1er année en Automatique et système embarquée à l'ENSISA

Le projet a pour but le développement d'une application graphique permettant de se connecter à un robot TurtleBot3, de visualiser ses mouvements et de commander ses déplacements. Le projet a été réalisé par une équipe de quatre personnes sur une période de 6 semaines. L'application a été développée en Python en utilisant TKinter pour l'interface graphique et matplotlib.animation pour les graphiques. 

Le projet est encore en cours de progression, nous avons des soucis au lancement de gazebo que ce soit sur machine virtuelle ou sur un linux booté sur une clé usb.

Le projet a été codeé sous python.

Le dossier source contient différents programmes permettant de lancer l'interface graphique, d'acquérir les données du déplacement du robot et aussi une base de données avec des coordonnées d'un robot qui se déplacerait dans un espace. 
Vous pouvez voir ci-dessous une démo de l'interface graphique :

![Animation](https://github.com/LouisDrx/Projet_ORC/assets/153221009/cd3fdbb8-0531-4a24-b441-604f8f6d9f7a)

NB : L'apparition d'un sinus sur le graphique est voulue dans cette démo

Dans cette deuxième démo, on lance le programme avec une base de données où l'on récupère des coordonnées, on peut voir sur le graphique le chemin parcouru par le robot.

![Animation_coord_doc](https://github.com/LouisDrx/Projet_ORC/assets/153221009/7fb3d86c-5aed-4bae-902e-8fb0c4affd3f)

Les problèmes rencontrés lors de ce projets sont les suivants :

- GUI : Trouver les différentes bibliothèques python pour actualiser l’acquisition de données
- GUI : Récupération des coordonnées depuis un document pour les implanter sur le graphique
- Acquisition de données: Réussir à ouvrir le fichier json et d’importer le PATH
- Gazebo : Non possibilité de le lancer que ce soit sur machine virtuelle ou clé bootable, même en suivant différents tuto a la lettre impossible, soit des packages sont corrompus et même en les réinstallant ils le sont encore, ou des repository ont disparu du git sur lequel le tuto nous envoie cloner et donc une fois lancer il y a des fichier manquant. Une explication a certaine erreur a été trouver sur un forum (je n'ai plus le lien) ou il parle de la compatibilité des processeurs avec gazebo.
- Manque de temps et de session pour faire le projet
- Difficulté à connecter ROS avec le robot turtlebot

Pour faire fonctionner les codes, il vous faudra installer les bibliothèques mentionnées dans le requirement.txt 

Pour retrouver les consignes de l'exercice demandé, veuillez consulter le fichier consigne.md

### Conclusion 
Le projet a été une réussite grâce à une planification rigoureuse, une répartition claire des tâches et une bonne communication entre les membres de l’équipe. Malgré les défis rencontrés, nous avons su les surmonter et livrer une application robuste et performante. Les connaissances et les compétences acquises durant ce projet seront précieuses pour les futurs développements.
