#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from time import time
import numpy as np
import re
import requests

import datetime as dt
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
os.getcwd()

import my_package.graph_functions as gf
from my_package.graph_options import graph_options, graph_options_alt_1, graph_options_alt_2, graph_options_alt_3, graph_options_alt_4
import my_package.dicts as dc
import my_package.datepaths as dp
import my_package.calculus as cc

from keys import keys
import twitter


# # Download raw data

# In[5]:


os.chdir('/home/edmz/DisplayDataCovid/Code')


# In[6]:


tic = time()
address = 'https://www.data.gouv.fr/api/1/datasets/'
datasets = ['donnees-hospitalieres-relatives-a-lepidemie-de-covid-19',
            'donnees-relatives-aux-resultats-des-tests-virologiques-covid-19',
            'donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1',
           ]
pattern = re.compile('sp-pos-quot-dep*|vacsi-a-dep*|donnees-hospitalieres-covid19*|donnees-hospitalieres-classe-age-covid19*')

for dataset in datasets:
    response = requests.get(address + dataset)
    for resource in response.json()['resources']:
        if (pattern.match(resource['title'])) and (resource['title'] not in os.listdir('../Data/')):
            r = requests.get(resource['url'], allow_redirects=True)
            with open('../Data/' + resource['title'], 'wb') as file:
                file.write(r.content)
            print(resource['url'])
            
toc = time()
time_download = -tic + toc
time_download


# # Calcul

# In[7]:


tic = time()


# In[3]:


# Données relatives aux résultats des tests virologiques
d_tests_1, path_temp = cc.sp_input()
d_tests_2 = cc.sp_tot_3C(d_tests_1)
d_tests_3 = cc.sp_compute(d_tests_2)

# dout = d_tests_3
# fname = path_temp + '-tot-3C-compute.csv'
# dout.to_csv(fname, sep = ';', index = False)
# print(fname)


# In[4]:


# Données hospitalières
d_hosp_1, path_temp = cc.hosp_input()
d_hosp_2 = cc.hosp_3C(d_hosp_1, keepDROM = True)
d_hosp_3 = cc.hosp_compute(d_hosp_2)

# dout = d_hosp_3
# fname = path_temp + '-3C-compute.csv'
# dout.to_csv(fname, sep = ';', index = False)
# print(fname)


# In[5]:


d_hosp_1, path_temp = cc.hosp_input()
d_hosp_2 = cc.hosp_3C(d_hosp_1, True)
d_hosp_3_DROM = cc.hosp_compute(d_hosp_2)

# dout = d_hosp_3
# fname = path_temp + '-3C-compute-DROM.csv'
# dout.to_csv(fname, sep = ';', index = False)
# print(fname)


# In[6]:


# Données hospitalières départementales (pas de répartition par classe d'âge)
d_hosp_dep_1, path_temp = cc.hosp_dep_input()
d_hosp_dep_2 = cc.hosp_dep_compute(d_hosp_dep_1)

# dout = d_hosp_dep_2
# fname = path_temp + '-compute.csv'
# dout.to_csv(fname, sep = ';', index = False)
# print(fname)


# In[7]:


# Données relatives aux personnes vaccinées (VACSI) 
d_vac_1, path_temp = cc.vac_input()
d_vac_1 = d_vac_1[(d_vac_1.dep != '20') & (d_vac_1.dep != '98') & (d_vac_1.dep != '947') & (d_vac_1.dep != '99')& (d_vac_1.dep != '00')]
d_vac_2 = cc.vac_tot_3C(d_vac_1)
d_vac_3 = cc.vac_compute(d_vac_2)

# dout = d_vac_3
# fname = path_temp + '-tot-3C-compute.csv'
# dout.to_csv(fname, sep = ';', index = False)
# print(fname)


# In[8]:


toc = time()
time_calculus = -tic+toc


# # Tracé des figures

# In[9]:


tic = time()


# In[10]:


# fname = dp.retrieve_temp('sp-pos-quot-dep', 'tot-3C-compute')
# dtes = pd.read_csv(fname, sep = ';', 
#                 parse_dates = ['jour'],
#                 dtype = {'entity': str},
#                )
dtes = d_tests_3

# fname = dp.retrieve_temp('vacsi-a-dep', 'tot-3C-compute')
# dvac = pd.read_csv(fname, sep = ';', 
#                 parse_dates = ['jour'],
#                 dtype = {'entity': str},
#                )
dvac = d_vac_3

# fname = dp.retrieve_temp('donnees-hospitalieres-classe-age-covid19', '3C-compute')
# dhos = pd.read_csv(fname, sep = ';', 
#                 parse_dates = ['jour'],
#                 dtype = {'entity': str},
#                )
dhos = d_hosp_3

