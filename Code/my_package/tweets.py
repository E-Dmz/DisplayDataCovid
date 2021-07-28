texts = [
    'Incidence et données hospitalières en Île-de-France ⤵️\n@SantePubliqueFr @datagouvfr',
    'Incidence et données hospitalières en France ⤵️',
    'Incidence à Paris et dans les 3 départements de petite couronne ⤵️',
    'Incidence dans les 4 départements de grande couronne ⤵️',
    'Voici les mêmes figures, en zoomant ⤵️\n(attention : échelles différentes en métropole et dans les outre-mer)',
    'En Martinique et en Guyane les dynamiques sont complètement différentes ⤵️',
    'Et la vaccination avance beaucoup moins vite qu\'en métropole ⤵️'

]

path_to_type0 = '../Output/Type0/'
path_to_type1 = '../Output/Type/'

#path_to_type0 = '/home/edmz/DisplayDataCovid/Output/Type0/'
#path_to_type1 = '/home/edmz/DisplayDataCovid/Output/Type1/'

figures = [
    [
        path_to_type0 + figure for figure in ['Île-de-France-incidence.png',
        'Île-de-France-hosp.png',
        'Île-de-France-rea.png',
        'Île-de-France-deces.png',]
    ],
    [

    ]
]