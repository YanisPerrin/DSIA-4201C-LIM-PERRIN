import streamlit as st
import pandas as pd 
import pandas as pd
from pymongo import MongoClient
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup

##################################################################################################################################################################
#PARTIE SCRAPPING

# Pour éviter que le programme lancé prenne 15 minutes, nous avons mis en commentaires les lignes qui run les fonctions. Nous utiliserons par la suite
#le fichier JSON "FIFA23.json" récupéré à partir de ces fonctions.

#Scrapping des noms, href, équipes, ligues, images et notes générales sur le site futwiz.com
def recup_data_futwiz_1():
    name=[]
    href=[]
    team=[]
    league=[]
    image=[]
    general_note=[]
    for i in range(0,20):    
        url="https://www.futwiz.com/en/fifa23/players?page="+str(i)+"&release=raregold"
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        all_names = soup.findAll(class_="name")
        all_teams = soup.findAll(class_="team")
        all_images = soup.find_all(class_="player-img")
        all_gen = soup.find_all(class_="otherversion23-txt")
        for names in all_names:
            name.append(names.text.replace("\n",""))
            href.append(names.find_all('a')[1].get('href'))
        for teams in all_teams:
            team.append(teams.find_all('a')[1].text)
            league.append(teams.find_all('a')[2].text)
        for images in all_images:
            image.append(images.get("src"))
        for gens in all_gen :
            general_note.append(gens.text)
    res=[name, href, team, league, image, general_note]
    return res
#futwiz_1=recup_data_futwiz_1()
#name=futwiz_1[0]
#href=futwiz_1[1]

