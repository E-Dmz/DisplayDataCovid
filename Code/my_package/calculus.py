# import time
# import datetime as dt
# import os
# import glob
# import json

# import itertools as it
# import numpy as np
import pandas as pd

from my_package.datepaths import retrieve_data
from my_package.dicts import dep_to_reg, reg_name 

### general functions

def groupby_sum(d, columns):
    """ returns a dataframe, grouped according to columns
            other columns are summed
        d: dataframe
        columns: list of str, labels of columns to groupby (example : group by entity and/or age_class)
    """
    dg = (d
          .groupby(columns)
          .agg([sum])
          .reset_index()
         )
    dg.columns = dg.columns.droplevel(level = 1)
    dg = dg.reindex(columns = d.columns) # keep same column order                        
    return dg

def columns_first(d, columns):
    """ returns: dataframe reordered
        d: dataframe
        columns: list of str, labels of columns to put first
    """
    d = d.reindex(columns = columns + [column for column in d.columns if column not in columns])
    return d

def map_rename(d, col_in, col_out, func):
    """ returns: dataframe with a column (col_in) mapped (with func) and renamed (col_out)
        d: dataframe
        col_in mapped: str (label of column)
        col_out: str (new label of column)
        func: function 
    """
    d[col_in] = d[col_in].map(func)
    return d.rename(columns = {col_in: col_out})

#universal input
def df_input(dataset):
    """
    returns din: dataframe
    path_temp: pathway for temporary files
    dataset: str, among ['sp-pos-quot-dep', 'donnees-hospitalieres-classe-age-covid19', 'donnees-hospitalieres-covid19', 'vacsi-a-dep']
    """
    data_fname, path_temp = retrieve_data(dataset)
    print(data_fname)
    df = pd.read_csv(data_fname, sep = ';', parse_dates = ['jour'], dtype = {'dep': str, 'reg': str})
    if 'dep' in df.columns:
        df = df[~df.dep.isin(['00', '20', '750', '970', '975', '977', '978', '98', '99', '947'])].reset_index(drop = True)
    df = df.rename(columns = {
        'dep': 'entity',
        'pop': 'population',
        'reg': 'entity',
        'cl_age90': 'age_class',
        'clage_vacsi': 'age_class',
    })
    return df


#universal tot-3C
def compute_reg_nat(din):
    d_dep = din.copy() 

    d_reg = din.copy()
    d_reg['entity'] = d_reg['entity'].map(lambda dep: dep_to_reg[dep])
    d_reg = groupby_sum(d_reg, columns = ['entity', 'jour', 'age_class'])

    d_nat = din.copy()
    d_nat = groupby_sum(d_nat, columns = ['jour', 'age_class'])
    d_nat['entity'] = 'France'

    d_dep_reg = pd.merge(d_dep, d_reg, how = 'outer')
    d_dep_reg_nat = pd.merge(d_dep_reg, d_nat, how = 'outer')

    return columns_first(d_dep_reg_nat, columns = ['entity', 'age_class', 'jour'])

def compute_nat(din):
    d_reg = din.copy()
    d_reg['entity'] = d_reg['entity'].map(lambda reg_number: reg_name[reg_number])
    d_reg = groupby_sum(d_reg, columns = ['entity', 'jour', 'age_class'])

    d_nat = din.copy()
    d_nat = groupby_sum(d_nat, columns = ['jour', 'age_class'])
    d_nat['entity'] = 'France'

    d_reg_nat = pd.merge(d_reg, d_nat, how = 'outer')

    return columns_first(d_reg_nat, columns = ['entity', 'age_class', 'jour'])

def compute_new_age_classes(d, map_age_classes):
    """map_age_classes is a dictionnary"""
    d ['age_class']= d['age_class'].map(lambda old_age_class: map_age_classes[old_age_class])
    d_new_age_classes = groupby_sum(d, ['entity', 'jour', 'age_class'])
    return columns_first(d_new_age_classes, columns = ['entity', 'age_class', 'jour'])

def add_population_column(df, population_by_entity_and_age_class):
    df['population'] = df.apply(lambda df: population_by_entity_and_age_class[df.entity][df.age_class], axis = 1)
    return columns_first(df, columns = ['entity', 'age_class', 'jour'])


# for the sp_pos dataset

def sp_pos_compute(din):
    """
    d: dataframe with columns 'P', 'T' and 'pop'
    returns: dataframe with extra columns 'P hebdo', 'T hebdo', 'incidence hebdo', 'taux de positifs hebdo', 'taux de tests hebdo'
    """
    d = din.copy()
    d1 = (d
            .groupby(['entity', 'age_class'])
            .rolling(window = 7, on = 'jour')
            .sum()
            .fillna(0)
            .reset_index()
            .set_index('level_2')
            .rename(columns = {
                                    'P': 'P hebdo',
                                    'T': 'T hebdo',
                                })
        )
    d[['P hebdo', 'T hebdo']] = d1[['P hebdo', 'T hebdo']]
    d['incidence hebdo'] = d['P hebdo'] / d.population * 100000
    d['taux de positifs hebdo'] = d['P hebdo'] / d['T hebdo'] * 100
    d['taux de tests hebdo'] = d['T hebdo'] / d.population * 100000
    
    return d

### function for the hospital dataset

def hosp_compute(din):
    d = din.copy()
    d['dc_hebdo'] = d['dc'] - (d.groupby(['entity', 'age_class'])
                            .shift(7)
                            )['dc']
    d['taux hosp'] = d.apply(lambda df: df.hosp/df.population * 100000, 
                            axis = "columns")
    d['taux rea'] = d.apply(lambda  df: df.rea/df.population * 100000, 
                            axis = "columns")
    d['taux décès'] = d.apply(lambda  df: df.dc_hebdo/df.population * 100000, 
                            axis = "columns")
    return d

### functions for the hospital department dataset

def hosp_dep_compute(din):
    
    d1 = din.copy()
    d2 = (d1[d1.sexe == 0]
                .drop(columns =['sexe'])
                .sort_values(['dep', 'jour'])
                .reset_index(drop = True)
                .rename(columns = {'dep': 'entity'})
    )
    d2['dc hebdo'] = d2['dc'] - d2.groupby(['entity']).shift(7)['dc']

    d = d2.copy()
    
    d['taux hosp'] = d.apply(lambda df: df.hosp/df.population * 100000, 
                            axis = "columns")
    d['taux rea'] = d.apply(lambda df: df.rea/df.population * 100000, 
                            axis = "columns")
    d['taux décès'] = d.apply(lambda df: df.dc/df.population * 100000,
                            axis = "columns")
    return d

### functions for the vaccine dataset

def vac_compute(din):
    d = din.copy()
    d['taux dose 1'] = d.apply(lambda df: df.n_cum_dose1 / df.population * 100, 
                         axis = "columns")
    d['taux complet'] = d.apply(lambda df: df.n_cum_complet / df.population * 100, 
                        axis = "columns")
    return d