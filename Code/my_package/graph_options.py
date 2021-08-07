from math import log10, floor, ceil
from my_package.dicts import regions, regions_metro

ordre_de_grandeur = lambda x: 10**floor(log10(x)) 

def rescale():
    for label in graph_options:
        ymax = graph_options[label]['ymax']
        majloc, minloc = loc_auto(ymax)
        graph_options[label]['majloc'] = majloc
        graph_options[label]['minloc'] = minloc

def delta(deltamin):
    """
    given a minimal delta, calculates the delta of majlocs and minlocs
    deltamin: float
    returns 2 floats
    """
    o = ordre_de_grandeur(deltamin)
    r = deltamin/ordre_de_grandeur(deltamin)
    if r < 2:
        return 2 * o, o
    elif r <5:
        return 5 * o, o
    else:
        return 10 * o, 5* o

def loc_auto(lim_sup, nmajor = 6, nminor = 14):
    """
    given a ymax (lim_sup), calculates the graduations 
    lim_sup: integer or float
    nmajor: integer, max number of major graduations
    nminor: integer, max number of minor graduations
    returns 
    majloc, minloc: lists of floats
    """
    deltamin = lim_sup/nmajor
    dmaj, dmin = delta(deltamin)
    
    majloc = [dmaj * i for i in range(ceil(lim_sup/dmaj))]
    minloc = [dmin * i for i in range(ceil(lim_sup/dmin))]
    if len(minloc) > nminor:
        minloc = majloc

    return majloc, minloc 

def graph_options_auto(indicateurs_dic):
    """
    returns a modified graph_options dictionnary
    indicateurs_dic: dictionary with keys = labels, values = ymax
    """
    graph_options_alt = graph_options.copy()

    for label, ymax in indicateurs_dic.items():
        modified_item  = graph_options_alt[label]
        modified_item['ymax'] = ymax
        locs = loc_auto(ymax)
        modified_item['majloc'] = locs[0]
        modified_item['minloc'] = locs[1]

    return graph_options_alt

def last_value(df, entity = 'Corse', age_class = '60+', label = 'incidence hebdo'):
    d = df[ (df.entity == entity)
                    & (df.three_class == age_class) 
                    & df[label].notna()]
    last_day = d.jour.max()
    lasts = d[ d.jour == last_day][label].values
    last = lasts[0] if lasts else 0.0
    return last

def max_last_value(df, entities = regions, age_class = '60+', label = 'incidence hebdo'):
    return max([last_value(df, entity, age_class, label) for entity in entities])

def max_value(df, entities = regions, age_class = '60+', label = 'incidence hebdo'):
    d = df[ (df.entity.isin(entities))
                    & (df.three_class == age_class) 
                    & df[label].notna()][label]
    return d.max()

def scale_graph_by_age_class_last(df, entities,  *args, factor = 1.5,):
    dic = {
        label:factor * (max_last_value(df, entities, age_class, label)+0.001) for label, age_class in args}

    return graph_options_auto(dic)

def scale_graph_by_age_class_max(df, entities = regions_metro,  *args, factor = 1.1,):
    dic = {
        label:factor * (max_value(df, entities, age_class, label)+0.001) for label, age_class in args}

    return graph_options_auto(dic)

graph_options = {
    'incidence hebdo': {
        'ymax': 1300,#1250,
        'main_color': 'darkturquoise',
        'title': 'Cas positifs par semaine,\npour 100 000 habitants',
        },
    'taux de tests hebdo': {
        'ymax': 21000,
        'main_color': 'gray',
        'title': 'Tests pratiqués par semaine,\npour 100 000 habitants',
        },
    'taux de positifs hebdo': {
        'ymax': 26,
        'main_color': 'olivedrab',
        'title': 'Tests positifs,\npour 100 tests\n(moyenne hebdomadaire)',
        },
    'taux hosp': {
        'ymax': 372,
        'main_color': 'mediumseagreen',
        'title': 'Patients hospitalisés,\npour 100 000 habitants',
        },
    'taux rea': {
        'ymax': 59,#59,
        'main_color': 'darksalmon',
        'title': 'Patients en réanimation,\npour 100 000 habitants',
        },
    'taux décès': {
        'ymax': 50,#59,
        'main_color': 'orchid',
        'title': "Décès à l'hôpital par semaine,\npour 100 000 habitants",
        },
    'taux dose 1': {
       'ymax': 100,
        'main_color': 'silver',
        'title': 'Première injection,\npour 100 habitants',
        },
    'taux complet': {
        'ymax': 100,  
        'main_color': 'gold',
        'title': 'Vaccination complète,\npour 100 habitants',
        },
    }

rescale()