# fname = dp.retrieve_temp('donnees-hospitalieres-covid19', 'compute')
# dhosdep = pd.read_csv(fname, sep = ';', 
#                 parse_dates = ['jour'],
#                 dtype = {'entity': str},
#                )
dhosdep = d_hosp_dep_2
dhosdep['three_class'] = 'whole'

d = pd.merge(dhos, dhosdep, how = 'outer')
d = pd.merge(d, dvac, how = 'outer')
d = pd.merge(d, dtes, how = 'outer')
d = d.sort_values(['entity', 'three_class', 'jour'])


# In[11]:


d.sample(5)


# In[12]:


regions = dc.regions
regions_metro = dc.regions_metro
regions_outre_mer = dc.regions_outre_mer


# In[13]:


plt.rcParams["figure.facecolor"] = (1,1,1,1)


# ## Figures Type 1

# In[44]:


# jour = d[d['taux rea'].notna()].jour.max()
# regions_ordered = (d[(d.jour == jour) 
#                     & (d.entity.isin(regions))
#                     & (d.three_class == '60+')]
#                    .groupby('entity')['taux rea']
#                    .mean()
#                    .sort_values(ascending = False)
#                    .index
#                    .tolist())
# regions_ordered_metro = (d[(d.jour == jour) 
#                     & (d.entity.isin(regions_metro))
#                     & (d.three_class == '60+')]
#                    .groupby('entity')['taux rea']
#                    .mean()
#                    .sort_values(ascending = False)
#                    .index
#                    .tolist())
# regions_ordered_outre_mer = (d[(d.jour == jour) 
#                     & (d.entity.isin(regions_outre_mer))
#                     & (d.three_class == '60+')]
#                    .groupby('entity')['taux rea']
#                    .mean()
#                    .sort_values(ascending = False)
#                    .index
#                    .tolist())
jour = d[d['incidence hebdo'].notna()].jour.max()
regions_ordered = (d[(d.jour == jour) 
                    & (d.entity.isin(regions))
                    & (d.three_class == '0-29')]
                   .groupby('entity')['incidence hebdo']
                   .mean()
                   .sort_values(ascending = False)
                   .index
                   .tolist())
regions_ordered_metro = (d[(d.jour == jour) 
                    & (d.entity.isin(regions_metro))
                    & (d.three_class == '0-29')]
                   .groupby('entity')['incidence hebdo']
                   .mean()
                   .sort_values(ascending = False)
                   .index
                   .tolist())
regions_ordered_outre_mer = (d[(d.jour == jour) 
                    & (d.entity.isin(regions_outre_mer))
                    & (d.three_class == '0-29')]
                   .groupby('entity')['incidence hebdo']
                   .mean()
                   .sort_values(ascending = False)
                   .index
                   .tolist())
# regions_ordered = (d[(d.entity.isin(regions)) 
#                      & (d.three_class == 'whole')]
#                    .groupby('entity')['taux décès']
#                    .sum()
#                    .sort_values(ascending = False)
#                    .index.tolist())
gf.fig_type1(d, regions_ordered_metro[:4], 'régions métropolitaines 1 sur 3')
gf.fig_type1(d, regions_ordered_metro[4:8], 'régions métropolitaines 2 sur 3')
gf.fig_type1(d, regions_ordered_metro[8:], 'régions métropolitaines 3 sur 3')
# gf.fig_type1(d, regions_ordered_metro, 'toutes régions métropolitaines')

# gf.fig_type1(d, regions_ordered[:5], 'régions 1 sur 3')
# gf.fig_type1(d, regions_ordered[5:10], 'régions 2 sur 3')
# gf.fig_type1(d, regions_ordered[10:], 'régions 3 sur 3')
# gf.fig_type1(d, regions_ordered, 'toutes régions')

gf.fig_type1(d, regions_ordered_metro[:4], 'zoom régions métropolitaines 1 sur 3', graph_options = graph_options_alt_4)
gf.fig_type1(d, regions_ordered_metro[4:8], 'zoom régions métropolitaines 2 sur 3', graph_options = graph_options_alt_4)
gf.fig_type1(d, regions_ordered_metro[8:], 'zoom régions métropolitaines 3 sur 3', graph_options = graph_options_alt_4)
# gf.fig_type1(d, regions_ordered_metro, 'zoom toutes régions métropolitaines', graph_options = graph_options_alt_1)

gf.fig_type1(d, regions_ordered_outre_mer, 'régions d\'Outre-mer')
gf.fig_type1(d, regions_ordered_outre_mer, 'zoom régions d\'Outre-mer', graph_options = graph_options_alt_2)

