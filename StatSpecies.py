# Claire Nolan 27Apr2019

# PANDS Project 2019
# AIM: Small module to analyse a data set and output the mean per variable by species
# Data set to be analysed is Fisher's Iris Data Set

# From my research i found code in references https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9. I'm going to start from section 4.
# and https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/
# This is the links for Parts 1 and 2 of the same series https://towardsdatascience.com/python-for-data-science-part-1-759524eb493b ; https://towardsdatascience.com/python-for-data-science-part-2-373d6473fa40 
# i tried it out in ipythons (see attached images) and eventually got it to work to calculate the mean value by species. I was also able to repeat for standard deviation, min and max value.
# The following reference https://towardsdatascience.com/python-for-data-science-part-4-6087cb811a29 is also useful for performing a more in-depth manipulation of the data set
import pandas as pd # imports the Python PANDAs program
import numpy as np # imports the Python Numpy program
import matplotlib.pyplot as plt # imports the Python PANDAs program

df1 = pd.read_csv('DataSetHeader.csv', delimiter=',') #identifies dataset to be analysed and how to format

#1 Generating basic statistics by species

SpMean = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].mean()
# this is the code form reference above which i found worked by practising on ipython first (see screenshots). the output is a table of the mean value of each varaible (ie sepal length and width, petal length and width) by species type
# this code is repeated below for standard deviation, min and max values
print('Mean') 
# Tried the following code but found it skewed the table headers: print('Standard Deviation',SpStd) so decided to add table title separately.
print(SpMean)

# Repeated the same code for the other statistics 

SpStd = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].std()
print('Standard Deviation') 
print(SpStd)

SpMin = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].min()
print('Minimum Values') 
print(SpMin)

SpMax = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].max()
print('Maximum') 
print(SpMax)

# This gives a nice output of the data in tables











