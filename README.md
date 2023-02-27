# ReadMe (Anne-Sophia Lim et Yanis Perrin)

## Présentation du projet

Notre projet pour l'unité **Data Engineering** porte sur les données du jeu vidéo FIFA23 développé par la société Electronic Arts. Ce projet a pour objectif de permettre aux joueurs de la célèbre license de pouvoir comparer les 500 meilleurs joueurs de football liés au mode de jeu **FIFA ULTIMATE TEAM**. 

### FIFA ULTIMATE TEAM, qu'est-ce que c'est ?

Ce mode de jeu adoré des joueurs permet à chaque utilisateur de créer son propre club et acheter des joueurs avec une monnaie virtuelle afin de créer sa propre équipe. Chaque joueur de football dans le jeu est désigné comme un objet avec une note basée sur sa qualité dans la vie réelle (sur 100). Au delà de la note générale, chaque joueur possède aussi d'autres notes qui évalue ses caractéristiques et ses aptitudes sur le terrain (vitesse, dribbles...). C’est donc aux utilisateurs de FUT* de compiler des équipes dans une formation de leur choix avec les joueurs de leur choix et d'affronter les utilisateurs du monde entier. 

*FUT : FIFA ULTIMATE TEAM

### Les données

Les données utilisés dans ce projet seront récupérées à partir de deux sites web : 

