import datetime as dt
now = dt.datetime.now()
now_text = now.strftime("%d/%m %H:%M")

texts = [
    f"[🤖 MAJ {now_text}] Incidence hebdo, taux d'hospitalisation, de réanimation et de décès hebdomadaire, par tranche d'âge (0-29, 30-59 et 60+) en France ⤵️\n@SantePubliqueFr @datagouvfr",
    "Suivi de l'épidémie à travers 7 indicateurs dans 4 régions métropolitaines ⤵️\n\
L'échelle des y est la même pour toutes les régions, pour permettre de comparer.",
    "... dans les 4 régions suivantes ⤵️",
    "... et dans les 5 dernières ⤵️",
    
    "Les régions étaient ordonnées par taux de réanimation décroissant **dans la tranche d'âge 30-59**. Les trois régions du pourtour méditerranéen se démarquent fortement des autres.",
    "Or ce sont aussi les 3 régions où le taux d'incidence est reparti le plus vite chez les 0-29 et 30-59. En changeant d'échelle pour mieux voir la tendance actuelle ⤵️",
    "Dans ces régions, c'est chez les + jeunes (0-29 et 30-59) que le virus circule le +,\n\
mais dans *toutes les tranches d'âges* les données hospitalières se dégradent.\n\
Et comme depuis le début, les 60+ sont les plus touchés par les décès.",
    "En Île-de-France et dans les autres régions, ça repart aussi, mais moins fort. Cependant, le rebond de la mortalité dans les Hauts-de-France est très fort.",
    # "Les régions du pourtour méditerranéen sont particulièrement concernées par la recrudescence. Voyons de plus près ce qui se passe en Corse (désolé l'axe des y qui est illisible..., je règlerai ce problème asap)",
    # "... en Occitanie",
    # "... et en PACA",
    # "Pendant ce temps, en Île-de-France, ça repart aussi, mais plus doucement.",
    "Dans les 5 départements et régions d'outre-mer, voici le tableau ⤵️",
    "Le taux de décès hebdomadaire en #Martinique et en #Guyane chez les 60+ approche les 30/100000, ce qui est énorme : le pic de la 1re vague en Île-de-France était à 50/100 000 en avril 2020.",
    "En Martinique, taux d'hospitalisation et de réa sont maintenant à même niveau chez les 30-59 (courbe noire) et les 60+ (courbe de couleur), tandis que chez les 0-29 ans (courbe rouge), ils atteignent un niveau jamais observé auparavant.",
    # "La Martinique inquiète beaucoup. Le taux de décès hebdomadaire  chez les 60+ est à 30/100000, ce qui est énorme ; pour mémoire, le pic de la 1re vague en Île-de-France était à 50/100 000.",
    # "... et la Guyane aussi",
    # "A Mayotte, en revanche, la situation semble stable",
    "Toutes ces figures sont générées automatiquement. Si vous voulez des combinaisons particulières (Grand Est x taux de réa ou département 13 x Taux d'incidence), demandez-le simplement en mentionnant @E_Dmz ou @E_Dmz_bot",
]

medias = [
    ["../Output/Type0/France-incidence hebdo.png", "../Output/Type0/France-taux hosp.png", "../Output/Type0/France-taux rea.png", "../Output/Type0/France-taux décès.png"],
    ["../Output/Type1/régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type1/régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"], 
    ["../Output/Type1/régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    
    [],
    ["../Output/Type1/zoom régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type0/Occitanie-incidence hebdo.png","../Output/Type0/Occitanie-taux hosp.png","../Output/Type0/Occitanie-taux rea.png","../Output/Type0/Occitanie-taux décès.png"],
    ["../Output/Type1/zoom régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png", "../Output/Type1/zoom régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    # ["../Output/Type0/Corse-incidence hebdo.png", "../Output/Type0/Corse-taux hosp.png", "../Output/Type0/Corse-taux rea.png", "../Output/Type0/Corse-taux décès.png"],
    # ["../Output/Type0/Occitanie-incidence hebdo.png", "../Output/Type0/Occitanie-taux hosp.png", "../Output/Type0/Occitanie-taux rea.png", "../Output/Type0/Occitanie-taux décès.png"],
    # ["../Output/Type0/Provence-Alpes-Côte d'Azur-incidence hebdo.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux hosp.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux rea.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux décès.png"],
    # ["../Output/Type0/Île-de-France-incidence hebdo.png", "../Output/Type0/Île-de-France-taux hosp.png", "../Output/Type0/Île-de-France-taux rea.png", "../Output/Type0/Île-de-France-taux décès.png"],
    ["../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    [],
    ["../Output/Type0/Martinique-incidence hebdo.png", "../Output/Type0/Martinique-taux hosp.png", "../Output/Type0/Martinique-taux rea.png", "../Output/Type0/Martinique-taux décès.png"],
    [],
    # ["../Output/Type0/Guyane-incidence hebdo.png", "../Output/Type0/Guyane-taux hosp.png", "../Output/Type0/Guyane-taux rea.png", "../Output/Type0/Guyane-taux décès.png"],
    # ["../Output/Type0/Mayotte-incidence hebdo.png", "../Output/Type0/Mayotte-taux hosp.png", "../Output/Type0/Mayotte-taux rea.png", "../Output/Type0/Mayotte-taux décès.png"],
    # [],
    # [],
    # [],
    # [],
    # [],
    # [],
    # [],
]