#Utilisation de href récupéré dans la précédente fonction pour pouvoir accéder au page de chaque joueur et donc scrapper les notes des capacités
def recup_futwiz_2(name, href):
    pace_gen=[]
    shooting_gen=[]
    passing_gen=[]
    dribbling_gen=[]
    defending_gen=[]
    physical_gen=[]

    acceleration=[]
    sprint_speed=[]

    positioning=[]
    finishing=[]
    shot_power=[]
    long_shots=[]
    volleys=[]
    penalties=[]

    vision=[]
    crossing=[]
    free_kick_accuracy=[]
    short_pass=[]
    long_pass=[]
    curve=[]

    agility=[]
    balance=[]
    reactions=[]
    ball_control=[]
    dribbling=[]
    composure=[]

    interceptions=[]
    heading_accuracy=[]
    defense_awareness=[]
    stand_tackle=[]
    slide_tackle=[]

    jumping=[]
    stamina=[]
    strength=[]
    agression=[]

    skills=[]
    age=[]
    weight=[]
    height=[]
    foot=[]
    weak_foot=[]
    position=[]
    country=[]
    value_in_game=[]
    #pour chaque joueur on récupére les différentes statistiques
    for i in range(len(name)):  
            
                url="https://www.futwiz.com/"+href[i]
                response = requests.get(url)
                while not len(response.text)>0: #ici on veut être sur que la réponse ne soit pas vide pour éviter les erreurs de scrapping causées par une réponse vide (les serveurs de futwiz ne supporte parfois pas les requêtes qu'on lui envoît)
                    response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text)
                pace_gen.append(soup.find_all(class_="headline-stat-num")[0].text)
                shooting_gen.append(soup.find_all(class_="headline-stat-num")[1].text)
                passing_gen.append(soup.find_all(class_="headline-stat-num")[2].text)
                dribbling_gen.append(soup.find_all(class_="headline-stat-num")[3].text)
                defending_gen.append(soup.find_all(class_="headline-stat-num")[4].text)
                physical_gen.append(soup.find_all(class_="headline-stat-num")[5].text)
                acceleration.append(soup.find_all(class_="individual-stat-bar-stat textcolour accelerationstat")[0].text)
                sprint_speed.append(soup.find_all(class_="individual-stat-bar-stat textcolour sprintspeedstat")[0].text)
                positioning.append(soup.find_all(class_="individual-stat-bar-stat textcolour positioningstat")[0].text)
                finishing.append(soup.find_all(class_="individual-stat-bar-stat textcolour finishingstat")[0].text)
                shot_power.append(soup.find_all(class_="individual-stat-bar-stat textcolour shotpowerstat")[0].text)
                long_shots.append(soup.find_all(class_="individual-stat-bar-stat textcolour longshotstat")[0].text)
                volleys.append(soup.find_all(class_="individual-stat-bar-stat textcolour volleysstat")[0].text)#
                penalties.append(soup.find_all(class_="individual-stat-bar-stat textcolour penaltiesstat")[0].text)
                vision.append(soup.find_all(class_="individual-stat-bar-stat textcolour visionstat")[0].text)
                crossing.append(soup.find_all(class_="individual-stat-bar-stat textcolour crossingstat")[0].text)
                free_kick_accuracy.append(soup.find_all(class_="individual-stat-bar-stat textcolour fkaccstat")[0].text)
                short_pass.append(soup.find_all(class_="individual-stat-bar-stat textcolour shortpassstat")[0].text)
                long_pass.append(soup.find_all(class_="individual-stat-bar-stat textcolour longpassstat")[0].text)
                curve.append(soup.find_all(class_="individual-stat-bar-stat textcolour curvestat")[0].text)
                agility.append(soup.find_all(class_="individual-stat-bar-stat textcolour agilitystat")[0].text)
                balance.append(soup.find_all(class_="individual-stat-bar-stat textcolour balancestat")[0].text)
                reactions.append(soup.find_all(class_="individual-stat-bar-stat textcolour reactionsstat")[0].text)
                ball_control.append(soup.find_all(class_="individual-stat-bar-stat textcolour ballcontrolstat")[0].text)
                dribbling.append(soup.find_all(class_="individual-stat-bar-stat textcolour dribblingstat")[0].text)
                composure.append(soup.find_all(class_="individual-stat-bar-stat textcolour composurestat")[0].text)
                interceptions.append(soup.find_all(class_="individual-stat-bar-stat textcolour tactawarestat")[0].text)
                heading_accuracy.append(soup.find_all(class_="individual-stat-bar-stat textcolour headingaccstat")[0].text)
                defense_awareness.append(soup.find_all(class_="individual-stat-bar-stat textcolour markingstat")[0].text)
                stand_tackle.append(soup.find_all(class_="individual-stat-bar-stat textcolour standingtacklestat")[0].text)
                slide_tackle.append(soup.find_all(class_="individual-stat-bar-stat textcolour slidetacklestat")[0].text)
                jumping.append(soup.find_all(class_="individual-stat-bar-stat textcolour jumpingstat")[0].text)
                stamina.append(soup.find_all(class_="individual-stat-bar-stat textcolour staminastat")[0].text)
                strength.append(soup.find_all(class_="individual-stat-bar-stat textcolour strengthstat")[0].text)
                agression.append(soup.find_all(class_="individual-stat-bar-stat textcolour aggressionstat")[0].text)
                skills.append(soup.find_all(class_="player-info-stat")[0].text.replace("\n","")[0])
                age_inter=(soup.find_all(class_="player-info-stat"))
                age.append(age_inter[4].text.replace("\n","")[0:2])
                height_inter=(soup.find_all(class_="player-info-stat"))
                height.append(height_inter[5].text.replace("\n","")[-5:])
                weight_inter=(soup.find_all(class_="player-info-stat"))
                weight.append(weight_inter[6].text.replace("\n","")[:-8]) 
                foot_inter=(soup.find_all(class_="player-info-stat"))
                foot.append(foot_inter[3].text.replace("\n","")[:-4])
                weak_foot_inter=(soup.find_all(class_="player-info-stat"))
                weak_foot.append(weak_foot_inter[1].text.replace("\n","")[0])
                position_inter=(soup.find_all(class_="player-info-stat"))
                position.append(position_inter[7].text.replace("\n","")[:-3])
                country_inter=soup.find_all(class_="pname-club")
                country.append(country_inter[0].find("a").text.replace(" ",""))
                value_in_game.append(soup.find_all(class_="price-num")[0].text)
    res=[pace_gen,shooting_gen,passing_gen,dribbling_gen,defending_gen,physical_gen,acceleration,sprint_speed,positioning,finishing,shot_power,long_shots,volleys,penalties,vision,crossing,free_kick_accuracy,short_pass,long_pass,curve,agility,balance,reactions,ball_control,dribbling,composure,interceptions,heading_accuracy,defense_awareness,stand_tackle,slide_tackle,jumping,stamina,strength,agression,skills,age,weight,height,foot,weak_foot,position,country,value_in_game]
    return res
