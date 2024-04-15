AOO Python – Projet
Consignes générales
A faire par groupe de 4 : les mêmes groupes que pour le projet TurtleBot.
Rendus
Un dépôt GitHub contenant :

Un fichier README.md avec les informations générales sur votre projet : noms des contributeurs, description, structure générale du projet, comment exécuter votre projet. N’hésitez pas à inclure des images, schéma etc…

Un fichier requirements.txt contenant les différents packages python qu’il est nécessaire d’installer pour pouvoir utiliser le projet.

Le code source dans un dossier « src »

Les tests unitaires dans un dossier « tests »

De la documentation supplémentaire (en Markdown également, dans un dossier « docs »)
Une ou plusieurs vidéos où vous montrerai votre programme en application avec le robot TurtleBot. Vous pourrez utiliser Moodle pour déposer les vidéos.
A rendre individuellement en plus : votre impression sur la bonne répartition de la charge de travail au sein des membres du groupe.
Google Forms à envoyer : https://forms.gle/KCsk9Ngr6h7nhqZN6
Date de rendu : dimanche 9 juin 2024, à 23h59
Travail demandé
L’objectif est de réaliser une application avec une interface graphique (« GUI » = graphical user interface) qui permet de se connecter au robot. Une fois connecté, l’utilisateur peut visualiser les mouvements du robot et commander des déplacements.
L’application devra être codée entièrement en Python et utiliser TKinter pour la partie interface graphique.
Les graphiques devront être réalisés à partir de matplotlib.animation.
L’application devra être utilisée comme suit :
1.
Démarrer le robot et les services ROS
2.
Sur un ordinateur distant (non la Raspberry PI), ouvrir l’application graphique. L’ordinateur distant doit être connecté sur le réseau WiFi du robot.
3.
Sur l’interface, rentrer les informations nécessaires (ROS master URI et ROS hostname) pour se connecter au robot. Appuyer ensuite sur un bouton « Start » pour commencer à réceptionner des données en provenance du robot. Une icône doit indiquer que la réception est active dans l’interface graphique (par exemple un logo qui passe de la couleur grise à la couleur verte). La réception des données de navigation du Turtlebot sera réalisée en réalisant un Subscriber ROS pour le topic /odom du Turtlebot. Un exemple minimal est implémenté ici.
4.
Utiliser l’application pour commander des déplacements au robot et visualiser ses mouvements (position relative et vitesse du robot). Le robot sera représenté par un point dans le plan (x, y). La commande des déplacements du Turtlebot sera réalisée par un Publisher ROS envoyant des messages de type Twist au topic /odom du Turtlebot. Un exemple est implémenté ici.
5.
Stopper la réception des données en appuyant sur un bouton « Stop ». L’icône de connexion doit indiquer lorsque la déconnexion est terminée (par exemple en changeant la couleur en gris à nouveau). La position relative du robot revient à (0, 0).
L’interface utilisateurs devra être divisée en trois zones.

•
Zone « connexion avec le robot » :
o
Un ou plusieurs champs de texte pour saisir les informations nécessaires pour se connecter au robot
o
Un bouton START
o
Un bouton STOP
o
Un icône représentant si l’acquisition des données est actuellement en cours ou non.

•
Zone « Mouvement du robot »
o
Vitesse linéaire et angulaires sur des graphiques. On pourra utiliser le package « matplotlib »
o
Position relative du robot sur un plan 2D. On pourra également utiliser « matplotlib »
o
Les valeurs doivent s’actualiser au moins 2 fois par secondes

•
Une zone « Commande ». Proposition :
o
Bouton Avancer
o
Bouton Reculer
o
Bouton Pivoter vers la gauche
o
Bouton Pivoter vers la droite
o
Un champ de texte ou un « slider » pour la vitesse linéaire de commande
o
Un champ de texte ou un « slider » pour la vitesse angulaire de commande
o
La commande est envoyée au robot dès que l’utilisateur appuie sur un bouton. Une commande de retour à zéro est envoyée dès que l’utilisateur relâche le bouton.
Une solution courante pour concevoir une application avec une interface utilisateur est le pattern « MVC » pour « Model View Controller ». Nous vous conseillons de lire ce tutoriel sur OpenClassrooms, mais vous pouvez trouver de nombreuses ressources sur le web. Il existe plusieurs versions légèrement différentes de ce pattern (MVP, MVVM…), il ne s’agit donc pas d’appliquer un tutoriel à la lettre, mais d’utiliser ce principe pour séparer les responsabilités au sein du code.
Pour aller plus loin
Stockez tous les mesures du robot reçues par votre application dans un fichier de logs. Ce fichier est écrasé à chaque nouveau lancement de l’application. Vous pouvez pour cela utiliser le package « logging » inclus dans la bibliothèque standard de Python.
Ce fichier pourrait ressembler à :
INFO 2024-04-05 11:29:51,758 - Robot connected
DEBUG 2024-04-05 11:29:52,433 - Vx=0.00, Ax=0.00
DEBUG 2024-04-05 11:29:53,434 - Vx=1.23, Ax=0.56
DEBUG 2024-04-05 11:29:54,551 - Vx=1.45, Ax=0.34
[...]
INFO 2024-04-05 11:35:52,011 - Robot disconnected
Critères d’évaluation

•
Un projet bien structuré

•
Le projet est bien documenté (README et documentation supplémentaire)

•
L’application s’exécute sans erreur et affiche des informations pertinentes

•
Le code est testé et tous les tests passent. On ne demande pas 100% de couverture. Ecrivez des tests qui ont du sens et pertinents pour vérifier le bon fonctionnement de votre application.

•
La code source respecte les règles de bonnes pratiques vues en cours : conventions PEP8, formatage, annotations de types, etc… Séparez votre code source en plusieurs modules.

•
L’utilisation des principes de la programmation orienté objet dans le code source. Attention, cela ne veut pas dire que tout doit devenir une classe ! Il vaut toujours mieux privilégier la simplicité.

•
L’utilisation de Git et GitHub dont vous aurez fait preuve pour collaborer à plusieurs. Chacun devra toujours travailler sur une branche, puis ouvrir une Pull Request. Demandez ensuite aux autres membres du projet de relire votre contribution, de suggérer des améliorations ou de valider. Mergez ensuite sur la branche principale.
La note sera normalement la même pour tous les membres du projet, sauf si une grande différence de contribution est mise en évidence. Cela pourra être fait en regardant l’historique des activités sur les dépôts GitHub ainsi que grâce aux retours individuels.
