import datetime as dt
now = dt.datetime.now()
now_text = now.strftime("%d/%m %H:%M")

tweets = [
        
    f"[🤖 MAJ {now_text}] Suivi de l'épidémie à travers 7 indicateurs dans les 4 régions métropolitaines où le taux de réanimation chez les + de 60 ans est le plus fort ⤵️",
    "... dans les 4 régions suivantes ⤵️",
    "... et dans les 5 dernières ⤵️",
    "... enfin dans les 5 départements et régions d'outre-mer (l'échelle a été changée, pour prendre en compte les valeurs beaucoup plus élevées) ⤵️",

    "Ces représentations graphiques décrivent comment l'épidémie de Covid-19 a impacté et continue d'impacter la France et ses régions.",
    "Les choix suivants sont les suivants : \n\
1️⃣ La chronologie de l'épidémie est présentée dans son intégralité ; le 1er janvier 2021 (barre verticale) et les trois périodes de confinement (zones grisées) servent de points de repère",
    "2️⃣ La population est divisée en 3 tranches d'âge : - de 30 ans, 30 à 60 ans et + de 60 ans\n\
3️⃣ Les indicateurs sont rapportés à la population de la tranche d'âge considérée, dans le territoire considéré",
    "4️⃣ Pour chaque indicateur, l'échelle des Y (à gauche) est identique dans les différents territoires (sauf indication contraire)\n\
5️⃣ Les territoires sont ordonnés selon un paramètre, ici le taux de réanimation chez + de 60 ans.",

    "Incidence et indicateurs hospitaliers (ici l'échelle est optimisée)\n\
1️⃣ sur l'ensemble de la France ⤵️", 
    "... 2️⃣ en Martinique ⤵️",
    "... 3️⃣ en Guadeloupe ⤵️",
"... 4️⃣ en Provence-Alpes-Côtes d'Azur ⤵️",

	"... 5️⃣ en Occitanie ⤵️",
    "... et en Île-de-France ⤵️",
	"Zoom sur les 4 régions métropolitaines les plus touchées",
    "👉 Le code source @E_Dmz https://github.com/E-Dmz/DisplayDataCovid\n\
👉 Les données @SantePubliqueFr @datagouvfr.",

"Des questions sur le(s) vaccin(s) ? @QuestionVaccin https://twitter.com/QuestionVaccin/status/1424659170717061124",
"#VaccinezVous https://twitter.com/E_Dmz/status/1427596782599557121",
]

media = [

    ["../Output/Type1/régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"],
    ["../Output/Type1/régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"], 
    ["../Output/Type1/régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"],
    ["../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"],
    
    [],
    [],
    [],
    [],

    ["../Output/Type0/France-incidence hebdo.png", "../Output/Type0/France-taux hosp.png", "../Output/Type0/France-taux rea.png", "../Output/Type0/France-taux décès.png"],
    ["../Output/Type0/Martinique-incidence hebdo.png", "../Output/Type0/Martinique-taux hosp.png", "../Output/Type0/Martinique-taux rea.png", "../Output/Type0/Martinique-taux décès.png"],
    ["../Output/Type0/Guadeloupe-incidence hebdo.png", "../Output/Type0/Guadeloupe-taux hosp.png", "../Output/Type0/Guadeloupe-taux rea.png", "../Output/Type0/Guadeloupe-taux décès.png"],
	["../Output/Type0/Provence-Alpes-Côte d'Azur-incidence hebdo.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux hosp.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux rea.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux décès.png"],
    
["../Output/Type0/Occitanie-incidence hebdo.png","../Output/Type0/Occitanie-taux hosp.png","../Output/Type0/Occitanie-taux rea.png","../Output/Type0/Occitanie-taux décès.png"],    
["../Output/Type0/Île-de-France-incidence hebdo.png", "../Output/Type0/Île-de-France-taux hosp.png", "../Output/Type0/Île-de-France-taux rea.png", "../Output/Type0/Île-de-France-taux décès.png"],
["../Output/Type1/zoom régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"],    
[],

[],
[],
]