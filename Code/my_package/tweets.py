import datetime as dt
now = dt.datetime.now()
now_text = now.strftime("%d/%m %H:%M")

tweets = [
    # f"[🤖 MAJ {now_text}] Incidence hebdo, taux d'hospitalisation, de réanimation et de décès hebdomadaire, par tranche d'âge (0-29, 30-59 et 60+) en France (échelle adaptée)⤵️\n@SantePubliqueFr @datagouvfr",
#     "Avertissement : L'objectif de ces représentations est de montrer graphiquement comment le virus SARS-CoV-2 et la maladie Covid-19 qu'il provoque ont frappé la France et ses régions.",
#     "Pour cela, des choix ont été faits : \n\
# 1️⃣ La chronologie de l'épidémie est présentée dans son intégralité ; le 1er janvier (barre verticale) et les périodes de confinement (zones grisées) sont indiquées comme points de repère",
#     "2️⃣ La population est divisée en 3 tranches dâge faciles à se représenter : - de 30 ans, 30 à 60 ans et + de 60 ans\n\
# 3️⃣ Les indicateurs représentés sont rapportés à la population de la tranche d'âge considérée, dans le territoire considéré",

#     "4️⃣ Pour chaque indicateur, l'échelle des Y (à gauche), est identique dans les différents territoires (sauf indication contraire)\n\
# 5️⃣ Les territoires sont ordonnés selon un paramètre, comme le taux de réanimation chez les 60+, par exemple",
#     "Chaque choix a ses défauts mais aucune visualisation n'est parfaite.\n\
# L'objectif est d'offrir une image simple à lire de l'impact de cette crise interminable, complémentaire des approches utilisées ailleurs.",
#     "Ce fil est tweeté grâce à un script (https://github.com/E-Dmz/DisplayDataCovid)\n\
# Les calculs se font à partir des MAJ les plus récentes de @SantePubliqueFr @datagouvfr\n\
# C'est un projet amateur (@E_Dmz) et un exercice de code.",
#     "La plupart du temps je reste neutre et me concentre à représenter les chiffres les interpréter.\n\
# Pour être transparent sur mes opinions : les vaccins sont une chance inouïe. La situation serait catastrophique sans leur déploiement massif #VaccinezVous",    
    
    f"[🤖 MAJ {now_text}] Suivi de l'épidémie à travers 7 indicateurs dans 4 régions métropolitaines ⤵️",
    "... dans les 4 régions suivantes ⤵️",
    "... et dans les 5 dernières ⤵️",
    "... enfin dans les 5 départements et régions d'outre-mer ⤵️",

    "Remarques : ces représentations graphiques décrivent l'impact de la maladie Covid-19 en France et dans ses régions.",
    "Les choix suivants ont été faits : \n\
1️⃣ La chronologie de l'épidémie est présentée dans son intégralité ; le 1er janvier 2021 (barre verticale) et les trois périodes de confinement (zones grisées) servent de points de repère",
    "2️⃣ La population est divisée en 3 tranches d'âge : - de 30 ans, 30 à 60 ans et + de 60 ans\n\
3️⃣ Les indicateurs représentés sont rapportés à la population de la tranche d'âge considérée, dans le territoire considéré",
    "4️⃣ Pour chaque indicateur, l'échelle des Y (à gauche) est identique dans les différents territoires (sauf indication contraire)\n\
5️⃣ Les territoires sont ordonnés selon un paramètre, ici le taux de réanimation chez les 30-59.",

#     "Chaque choix a ses défauts mais aucune visualisation n'est parfaite.\n\
# L'objectif est d'offrir une image simple à lire de l'impact de cette crise interminable, complémentaire des approches utilisées ailleurs.",
#     "Ce fil est tweeté grâce à un script (https://github.com/E-Dmz/DisplayDataCovid)\n\
# Les calculs se font à partir des MAJ les plus récentes de @SantePubliqueFr @datagouvfr\n\
# C'est un projet amateur (@E_Dmz) et un exercice de code.",
#     "La plupart du temps je reste neutre et me concentre à représenter les chiffres les interpréter.\n\
# Pour être transparent sur mes opinions : les vaccins sont une chance inouïe. La situation serait catastrophique sans leur déploiement massif #VaccinezVous",

#     "Les régions étaient ordonnées par taux de réanimation décroissant **dans la tranche d'âge 30-59**. Les trois régions du pourtour méditerranéen se démarquent fortement des autres.",
#     "Or ce sont aussi les 3 régions où le taux d'incidence est reparti le plus vite chez les 0-29 et 30-59. En changeant d'échelle pour mieux voir la tendance actuelle ⤵️",
#     "Dans ces régions, c'est chez les + jeunes (0-29 et 30-59) que le virus circule le +,\n\
# mais dans *toutes les tranches d'âges* les données hospitalières se dégradent.\n\
# Et comme depuis le début, les 60+ sont les plus touchés par les décès.",
#     "En Île-de-France et dans les autres régions, ça repart aussi, mais moins fort. Cependant, le rebond de la mortalité dans les Hauts-de-France est très fort.",
    # "Les régions du pourtour méditerranéen sont particulièrement concernées par la recrudescence. Voyons de plus près ce qui se passe en Corse (désolé l'axe des y qui est illisible..., je règlerai ce problème asap)",
    # "... en Occitanie",
    # "... et en PACA",
    # "Pendant ce temps, en Île-de-France, ça repart aussi, mais plus doucement.",
    # "Dans les 5 départements et régions d'outre-mer, voici le tableau ⤵️",
    # "Le taux de décès hebdomadaire en #Martinique et en #Guyane chez les 60+ approche les 30/100000, ce qui est énorme : le pic de la 1re vague en Île-de-France était à 50/100 000 en avril 2020.",
    # "En Martinique, taux d'hospitalisation et de réa sont maintenant à même niveau chez les 30-59 (courbe noire) et les 60+ (courbe de couleur), tandis que chez les 0-29 ans (courbe rouge), ils atteignent un niveau jamais observé auparavant.",
    # # "La Martinique inquiète beaucoup. Le taux de décès hebdomadaire  chez les 60+ est à 30/100000, ce qui est énorme ; pour mémoire, le pic de la 1re vague en Île-de-France était à 50/100 000.",
    # "... et la Guyane aussi",
    # "A Mayotte, en revanche, la situation semble stable",
    ]

media = [
    # ["../Output/Type0/France-incidence hebdo.png", "../Output/Type0/France-taux hosp.png", "../Output/Type0/France-taux rea.png", "../Output/Type0/France-taux décès.png"],
    # [],
    # [],
    # [],

    # [],
    # [],
    # [],
    # [],

    ["../Output/Type1/régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type1/régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"], 
    ["../Output/Type1/régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    
    [],
    [],
    [],
    [],

#     ["../Output/Type1/zoom régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
#     ["../Output/Type0/Occitanie-incidence hebdo.png","../Output/Type0/Occitanie-taux hosp.png","../Output/Type0/Occitanie-taux rea.png","../Output/Type0/Occitanie-taux décès.png"],
#     ["../Output/Type1/zoom régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png", "../Output/Type1/zoom régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
#     # ["../Output/Type0/Corse-incidence hebdo.png", "../Output/Type0/Corse-taux hosp.png", "../Output/Type0/Corse-taux rea.png", "../Output/Type0/Corse-taux décès.png"],
#     # ["../Output/Type0/Occitanie-incidence hebdo.png", "../Output/Type0/Occitanie-taux hosp.png", "../Output/Type0/Occitanie-taux rea.png", "../Output/Type0/Occitanie-taux décès.png"],
#     # ["../Output/Type0/Provence-Alpes-Côte d'Azur-incidence hebdo.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux hosp.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux rea.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux décès.png"],
#     # ["../Output/Type0/Île-de-France-incidence hebdo.png", "../Output/Type0/Île-de-France-taux hosp.png", "../Output/Type0/Île-de-France-taux rea.png", "../Output/Type0/Île-de-France-taux décès.png"],
#     ["../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
#     [],
#     ["../Output/Type0/Martinique-incidence hebdo.png", "../Output/Type0/Martinique-taux hosp.png", "../Output/Type0/Martinique-taux rea.png", "../Output/Type0/Martinique-taux décès.png"],
#     # ["../Output/Type0/Guyane-incidence hebdo.png", "../Output/Type0/Guyane-taux hosp.png", "../Output/Type0/Guyane-taux rea.png", "../Output/Type0/Guyane-taux décès.png"],
#     # ["../Output/Type0/Mayotte-incidence hebdo.png", "../Output/Type0/Mayotte-taux hosp.png", "../Output/Type0/Mayotte-taux rea.png", "../Output/Type0/Mayotte-taux décès.png"],
#     # [],
#     # [],
#     # [],
#     # [],
#     # [],
#     # [],
#     # [],
]