# This is a practise file


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.genfromtxt('DataSetHeader.csv', delimiter=',')

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]

#https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9
# to give stat results by species type

df1 = pd.read_csv('DataSetHeader.csv', delimiter=',')

SpMean = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].max()



print(SpMean)


