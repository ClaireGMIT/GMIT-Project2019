


#################
#reference for graphs - https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f

################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('DataSet.csv', delimiter=',')

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]


############
#Try code from https://mode.com/python-tutorial/python-histograms-boxplots-and-distributions/https://mode.com/python-tutorial/python-histograms-boxplots-and-distributions/
bin_values = np.arange(start=0, stop=10, step=0.5)
Sps = data['Species'].isin(['setosa','versicolor' , 'virginica']) # create index of species
SL = data[Sps] # select rows
HistSPSL = SL.groupby('Species')['Sepleng'] # group values by SL, species
HistSPSL.plot(kind='hist', bins=bin_values, figsize=[12,6], alpha=.4, legend=True) # alpha for transparency
    
#################