# gf.fig_type1(d, regions_ordered_outre_mer, 'régions d\'Outre-mer (Mayotte)', graph_options = graph_options_alt_3)


# # Figures Type 0

# ## France

# In[23]:


gf.simple_figure(d, 'France', 'taux hosp', graph_options = graph_options_alt_4)
gf.simple_figure(d, 'France', 'taux décès', graph_options = graph_options_alt_4)
gf.simple_figure(d, 'France', 'taux rea', graph_options = graph_options_alt_4)
gf.simple_figure(d, 'France', 'incidence hebdo', graph_options = graph_options_alt_4)


# ## Île-de-France

# In[ ]:


gf.simple_figure(d, 'Île-de-France', 'taux hosp', graph_options = graph_options_alt_4)
gf.simple_figure(d, 'Île-de-France', 'taux décès', graph_options = graph_options_alt_4)
gf.simple_figure(d, 'Île-de-France', 'taux rea', graph_options = graph_options_alt_4)
gf.simple_figure(d, 'Île-de-France', 'incidence hebdo', graph_options = graph_options_alt_4)


# ## Paris et petite couronne

# In[17]:


gf.simple_figure(d, '75', 'incidence hebdo', graph_options = graph_options_alt_4)
gf.simple_figure(d, '93', 'incidence hebdo', graph_options = graph_options_alt_4)
gf.simple_figure(d, '92', 'incidence hebdo', graph_options = graph_options_alt_4)
gf.simple_figure(d, '94', 'incidence hebdo', graph_options = graph_options_alt_4)


# ## Grande couronne

# In[18]:


gf.simple_figure(d, '91', 'incidence hebdo', graph_options = graph_options_alt_4)
gf.simple_figure(d, '95', 'incidence hebdo', graph_options = graph_options_alt_4)
gf.simple_figure(d, '77', 'incidence hebdo', graph_options = graph_options_alt_4)
gf.simple_figure(d, '78', 'incidence hebdo', graph_options = graph_options_alt_4)


# ## Martinique et Guyane

# In[20]:


gf.simple_figure(d, 'Martinique', 'incidence hebdo', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Martinique', 'taux rea', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Martinique', 'taux dose 1', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Martinique', 'taux complet', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Guyane', 'incidence hebdo', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Guyane', 'taux rea', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Guyane', 'taux dose 1', graph_options = graph_options_alt_2)
gf.simple_figure(d, 'Guyane', 'taux complet', graph_options = graph_options_alt_2)
toc = time()
time_graph = -tic + toc


# ## Corse

# In[16]:


gf.simple_figure(d, 'Corse', 'incidence hebdo')
gf.simple_figure(d, 'Corse', 'taux dose 1')
gf.simple_figure(d, 'Corse', 'taux hosp')
gf.simple_figure(d, 'Corse', 'taux complet')
gf.simple_figure(d, 'Corse', 'taux rea')


# # Tweet

# In[24]:


tic = time()
now = dt.datetime.now()
now_text = now.strftime("%d/%m %H:%M")
api = twitter.Api(**keys)
num_tweets = 9

#Tweet 1
path_to_type0 = '/home/edmz/DisplayDataCovid/Output/Type0/'
figures = ['Île-de-France-incidence.png',
'Île-de-France-hosp.png',
'Île-de-France-rea.png',
'Île-de-France-deces.png']
status = api.PostUpdate(f'[🤖 MAJ {now_text}]\nIncidence et données hospitalières en Île-de-France ⤵️\n@SantePubliqueFr @datagouvfr\n1/{num_tweets}', 
                        media = [path_to_type0 + figure for figure in figures],
                                 )
status_0 = status

#Tweet 2
figures = ['France-incidence.png',
'France-hosp.png',
'France-rea.png',
'France-deces.png']
status = api.PostUpdate(f'Incidence et données hospitalières en France ⤵️\n🤖 2/{num_tweets}', 
                        media = [path_to_type0 + figure for figure in figures],
                       in_reply_to_status_id = status.id,
                                 )
#Tweet 3
figures = ['75-incidence.png',
'92-incidence.png',
'93-incidence.png',
'94-incidence.png']
status = api.PostUpdate(f'Incidence à Paris et dans les 3 départements de petite couronne ⤵️\n🤖 3/{num_tweets}', 
                        media = [path_to_type0 + figure for figure in figures],
                       in_reply_to_status_id = status.id,
                                 )