#futwiz_2=recup_futwiz_2(name, href)

#Création d'une fonction qui transforme les noms pour les rendre utilisables dans les liens transfermarkt (utilisé dans recup_transfermarkt)
def transform_link(nom):
    name=[]
    for names in nom:
        names=names.replace(" ","+")
        name.append(names)
    return(name) 

#Création d'une fonction pour les joueurs non reconnus par transfermarkt malgré transform_link()
def no_recognize(player, new_player, new_name):
    if player in new_name:
        new_name[new_name.index(player)]=new_player

#récupération des valeurs et des sponsors des joueurs sur le site transfermarkt
def recup_transfermarkt(name):
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    new_name=transform_link(name)

    #Certains joueurs ne sont pas reconnus dans transfermarkt car les noms de futwiz et de transfermarkt ne sont pas corrélés, on modifie donc ces noms pour que transfermarkt les reconnaisse et renvoie le bon joueur.
    no_recognize("Neymar+Jr","Neymar",new_name)
    no_recognize("Heung+Min+Son","heung-min+son",new_name)
    no_recognize("Fernando","Fernando+Francisco+Reges",new_name)
    no_recognize("Fabian","fabian+ruiz",new_name)
    no_recognize("Odisseas+Vlachodimos","Vlachodimos",new_name)
    no_recognize("Neto","norberto+murara",new_name)
    no_recognize("Andre-Franck+Zambo+Anguissa","Zambo+Anguissa",new_name)
    no_recognize("Jose+Sa","José+Pedro+Malheiro+de+Sá",new_name)
    no_recognize("Morales","josé+luis+morales",new_name)
    no_recognize("Kim+Min+Jae","Jae",new_name)
    no_recognize("Alexandr+Golovin","Golovin",new_name)
    no_recognize("Luis+Milla","Luis+Milla+Manzanares",new_name)

    value=[]
    href2=[]#href qui permettra d'accéder au page de chaque joueur
    sponsor=[]
    for j in range(0,len(new_name)):
        url = "https://www.transfermarkt.fr/schnellsuche/ergebnis/schnellsuche?query="+new_name[j]
        response = requests.get(url, headers=headers)
        while not len(response.text)>0:
            response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        value.append(soup.find_all(class_="rechts hauptlink")[0].text)
        href2.append(soup.find_all(class_="hauptlink")[0].find("a").get("href"))

    #on accède à la page de chaque joueur et on récupére le sponsor
    for w in range(0,len(href2)):
        try :
            url = "https://www.transfermarkt.fr"+href2[w]
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            sponsor.append(soup.find(text="Équipementier:").find_next('span').text)  
        except(AttributeError):
            sponsor.append("-") #Si le joueur n'a pas de sponsor alors on ajoute un "-"
    res=[value, sponsor]
    return res
#transfermarkt=recup_transfermarkt(name)

#Création de la dataframe
#data={
    #"Name" : name, "Age" : futwiz_2[36], "Weight (kg)" : futwiz_2[37], "Height (cm)" : futwiz_2[38], "Image" : futwiz_1[4], "Year" : 2023, "Country" : futwiz_2[42], "Team" : futwiz_1[2], "League" : futwiz_1[3], "Position": futwiz_2[41], "Value IRL (mio)" : transfermarkt[0], "Value in game" : futwiz_2[43], 
    #"Sponsor" : transfermarkt[1], "Foot" : futwiz_2[39], "Weak Foot (/5)" : futwiz_2[40], "Skills (/5)" : futwiz_2[35], "General Note" : futwiz_1[5], "General Pace" : futwiz_2[0], "General Shooting" : futwiz_2[1], "General Passing" : futwiz_2[2], 
    #"General Dribbling" : futwiz_2[3], "General Defending" : futwiz_2[4], "General Physical" : futwiz_2[5], "Acceleration" : futwiz_2[6], "Sprint Speed" : futwiz_2[7], "Positioning" : futwiz_2[8], "Finishing" : futwiz_2[9], 
    #"Shot Power" : futwiz_2[10], "Long Shots" : futwiz_2[11], "Volleys" : futwiz_2[12], "Penalties" : futwiz_2[13], "Vision" : futwiz_2[14], "Crossing" : futwiz_2[15], "Free Kick Accuracy" : futwiz_2[16], "Short Pass" : futwiz_2[17], "Long Pass" : futwiz_2[18], 
    #"Curve" : futwiz_2[19], "Agility" : futwiz_2[20], "Balance" : futwiz_2[21], "Reactions" : futwiz_2[22], "Ball Control" : futwiz_2[23], "Dribbling" : futwiz_2[24], "Composure" : futwiz_2[25], "Interceptions" : futwiz_2[26], "Heading Accuracy" : futwiz_2[27],
    #"Defense Awareness" : futwiz_2[28], "Stand Tackle" : futwiz_2[29], "Slide Tackle" : futwiz_2[30], "Jumping" : futwiz_2[31], "Stamina" : futwiz_2[32], "Strength" : futwiz_2[33], "Agression" : futwiz_2[34]
#}
#df=pd.DataFrame(data)

#Nettoyage de la dataframe
def clean_data(df):
    df['Value in game']=[df['Value in game'][i].replace(',','') for i in range(0,len(df['Value in game']))]
    df['Value IRL (mio)']=[df['Value IRL (mio)'][i].replace(" mio. €",'').replace(",","").replace('-','-1').replace(' K €',"000") for i in range(0,len(df['Value IRL (mio)']))] #on désire transformer les données string en int pour pouvoir les manipuler après, on remplace donc les charactères pour appliquer la modification de type
    df['Height (cm)']=[df['Height (cm)'][i].replace('cm','') for i in range(0,len(df['Height (cm)']))]
    df = df.astype({"Age":"int64","Weight (kg)":"int64", "Height (cm)":"int64", "Value IRL (mio)" : "int64", "Value in game":"int64", "Weak Foot (/5)":"int64", "Skills (/5)":"int64", "General Note":"int64", "General Pace":"int64","General Shooting":"int64","General Passing":"int64",
    "General Dribbling":"int64", "General Defending":"int64","General Physical":"int64","Acceleration":"int64","Sprint Speed":"int64","Positioning":"int64","Finishing":"int64","Shot Power":"int64","Long Shots":"int64",
    "Volleys":"int64","Penalties":"int64","Vision":"int64","Crossing":"int64","Free Kick Accuracy":"int64","Short Pass":"int64","Long Pass":"int64","Curve":"int64","Agility":"int64","Balance":"int64","Reactions":"int64",
    "Ball Control":"int64","Dribbling":"int64","Composure":"int64","Interceptions":"int64","Heading Accuracy":"int64","Defense Awareness":"int64","Stand Tackle":"int64","Slide Tackle":"int64","Jumping":"int64",
    "Stamina":"int64","Strength":"int64","Agression":"int64"})
    df['Value IRL (mio)']=df['Value IRL (mio)']*10000 #pour remettre en millions
    if "Jesus Corona" in df['Name']:
        df.loc[df.Name=="Jesus Corona", 'Value IRL (mio)']=800000 # ici le joueur vaut moins de 1 million
    df['Value IRL (mio)']=df['Value IRL (mio)']/1000000 # pour mettre tous les joueurs à l'échelle du millions y compris les joueurs valant en dessous de 1 million
    return df 
#df=clean_data(df)
#Création du fichier Json qui sera utilisé par la suite
#df.to_json("FIFA23.json") 




##################################################################################################################################################################
#UTILISATION DES DONNEES



st.title("""
Projet Data Engineering Anne-Sophia LIM / Yanis PERRIN
""")

