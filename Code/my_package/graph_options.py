from math import log10, floor, ceil
from my_package.dicts import regions, regions_metro

def rescale(graph_options):
    """modifies graph_options"""
    for label in graph_options:
        ymax = graph_options[label]['ymax']
        majloc, minloc = loc_auto(ymax)
        graph_options[label]['majloc'] = majloc
        graph_options[label]['minloc'] = minloc
    return graph_options

def calculate_deltas(delta):
    """calculates the delta for majlocs and for minlocs
    deltamin: 1 float
    returns: 2 floats"""
    order_of_magnitude = lambda x: 10**floor(log10(x)) 
    o = order_of_magnitude(delta)
    r = delta / o

    if r < 2:
        delta_majloc = 2 * o
        delta_minloc = o
    elif r <5:
        delta_majloc = 5 * o 
        delta_minloc = o
    else:
        delta_majloc = 10 * o
        delta_minloc = 5* o

    return delta_majloc, delta_minloc

def loc_auto(lim_sup, nmajor = 6, nminor = 14):
    """given lim_sup, calculates the graduations (majlocs and minlocs)
    lim_sup: integer or float
    nmajor: integer, max number of major graduations
    nminor: integer, max number of minor graduations 
    majloc, minloc: lists of floats"""
    delta = lim_sup / nmajor
    delta_majloc, delta_minloc = calculate_deltas(delta)
    majlocs = [delta_majloc * i for i in range(ceil(lim_sup/delta_majloc))]
    minlocs = [delta_minloc * i for i in range(ceil(lim_sup/delta_minloc))]
    if len(minlocs) > nminor:
        minlocs = majlocs

    return majlocs, minlocs

def graph_options_auto(indicateurs_dic):
    """
    modifies the graph_options dictionary
    indicateurs_dic: dictionary with keys: labels, values: ymaxs
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
    """returns the last value of an indicator (label), for in a geographical entity for a given age class"""
    d = df[ (df.entity == entity)
                    & (df.three_class == age_class) 
                    & df[label].notna()]
    last_day = d.jour.max()
    lasts = d[ d.jour == last_day][label].values
    last = lasts[0] if lasts else 0.0
    return last

def max_last_value(df, entities = regions, age_classes = ['0-29', '30-59','60+'], label = 'incidence hebdo'):
    """returns the last max value for one indicator (label) for all given entities and age_classes"""
    return max([last_value(df, entity, age_class, label) for entity in entities for age_class in age_classes])

def max_value(df, entities = regions, age_classes = ['0-29', '30-59','60+'], label = 'incidence hebdo'):
    """returns the max value for one indicator (label) for all given entities and age_classes"""
    d = df[ (df.entity.isin(entities))
                    & (df.three_class.isin(age_classes))
                    & df[label].notna()][label]
    return d.max()

def scale_graph_by_age_class_last(df, entities,  *args, factor = 1.5,):
    """returns a modified graph_options dictionary"""
    dic = {
        label:factor * (max_last_value(df, entities, age_classes, label)+0.001) for label, age_classes in args}

    return graph_options_auto(dic)

def scale_graph_by_age_class_max(df, entities = regions_metro,  *args, factor = 1.1,):
    """returns a modified graph_options dictionary"""
    dic = {
        label:factor * (max_value(df, entities, age_class, label)+0.001) for label, age_class in args}

    return graph_options_auto(dic)

graph_options = {
    'incidence hebdo': {
        'ymax': 1300,
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
        'ymax': 59,
        'main_color': 'darksalmon',
        'title': 'Patients en réanimation,\npour 100 000 habitants',
        },
    'taux décès': {
        'ymax': 50,
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

graph_options = rescale(graph_options)