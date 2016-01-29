
# coding: utf-8

# In[2]:

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(line)


# In[4]:

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(len(line))


# In[6]:

import csv

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print(line)


# In[8]:

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print(len(line))


# In[10]:

import pandas as pd

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates_continent-90m.csv')


# In[17]:

input_dataframe[0:10]


# In[ ]:



