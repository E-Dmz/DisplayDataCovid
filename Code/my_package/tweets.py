import datetime as dt
now = dt.datetime.now()
now_text = now.strftime("%d/%m %H:%M")

texts = [
    "Je teste une nouvelle façon de tweeter, plus pratique pour mon auteur, paraît-il !\npoke @E_Dmz, vive #python #twitterapi!",
    f"[🤖 MAJ {now_text}] Voici l'incidence et les données hospitalières en France, par tranche d'âge (0-29, 30-59 et 60+) ⤵️\n@SantePubliqueFr @datagouvfr",
    "Suivi à travers 7 indicateurs pour les 4 régions métropolitaines avec le plus fort taux de réanimation dans la tranche d'âge 30-59 ⤵️",
    "... pour les 4 suivantes ⤵️",
    "... et pour les 5 dernières ⤵️",
    "Les régions du pourtour méditerranéen semblent particulièrement concernées par la recrudescence... Voyons de plus près ce qui se passe en Corse",
    "... en Occitanie",
    "... et en PACA",
    "Pendant ce temps, en Île-de-France (oui, je suis un robot francilien...)",
    "Dans les 5 départements et régions d'outre-mer, voici le tableau ⤵️",
    "La Martinique inquiète beaucoup",
    "... et la Guyane aussi",
    "A Mayotte, la situation semble stable",
    "Pour terminer, quelques lectures intéressantes ⤵️⤵️⤵️ #VaccinezVous https://www.nytimes.com/2021/07/30/us/covid-vaccine-hesitancy-regret.html?smid=tw-share",
    'https://twitter.com/GuillaumeRozier/status/1421104412773294080',
    'https://twitter.com/jburnmurdoch/status/1416805508724502533',
    'https://twitter.com/apresj20/status/1421371813901357058',
    'https://twitter.com/MarieBayle77/status/1408887829825044483',
    'https://twitter.com/CAudigierValett/status/1421151570595622916',
    "C'est tout pour aujourd'hui. @EricBillyFR @CAudigierValett @Le___Doc @PeppeGanga @E_Dmz",
]

medias = [
    ['Screenshot.png'],
    ["../Output/Type0/France-incidence hebdo.png", "../Output/Type0/France-taux hosp.png", "../Output/Type0/France-taux rea.png", "../Output/Type0/France-taux décès.png"],
    ["../Output/Type1/régions métropolitaines 1 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type1/régions métropolitaines 2 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"], 
    ["../Output/Type1/régions métropolitaines 3 sur 3, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type0/Corse-incidence hebdo.png", "../Output/Type0/Corse-taux hosp.png", "../Output/Type0/Corse-taux rea.png", "../Output/Type0/Corse-taux décès.png"],
    ["../Output/Type0/Occitanie-incidence hebdo.png", "../Output/Type0/Occitanie-taux hosp.png", "../Output/Type0/Occitanie-taux rea.png", "../Output/Type0/Occitanie-taux décès.png"],
    ["../Output/Type0/Provence-Alpes-Côte d'Azur-incidence hebdo.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux hosp.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux rea.png", "../Output/Type0/Provence-Alpes-Côte d'Azur-taux décès.png"],
    ["../Output/Type0/Île-de-France-incidence hebdo.png", "../Output/Type0/Île-de-France-taux hosp.png", "../Output/Type0/Île-de-France-taux rea.png", "../Output/Type0/Île-de-France-taux décès.png"],
    ["../Output/Type1/régions d'outre-mer, classées par taux de réanimation décroissant chez les personnes de 30 à 59 ans.png"],
    ["../Output/Type0/Martinique-incidence hebdo.png", "../Output/Type0/Martinique-taux hosp.png", "../Output/Type0/Martinique-taux rea.png", "../Output/Type0/Martinique-taux décès.png"],
    ["../Output/Type0/Guyane-incidence hebdo.png", "../Output/Type0/Guyane-taux hosp.png", "../Output/Type0/Guyane-taux rea.png", "../Output/Type0/Guyane-taux décès.png"],
    ["../Output/Type0/Mayotte-incidence hebdo.png", "../Output/Type0/Mayotte-taux hosp.png", "../Output/Type0/Mayotte-taux rea.png", "../Output/Type0/Mayotte-taux décès.png"],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]