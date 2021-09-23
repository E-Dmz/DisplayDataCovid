import datetime as dt
now = dt.datetime.now()
now_text = now.strftime("%d/%m %H:%M")

tweets = [
   
    f"[🤖 MAJ {now_text}] Suivi de l'épidémie à travers 7 indicateurs ⤵️",
    "Zoom sur les 4 régions métropolitaines les plus touchées ⤵️",
    """Incidence et indicateurs hospitaliers :
- ensemble de la France""", 

    "- en Île-de-France",
    "- en Provence-Alpes-Côte d'Azur",
    "- en Occitanie",


    "- en Martinique",
    "- en Guadeloupe",

    """👉 code source @E_Dmz https://github.com/E-Dmz/DisplayDataCovid
👉 données @SantePubliqueFr @datagouvfr.""",
    "Si vous avez des questions sur le(s) vaccin(s), @QuestionVaccin y répondra https://twitter.com/QuestionVaccin/status/1424659170717061124"
    ]

media = [
    ["../Output/Type1/régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png",
    "../Output/Type1/régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png", 
    "../Output/Type1/régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png",
    "../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"],
    
    ["../Output/Type1/zoom régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de plus de 60 ans.png"],
    ["../Output/Type0/France-incidence hebdo.png", "../Output/Type0/France-taux hosp.png", "../Output/Type0/France-taux rea.png", "../Output/Type0/France-taux décès.png"],
    
    ["../Output/Type0/Île-de-France-incidence hebdo.png", "../Output/Type0/Île-de-France-taux hosp.png", "../Output/Type0/Île-de-France-taux rea.png", "../Output/Type0/Île-de-France-taux décès.png"],
    ["../Output/Type0/Provence-Alpes-Côte d'Azur-incidence hebdo.png","../Output/Type0/Provence-Alpes-Côte d'Azur-taux hosp.png","../Output/Type0/Provence-Alpes-Côte d'Azur-taux rea.png","../Output/Type0/Provence-Alpes-Côte d'Azur-taux décès.png"],
    ["../Output/Type0/Occitanie-incidence hebdo.png","../Output/Type0/Occitanie-taux hosp.png","../Output/Type0/Occitanie-taux rea.png","../Output/Type0/Occitanie-taux décès.png"],

    ["../Output/Type0/Martinique-incidence hebdo.png", "../Output/Type0/Martinique-taux hosp.png", "../Output/Type0/Martinique-taux rea.png", "../Output/Type0/Martinique-taux décès.png"],
    ["../Output/Type0/Guadeloupe-incidence hebdo.png", "../Output/Type0/Guadeloupe-taux hosp.png", "../Output/Type0/Guadeloupe-taux rea.png", "../Output/Type0/Guadeloupe-taux décès.png"],
    
   
    [],
    [],

]