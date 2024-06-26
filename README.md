# Projet_ORC

Projet python du groupe ORC composé de Farcasiu-Popovici Théo, Khalfi Rayann, Sauzay Erwan et Dreux Louis

Le projet a été réalisé pendant l'année scolaire 2023-2024 lors de la 1er année en Automatique et système embarquée à l'ENSISA

Le projet a pour but le développement d'une application graphique permettant de se connecter à un robot TurtleBot3, de visualiser ses mouvements et de commander ses déplacements. Le projet a été réalisé par une équipe de quatre personnes sur une période de 6 semaines. L'application a été développée en Python en utilisant TKinter pour l'interface graphique et matplotlib.animation pour les graphiques. 

Le projet est encore en cours de progression, nous avons des soucis au lancement de gazebo que ce soit sur machine virtuelle ou sur un linux booté sur une clé usb.

Le projet a été codé sous python.

Le dossier source contient différents programmes permettant de lancer l'interface graphique, d'acquérir les données du déplacement du robot et aussi une base de données avec des coordonnées d'un robot qui se déplacerait dans un espace. 

### Utilisation fonctionnalités :
- Lancer pose_subscriber.py pour générer les coordonnées de position du Turtle bot au cours du temps
- Lancer Gui_finished.py pour lancer l'interface graphique
    - La connexion avec le robot n'est pas fonctionnelle 
    - Appuier sur start permet de voir l'affichage graphique d'une      simulation de déplacement 
    - Modifier les curseurs de commande et appuier sur les bouttons de commande permet d'informe du chagement de directive operatoire du robot. 

Vous pouvez voir ci-dessous une démo de l'interface graphique :

![Animation](https://github.com/LouisDrx/Projet_ORC/assets/153221009/cd3fdbb8-0531-4a24-b441-604f8f6d9f7a)

NB : L'apparition d'un sinus sur le graphique est voulue dans cette démo

Dans cette deuxième démo, on lance le programme avec une base de données où l'on récupère des coordonnées, on peut voir sur le graphique le chemin parcouru par le robot.

![Animation_coord_doc](https://github.com/LouisDrx/Projet_ORC/assets/153221009/7fb3d86c-5aed-4bae-902e-8fb0c4affd3f)

Les problèmes rencontrés lors de ce projets sont les suivants :

- GUI : Trouver les différentes bibliothèques python pour actualiser l’acquisition de données
- GUI : Récupération des coordonnées depuis un document pour les implanter sur le graphique
- Acquisition de données: Réussir à ouvrir le fichier json et d’importer le PATH
- Gazebo : Non possibilité de le lancer que ce soit sur machine virtuelle ou clé bootable, même en suivant différents tutoriels à la lettre. Soit des packages sont corrompus et même en les réinstallant ils le sont encore, soit des repositories ont disparu du git sur lequel le tuto nous envoie cloner et donc une fois lancé il y a des fichiers manquants. Une explication à certaines erreurs a été trouvée sur un forum (je n'ai plus le lien) où il parle de la compatibilité des processeurs avec gazebo.
- Manque de temps et de session pour faire le projet
- Difficulté à connecter ROS avec le robot turtlebot


Pour faire fonctionner les codes, il vous faudra installer les bibliothèques mentionnées dans le requirement.txt 

Pour retrouver les consignes de l'exercice demandé, veuillez consulter le fichier consigne.md

## Répartition des Tâches 
L'équipe était composée de quatre membres : Rayann, Théo, Erwan et Louis. Voici la répartition des tâches : 
### Rayann 
- Développement du code python pour l’acquisition des données sous ROS 
- Développement du code Python pour l’acquisition des données via le dossier données 
- Gestion de la base de données 
- Documentation du Projet 
### Théo 
- Conception de l'interface utilisateur avec TKinter
- Développement des composants graphiques
- Mise en œuvre des interactions utilisateur
- Tests d’interface utilisateur
- Utilisation des données acquises dans la base de données sur l’interface GUI “Mouvement du robot”
### Erwan
- Prise en Main du logiciel GAZEBO
- Correction des codes
- Rédaction des spécifications fonctionnelles 
- Élaboration des plans de test
- Exécution des tests fonctionnels
 
### Louis 
- Prise en Main du logiciel GAZEBO
- Supervision de la bonne collaboration via github
- Rédaction du README et du requirment
- Élaboration des plans de test
- Exécution des tests fonctionnels  
- Vérification que les codes suivent la convention Pep8 


### Conclusion 
Le projet a été en partie réalisé. Il est possible de sélectionner des commandes sur une interface graphique et de visualiser des simulations sur cette même interface. La récupération des données sur Gazebo est le point qui pose problème dans notre projet. Le temps passé sur les dual boots ou les VM n’ont pas permis de l’utiliser. Nous nous sommes rabattus sur l’utilisation des données fournies.
A travers  nos travaux collaboratifs sur GIthub, nous nous sommes rendu compte de l’importance de bien documenter ses avances et qu’il fallait savoir faire machine arrière dans le développement de son code pour une bonne intégration avec un minimum de problèmes au sein du projet. 
Nous nous sommes aussi rendu compte  du processus de développement de code pour répondre à un besoin concret. 

