# py-dice-roll
Un simple programme en python pour lancer les dés de Jeu de rôle avec une synthèse vocale.

Le programme integre la synthèse vocale pyttsx3 vous pouvez la désactiver en ajoutant l'argument mute au démarrage du programme.

# Paramètres

* --mute
désactive la synthèse vocale|
* --timecode
Ajoute un timecode avant chaque lancé|

# Touches Raccourcies AZERTY
* A = 1d20
* Z = 1d12
* E = 1d10
* R = 1d8
* T = 1d6
* Y = 1d4

# Autres commandes
* P ou Entrée = Répéter la derniere phrase prononcée
* O = Refaire le dernier lancé
* I = Ouvrir un fichier avec les 5 derniers lancés
* U = Ouvrir un fichier avec l'historique complet
* Q - Quitter le programme 

# Formes abrégés supportées
* 1d20 
* 3d20+3
* 2d4-1
* a+3
* 1.20
* 3x6
* ...

# Faire plusieurs lancés
Vous pouvez séparer les formes abrégées par point-virgule pour faire plusieurs lancés en même temps
* 1d20;a+3;Z;e 
* 3d20+3;T;2D6
* ...

