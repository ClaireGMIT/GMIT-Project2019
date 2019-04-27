# Claire Nolan 26Apr2019

# PANDS Project 2019
# Small module to analyse a data set and output the mean per variable by species
# Data set to be analysed is Fisher's Iris Data Set

# From my research i found code in reference https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9. I'm going to start from section 4.
# i tried it out in ipythons (see attached images) and eventually got it to work to calculate the mean value by species. I was also able to repeat for standard deviation, min and max value.

import pandas as pd # imports the Python PANDAs program
import numpy as np # imports the Python Numpy program
import matplotlib.pyplot as plt # imports the Python PANDAs program

df1 = pd.read_csv('DataSetHeader.csv', delimiter=',') #identifies dataset to be analysed and how to format

#1 Generating basic statistics by species

SpMean = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].mean()
# this is the code form reference above which i found worked by practising on ipython first (see screenshots). the output is a table of the mean value of each varaible (ie sepal length and width, petal length and width) by species type
# this code is repeated below for standard deviation, min and max values
print('Mean') 
# Tried following code but found it skewed the table headers: print('Standard Deviation',SpStd) so decided to add table title separately.
print(SpMean)

SpStd = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].std()
print('Standard Deviation') 
print(SpStd)

SpMin = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].min()
print('Minimum Values') 
print(SpMin)

SpMax = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].max()
print('Maximum') 
print(SpMax)

#2 Generating graphs by species type