st.markdown("""
This application allows you to visualize the caracteristics of the top 500 players of the game FIFA23.
* **Python libraries:** beautifulsoup4, pandas, streamlit, pymongo, requests 
* **Data source:** [futwiz.com](https://www.futwiz.com/en/fifa23/players?page=0&release=raregold) et [transfermarkt.fr](https://www.transfermarkt.fr/)
""")

st.sidebar.header('Filters')
st.sidebar.markdown("""
##### *You can clear all the selected filters by clicking on the cross of each filter. The little cross of each category allows you to clear all the filters already choosen. By default, no filters are selected.*
# """)

df=pd.read_json('FIFA23.json')
client=MongoClient("mongo")
collection=client.fifa23.joueur

df=pd.DataFrame(df)

##################################################################################################################################################################
# PARTIE I : Visualisation des informations principales des joueurs.

#Création des sliders et des différents sélecteurs

all_names=collection.distinct('Name')#Requête qui récupère les uniques noms.
selected_name = st.sidebar.multiselect('Name', all_names)

all_teams=collection.distinct('Team')
selected_team = st.sidebar.multiselect('Team', all_teams)

all_countries=collection.distinct('Country')
selected_country = st.sidebar.multiselect('Country', all_countries)

all_leagues=collection.distinct('League')
selected_league = st.sidebar.multiselect('League', all_leagues)

all_positions=collection.distinct('Position')
selected_position = st.sidebar.multiselect('Position', all_positions)

all_sponsor=collection.distinct('Sponsor')
selected_sponsor = st.sidebar.multiselect('Sponsor', all_sponsor)

all_foot=collection.distinct('Foot')
selected_foot = st.sidebar.multiselect('Foot', all_foot)

all_ages=collection.distinct('Age')
min_age=next(collection.find().sort([("Age",1)]).limit(1)).get('Age')#Requête qui recherche l'age maximal dans la bdd
max_age=next(collection.find().sort([("Age",-1)]).limit(1)).get('Age')#Requête qui recherche l'age minimal dans la bdd
selected_age = st.sidebar.slider('Age',int(min_age),int(max_age),(int(min_age),int(max_age)))

#Petite Précision : si le joueur a une valeur de 0.01 IRL cela veut dire qu'il a pris sa retraite
min_value_irl=next(collection.find().sort([("Value IRL (mio)",1)]).limit(1)).get('Value IRL (mio)')
max_value_irl=next(collection.find().sort([("Value IRL (mio)",-1)]).limit(1)).get('Value IRL (mio)')
selected_value_irl = st.sidebar.slider('Value In Real Life (millions)',float(min_value_irl),float(max_value_irl),(float(min_value_irl),float(max_value_irl)))

min_value_in_game=next(collection.find().sort([("Value in game",1)]).limit(1)).get('Value in game')
max_value_in_game=next(collection.find().sort([("Value in game",-1)]).limit(1)).get('Value in game')
selected_value_in_game = st.sidebar.slider('Value In Game',int(min_value_in_game),int(max_value_in_game),(int(min_value_in_game),int(max_value_in_game)))

min_weight=next(collection.find().sort([("Weight (kg)",1)]).limit(1)).get('Weight (kg)')
max_weight=next(collection.find().sort([("Weight (kg)",-1)]).limit(1)).get('Weight (kg)')
selected_weight = st.sidebar.slider('Weight (kg)',int(min_weight),int(max_weight),(int(min_weight),int(max_weight)))

min_height=next(collection.find().sort([("Height (cm)",1)]).limit(1)).get('Height (cm)')
max_height=next(collection.find().sort([("Height (cm)",-1)]).limit(1)).get('Height (cm)')
selected_height = st.sidebar.slider('Height (cm)',int(min_height),int(max_height),(int(min_height),int(max_height)))

##################################################################################################################################################################

#On crée la fonction add_to_filter_str qui permet de sélectionner les filtres qui ne sont pas vides, elle nous permettra aussi d'afficher
#la datataframe même si aucun filtre n'est sélectionné. La fonction a comme paramètres le tableau des filtres qui seront appliquée,
#column (la catégorie), selected_variable (les filtres sélectionnés) et l'aggregation (ici $in). 
def add_to_filter_str(filter,column,selected_variable, aggregation="$in"): 
    if(len(selected_variable)>0):
            filter.append({column:{aggregation:selected_variable}})