> - [Futwiz.com](https://www.futwiz.com/en/fifa23/players?page=0&release=raregold "Details sur les données de Futwiz"). 

Futwiz est un site qui répertorie les notes et les caractéristiques mais aussi les valeurs des différents joueurs de football du jeu. 

> - [Transfermarkt.fr](https://www.transfermarkt.fr/ "Details sur les données de Transfermarkt"). 

Transfermarkt est un site web reconnus par les acteurs du monde du football notamment pour connaître la valeur d'un joueur de football dans la vraie vie. On y trouve aussi de nombreuses informations sur la carrière de chaque joueur de football.

➡️  Ces données seront récupérées à partir de méthode de web scrapping.

## Sommaire


Ce *README* est composé de trois principales parties :

1. **User Guide** (Ce guide indique comment déployer et visualiser notre application)

    1. Cloner le projet.
    
    2. Déployer le projet.

2. **Developper Guide** (Ce guide permet de comprendre l’architecture du code)

    1. Récupération et nettoyage des données.
    
    2. Stockage, utilisation et affichage des données.
    
    3. Architecture du code.

3. **Rapport de fonctionnalité** (Ce rapport explique les différentes fonctionnalités de l'application)

    1. Visualisation des informations principales des joueurs.
    
    2. Outils de comparaison des joueurs.
    
    3. Visualisation de statistiques liées aux équipes.


*À noter que l'entièreté du projet (code, rendu) sera en anglais pour raison de simplicité.*

## User Guide

### Cloner le projet

Pour pouvoir accéder à notre projet, il faut pouvoir cloner l'original accessible depuis git.

Lancer un terminal gitbash (windows) dans le répertoite où vous allez stocker le projet.

Ecrire les instructions suivantes:

> git config --global core.autocrlf false

> git clone https://github.com/YanisPerrin/DSIA-4201C-LIM-PERRIN.git

### Déployer le projet

Afin de déployer le projet, il faut que vous ayez installer **Docker Desktop** sur votre pc, c'est le seul pré-requis.

Suivre les instructions suivantes :

> Se rendre dans un terminal (vs code ou celui de windows) à l'endroit où est stocker le projet.

> Ouvrir Docker Desktop.

> Dans le terminal, exécuter la commande "docker compose up".

> Une fois la commande lancée, se rendre dans la liste des conteneurs de Docker Desktop et lancer le lien au port "8501:8501" de l'image "streamlit-1" du conteneur "dsia-4201c_lim_perrin".

Vous pouvez désormais visualiser et interargir avec notre application.

## Developper Guide

### Récupération des données

#### Scrapping

Pour récupérer les données des sites web cités précédemment, il faut récupérer le code HTML des sites à partir d'une requête. Lorsque le texte d'un site est récupérer il faut le parser. Pour cela, nous avons utilisé BeautifulSoup 4 qui permet de transformer la structure HTML en objet Python. 

Pour cela, notre code possède 3 principales fonctions :

- recup_futwiz_1()

- recup_futwiz_2()

- recup_transfermarkt()

La fonction **recup_futwiz_1()** scrappe les données des pages principales de futwiz, c'est-à-dire les pages où l'ensemble des joueurs sont affichés ainsi que leurs informations principales. On récupère leur nom, leur équipe... ainsi que les href (lien qui pointe vers la page du joueur) qui sont très important pour que l'on puisse ensuite accéder aux pages de chaque joueur et donc récupérer toutes les données précises qui nous intéresse dans la fonction recup_futwiz_2(). Les href font le lien avec la fonction recup_futwiz_2(). 

La fonction **recup_futwiz_2()** récupère toutes les statistiques précises de chaque joueur (dribbles, vitesse...) à partir des href récupérés précédemment. Elle prend en paramètre la liste des href et les noms des joueurs.

Enfin, la fonction **recup_transfermarkt()** récupère les données transfermarkt (sponsor et valeur du joueur) à partir des noms des joueurs récupérés dans la première fonction. Elle prend en paramètre la liste des noms des joueurs. Cette fonction est couplé aux fonctions **transform_link()** et **no_recognize()** qui transforment simplement la liste des noms pour que transfermarkt reconnaisse les requêtes des liens http. 

Exemple : 

>https://www.transfermarkt.fr/schnellsuche/ergebnis/schnellsuche?query=Neymar+Jr

Transfermarkt ne reconnaît pas "Neymar+Jr" mais plutôt : 

>https://www.transfermarkt.fr/schnellsuche/ergebnis/schnellsuche?query=Neymar

On modifie donc "Neymar+Jr" en "Neymar".
#### Nettoyage des données

On nettoie les données pour les rendre utilisable par la suite et construire un fichier JSON viable via la fonction **clean_data()**. 

### Stockage, utilisation et affichage des données

#### Stockage

Maintenant que les données sont récupérés et traités, il faut que l'on stocke ces données. Pour cela, nous avons utilisé la base de donnée **MongoDb**. Le fichier **init_mongo.py** initialise la connexion à MongoDb afin d'éviter de relancer des requêtes insert_many() qui causeront la dupplication des données dans la base. Nous utilisons la librairie **pymongo** pour effectuer les requêtes mongo à partir de python.

#### Utilisation

À travers le code, nous utiliserons dans la grande majorité les données récupérées via des requêtes mongo. Ces dernières nous permettront d'afficher correctement toutes les données et graphiques. 

*pour plus de précision, voir le code documenté.*

#### Affichage

Pour de ce qui est de l'affichage, nous avons opté pour l'outil de création d'application **Streamlit**. L'objectif de l'unité n'étant pas de faire du développement web, nous avons préféré cette outil à **Flask** ou **Dash**.

*Nous avions bien évidemment validé cette solution avec Mr. Courivaud auparavant.*

#### Partage de l'application

Pour pouvoir partager efficacement l'application sans forcer l'utilisateur à installer toutes les dépendances et librairies, nous avons opté pour la solution **Docker**. L'utilisateur a seulement besoin de **Docker Desktop** pour lancer l'application. Le développement d'un ***Dockerfile*** et d'un ***docker-compose*** a été nécessaire.

#### Architecture du code

[![](https://mermaid.ink/img/pako:eNqNVd1u2jAUfpXIk7obejFYu5aLSbRdr7apAu0OyTLJcbBw7Mw5UUVLH4i9Bi-2k5jGAQKUC2TO-b7v_Nq8stgmwIZMavscz4XD6Od4aiL6-O-inKVO5PNo5OK5QoixdMCTklc8D6k-DuIy57LEZ_XCv0QXu4Z-Y0AnTCHBZcItMLq8_B6txps1eTZrB6so1iAMTwSKIP3LmtR66ARtvAASG8PfcvMPiZFTygrqkNtjPxwHQSUoe6nfgGgVCdTyASetiVFZY4RWuFnXwvu2fodtUMtO0IHIyBIEfcXWZVwrsyCmsZx6YVOjXsDn8qg0VtV3tGi_wztOX4jIiHo6SlBpxtl0XVRV8AQKnlA1mzUUR6dax5s7kL3I1FF3h3ya12YcKRFM0pGp786xhgZ7u-JzmvX0lyKFI4V37WG3Ur2SJLS3rx8qqooPyP-g0qo4NYdmyamTIkm4JDY4XqCjSbcMyrS6eQZYT-Vg2w9i9mvck7aol8Hpf3dK9A8k_NVIqFKRpg7SutKA2nN0ig7O9XMkpaLnqz2H5i5GR8j-1JgarSdK268G159FnmsVt1Ju8F0PIuW-eqjeKLc6I1PgUkNIO6LB6OEneXvddn9kS7bM2Uy2md0LvsXeDG5udwO9b_EWcHU9uvpx3waceC62nK-Du8f7bwfZQ4eb9VhWXX6V0B_Pa2WbMpxDBlM2pGMCUpQap2xq3ggqSrSTpYnZEF0JPVbmdC_hQQmaVsaGUugC3v4DRw9H1A?type=png)](https://mermaid.live/edit#pako:eNqNVd1u2jAUfpXIk7obejFYu5aLSbRdr7apAu0OyTLJcbBw7Mw5UUVLH4i9Bi-2k5jGAQKUC2TO-b7v_Nq8stgmwIZMavscz4XD6Od4aiL6-O-inKVO5PNo5OK5QoixdMCTklc8D6k-DuIy57LEZ_XCv0QXu4Z-Y0AnTCHBZcItMLq8_B6txps1eTZrB6so1iAMTwSKIP3LmtR66ARtvAASG8PfcvMPiZFTygrqkNtjPxwHQSUoe6nfgGgVCdTyASetiVFZY4RWuFnXwvu2fodtUMtO0IHIyBIEfcXWZVwrsyCmsZx6YVOjXsDn8qg0VtV3tGi_wztOX4jIiHo6SlBpxtl0XVRV8AQKnlA1mzUUR6dax5s7kL3I1FF3h3ya12YcKRFM0pGp786xhgZ7u-JzmvX0lyKFI4V37WG3Ur2SJLS3rx8qqooPyP-g0qo4NYdmyamTIkm4JDY4XqCjSbcMyrS6eQZYT-Vg2w9i9mvck7aol8Hpf3dK9A8k_NVIqFKRpg7SutKA2nN0ig7O9XMkpaLnqz2H5i5GR8j-1JgarSdK268G159FnmsVt1Ju8F0PIuW-eqjeKLc6I1PgUkNIO6LB6OEneXvddn9kS7bM2Uy2md0LvsXeDG5udwO9b_EWcHU9uvpx3waceC62nK-Du8f7bwfZQ4eb9VhWXX6V0B_Pa2WbMpxDBlM2pGMCUpQap2xq3ggqSrSTpYnZEF0JPVbmdC_hQQmaVsaGUugC3v4DRw9H1A)

### Rapport de fonctionnalité

#### Visualisation des informations principales des joueurs

Notre première fonctionnalité porte sur la visualisation des informations principales des joueurs. À l'aide de la ***sidebar*** à disposition de l'utilisateur, celui-ci peut appliquer des filtres aux données affichées. De nombreux filtres sont disponibles comme les sponsors des joueurs, l'âge des joueurs ou encore les équipes des joueurs. Deux types de filtres peuvent être appliquer :

- **Un slider**

- **Un sélecteur**

#### Outils de comparaison des joueurs

Notre deuxième fonctionnalité porte sur la comparaison des statistiques générales d'un ou plusieurs joueurs. L'utilisateur peut comparer les statistiques des joueurs soit par visualisation des données simples soit par un ***Spider Chart*** créer via **Plotly** une libraire python qui permet de créer les graphiques. 

L'utilisateur peut aussi visualiser les statistiques avancées via un ***Bar Chart*** et les comparer entre les joueurs selectionnés.

#### Visualisation des statistiques liées aux équipes

Notre dernière fonctionnalité porte sur la visualisation de certaines statistiques des équipes comme le nombre de joueurs de l'équipe dans le top 500 ou encore son rang par rapport aux autres équipes.

### Conclusion sur le projet

Après de nombreuses heures passés à scrapper et développer cette application, nous sommes fiers de rendre une application stable et qui ne présente pas de bugs. Nous avons du faire face à de nombreux problèmes comme le fait que les serveurs de futwiz crashent lorsque trop de requêtes lui sont demandés ou le changement de site vers futwiz car l'ancien présentait trop peu de données. 

Quelques améliorations peuvent être apportées comme le fait d'ouvrir cette application aux données des précédentes années ou encore à tous les joueurs de football présents dans le jeu. Nous avions décidé de limiter ce nombre de données car il y'avait déjà assez pour développer une application (26 000 observations, 52 variables, 500 joueurs).

Étant de grands fans du ballon rond, nous sommes satisfaits et fiers de cette application. 