#Tweet 4
figures = ['91-incidence.png',
'95-incidence.png',
'77-incidence.png',
'78-incidence.png']
status = api.PostUpdate(f'Incidence dans les 4 départements de grande couronne ⤵️\n🤖 4/{num_tweets}', 
                        media = [path_to_type0 + figure for figure in figures],
                       in_reply_to_status_id = status.id,
                                 )
#Tweet 5
path_to_type1 = '/home/edmz/DisplayDataCovid/Output/Type1/'
'France-hosp.png'
figures = ['régions métropolitaines 1 sur 3.png',
'régions métropolitaines 2 sur 3.png',
'régions métropolitaines 3 sur 3.png',
"régions d'Outre-mer.png"]
status = api.PostUpdate(f'Comparaison de 7️⃣ indicateurs,\npour 3️⃣ classes d\'âge (0-29, 30-59 et 60+), région par région ⤵️\n(attention : échelles différentes en métropole et dans les outre-mer)\n@SantePubliqueFr @datagouvfr\n🤖 5/{num_tweets}', 
                        media = [path_to_type1 + figure for figure in figures],
                       in_reply_to_status_id = status.id,
                                 )
#Tweet 6
figures = ['zoom régions métropolitaines 1 sur 3.png',
'zoom régions métropolitaines 2 sur 3.png',
'zoom régions métropolitaines 3 sur 3.png',
"zoom régions d'Outre-mer.png"]
status = api.PostUpdate(f'Voici les mêmes figures, en zoomant ⤵️\n(attention : échelles différentes en métropole et dans les outre-mer)\n🤖 6/{num_tweets}', 
                        media = [path_to_type1 + figure for figure in figures],
                       in_reply_to_status_id = status.id)

#Tweet 7
path_to_type0 = '/home/edmz/DisplayDataCovid/Output/Type0/'
figures = ['Guyane-incidence.png',
'Guyane-rea.png',
'Martinique-incidence.png',
'Martinique-rea.png']
status = api.PostUpdate(f'En Martinique et en Guyane les dynamiques sont complètement différentes ⤵️\n🤖7/{num_tweets}',
                        media = [path_to_type0 + figure for figure in figures],
                       in_reply_to_status_id = status.id)
#Tweet 8
figures = ['Guyane-dose1.png',
'Guyane-vaccin complet.png',
'Martinique-dose1.png',
'Martinique-vaccin complet.png']
status = api.PostUpdate(f'Et la vaccination avance beaucoup moins vite qu\'en métropole ⤵️ \n🤖8/{num_tweets}',
                        media = [path_to_type0 + figure for figure in figures],
                       in_reply_to_status_id = status.id)

#Tweet 9
toc = time()
time_publish = -tic + toc

status = api.PostUpdate(f'🤖 Pour faire cette MAJ, il m\'a fallu : \n{time_download:.1f} s pour télécharger, \n{time_calculus:.1f} s pour calculer,\n{time_graph:.1f} s pour tracer,\net {time_publish:.1f} s pour publier\n9/{num_tweets}',
                       in_reply_to_status_id = status.id)

status = api.PostRetweet(status_0.id)


# # Autres graphes

# In[ ]:



# gf.simple_figure(d, 'Grand Est', 'taux décès')
# gf.simple_figure(d, 'Corse', 'taux complet')
# gf.simple_figure(d, 'Nouvelle-Aquitaine', 'taux rea')
# gf.simple_figure(d, 'Hauts-de-France', 'taux de tests hebdo')


# In[22]:


# gf.simple_figure(d, 'France', 'taux hosp')
# gf.simple_figure(d, 'France', 'taux rea')
# gf.simple_figure(d, 'France', 'taux décès')


# In[23]:


# gf.simple_figure(d, 'Mayotte', 'incidence hebdo')
# gf.simple_figure(d, 'Mayotte', 'taux rea')
# gf.simple_figure(d, '976', 'incidence hebdo')


# In[17]:


# gf.simple_figure(d, 'Guyane', 'taux hosp')
# gf.simple_figure(d, 'Guyane', 'taux rea')
# gf.simple_figure(d, 'Guyane', 'taux décès')
# gf.simple_figure(d, '973', 'taux dose 1')
# gf.simple_figure(d, '973', 'taux complet')


# In[19]:


# gf.simple_figure(d, '973', 'incidence hebdo')
# gf.simple_figure(d, '93', 'incidence hebdo')
# gf.simple_figure(d, '971', 'incidence hebdo')

# gf.simple_figure(d, '971', 'incidence hebdo')


# In[ ]:


# gf.simple_figure(d, 'France', 'incidence hebdo')
# gf.simple_figure(d, 'Île-de-France', 'incidence hebdo')
# gf.simple_figure(d, '75', 'incidence hebdo')