#On crée les paramètres qui seront entrés dans la fonction
filter_couples_str=[("Name", selected_name),("Team", selected_team),("Position",selected_position), ("League", selected_league), ("Country",selected_country), ("Sponsor", selected_sponsor), ("Foot", selected_foot)]
filters_str=[]
for couple in filter_couples_str:
    column=couple[0]
    selected_variable=couple[1]
    add_to_filter_str(filters_str, column, selected_variable)

#Même fonction que précédemment mais ici pour les données numériques et il n'y pas besoin de vérifier si le filtre est vide car il sera toujours
#remplis par deux valeurs (min et max). 
def add_to_filter_int(filter,column,selected_variable, aggregation1="$gte", aggregation2="$lte"): 
    filter.append({column:{aggregation1:selected_variable[0], aggregation2:selected_variable[1]}})

filter_couples_int=[("Age", selected_age),("Value IRL (mio)", selected_value_irl),("Value in game", selected_value_in_game), ("Weight (kg)", selected_weight), ("Height (cm)", selected_height)]
filters_int=[]
for couple in filter_couples_int:
    column=couple[0]
    selected_variable=couple[1]
    add_to_filter_int(filters_int, column, selected_variable)

main_infos_categories=['Name','Age','Weight (kg)','Height (cm)','Country','Team','League','Position','Value IRL (mio)','Value in game','Sponsor','Foot']

#Une fois le filtre calculée on l'applique sur la base de donnée
cur_selected_filter=collection.find({"$and":filters_str+filters_int},{k:1 for k in main_infos_categories} | {"_id":0})
df_selected_filter=pd.DataFrame(list(cur_selected_filter))

st.header("Display player's main informations from selected filter(s)")
if len(df_selected_filter)>0:
    st.dataframe(df_selected_filter) 
else : st.write("No player found")

##################################################################################################################################################################
# PARTIE II : Outils de comparaison des joueurs.
st.header("Compare players general stats with others")

all_players=collection.distinct('Name')
selected_player=st.multiselect('Select Player(s)', all_players)

general_stats_categories=['Name','Value in game','General Note','General Pace','General Shooting','General Passing','General Dribbling','General Defending', 'General Physical','Weak Foot (/5)','Skills (/5)']

#requête sur la base de données mongo, qui retourne les données pour les notes générales de chaque stat en fonction du/des joueur(s) recherché(s)
cur_general_stats = collection.find({"Name":{"$in":selected_player}}, {k:1 for k in general_stats_categories} | {"_id":0})
df_general_stats = pd.DataFrame(list(cur_general_stats)) 
image_player=[]
for document in collection.find({"Name":{"$in":selected_player}}):
    image_player.append(document.get('Image'))

st.image(image_player)

if len(df_general_stats)>0:
    st.dataframe(df_general_stats) 
else : st.write("Please select at least one player...")

#SPIDER CHART
#Création du Spider chart avec Plotly
st.markdown("""
#### Spider Chart
""")
st.markdown("""
*You can click on the player name in the legend to choose which one you want to visualize*
""")
#st.write("* You can click on the player name in the legend to choose which one you want to visualize")
general_stats_categories = ['General Pace', 'General Shooting', 'General Passing','General Dribbling', 'General Defending', 'General Physical']

fig = go.Figure()

#pour chaque joueur on ajoute son spider chart à la figure
for i in range(len(df_general_stats)):
        name=df_general_stats.loc[i]['Name']
        stats = list(df_general_stats.loc[i][general_stats_categories])
        fig.add_trace(go.Scatterpolar(
            r=stats,
            theta=general_stats_categories,
            fill='toself',
            name=name))

fig.update_layout(
    width=700,
    height=700,
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 100]
    )),
)

st.plotly_chart(fig)

#BAR CHART
#Création du Bar Chart avec plotly

st.header("Advanced statistics")
st.markdown("""
#### Bar Chart
""")
advanced_stats_categories=['Name','Acceleration','Sprint Speed','Positioning','Finishing','Shot Power','Long Shots','Volleys','Penalties','Vision','Crossing','Free Kick Accuracy','Short Pass','Long Pass','Curve','Agility',
 'Balance','Reactions','Ball Control','Dribbling','Composure','Interceptions','Heading Accuracy','Defense Awareness','Stand Tackle','Slide Tackle','Jumping',
 'Stamina','Strength','Agression']

#requête sur la base de données mongo, qui retourne les données pour les notes précises de chaque stat en fonction du/des joueur(s) recherché(s)
cur_advanced_stats = collection.find({"Name":{"$in":selected_player}}, {k:1 for k in advanced_stats_categories} | {"_id":0})
df_advanced_stats = pd.DataFrame(list(cur_advanced_stats)) #list vide le cursor de tous les joueurs

fig2 = go.Figure()

#pour chaque joueur on ajoute son bar chart à la figure
for i in range(len(df_advanced_stats)):
    name_advanced_stats=df_advanced_stats.loc[i]['Name']
    stats=list(df_advanced_stats.loc[i][advanced_stats_categories])
    fig2.add_trace(go.Bar(
        x=advanced_stats_categories[1:],#on n'oublie pas de ne pas sélectionner la colonne name
        y=stats[1:],
        name=name_advanced_stats
))
fig2.update_layout(
    width=1100,
    height=800,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Stats',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group',
    bargap=0.50, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig2)

##################################################################################################################################################################
# PARTIE III: Visualisation de statistiques liées aux équipes.

st.header("Team's observations")

#On crée une fonction qui nous permettra de récupérer des observations faites avec des requêtes mongo et de les convertir
#en une dataframe pour pouvoir les regrouper et les afficher.
def det_aggregation(name, aggregation, variable, column_name):
    team=[]
    column=[]
    cur = collection.aggregate([{"$group" : {"_id" : "$Team", name : {aggregation : variable}}}])
    for document in cur:
        team.append(document.get("_id"))
        column.append(document.get(name))
    data={"Team":team, column_name:column}
    df=pd.DataFrame(data)
    return df

total_note=det_aggregation("totalNote", "$sum", "$General Note", "Total Note")
average_age=det_aggregation("averageAgeByTeam", "$avg", "$Age", "Average Age")
number_player=det_aggregation("numberOfPlayer", "$sum", 1, "Number of Player")
best_note=det_aggregation("bestNote", "$max", "$General Note", "Best Note")

merge1=pd.merge(total_note, average_age, on="Team")
merge2=pd.merge(number_player, best_note, on="Team")
mergefinal=pd.merge(merge1, merge2, on="Team")

mergefinal['Average Age']=round(mergefinal['Average Age'],1)
df_rank=mergefinal.sort_values(['Total Note'], ascending=False, ignore_index=True)#sera utilisé pour obtenir le rank de l'équipe

#Création des métrics
selected_team_metric = st.multiselect("Select a team", all_teams)

#Pour chaque équipe sélectionnés on affiche les stats calculés par les requêtes mongo
for team in selected_team_metric:
    cur=collection.find({"Team":team})
    league=next(cur).get("League")
    rank=df_rank[df_rank.Team==team].index.values[0]
    total_points=mergefinal.loc[mergefinal.Team==team]['Total Note'].values[0]
    number_player=mergefinal.loc[mergefinal.Team==team]['Number of Player'].values[0]
    best_note=mergefinal.loc[mergefinal.Team==team]['Best Note'].values[0]
    average_age=mergefinal.loc[mergefinal.Team==team]['Average Age'].values[0]
    cols1 = st.columns(3)
    cols1[0].metric(team, league)
    cols1[1].metric("Total Points", total_points)
    cols1[2].metric("Rank", "Top "+str(rank+1))
    cols2=st.columns(3)
    cols2[0].metric("Number of Player in the top 500", number_player)
    cols2[1].metric("Best Note", best_note)
    cols2[2].metric("Average Age", average_age)
    st.markdown("""***""")