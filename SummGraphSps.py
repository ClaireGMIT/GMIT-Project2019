# Claire Nolan 28Apr2019

# PANDS Project 2019
# Data set to be analysed is Fisher's Iris Data Set
# Basic summary stats program (BasicSummStats.py) and graph program (BasicGraphs.py) joined into one program called "SummaryStatsGraph.py". 

# AIM: To creat scatterplots for the variables data with different colour data points for each species

# References:https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html ; https://matplotlib.org/users/pyplot_tutorial.html

# Data set to be analysed is Fisher's Iris Data Set

# After final review of the stakoverflow website i found this refercnce which i was able to use to give the scatterplots colour coded by species
# https://stackoverflow.com/questions/8202605/matplotlib-scatterplot-colour-as-a-function-of-a-third-variable

import numpy
# Import numpy function

import matplotlib.pyplot as plt
# import Mat lab function

dtype = [('A', 'float'), ('B', 'float'), ('C', 'float'), ('D', 'float'), ('E', '<U32')] # this identifies how the data is to be manipulated
data = numpy.genfromtxt('DataSet.csv', delimiter=',', dtype=dtype) #dtype is a list and dtype=dtype means identify the list in the data as dtype

# Code below identifies the data set
SepLeng = data['A']
SepWid = data['B']
PetLeng = data['C']
PetWid = data['D']
Species = data['E']

# Function to map the colors as a list from the input list of x variables
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l=='versicolor': 
            cols.append('red') # ie if the iris species is versicolor then the data points should be coloured red
        elif l=='setosa':
            cols.append('blue') # ie if the iris species is setosa then the data points should be coloured blue
        elif l=='virginica':
            cols.append('green') # ie if the iris species is virginica then the data points should be coloured green
        else:
            cols.append('gray') # otherwise any other data points should be coloured grey
    return cols

cols=pltcolor(Species)

# 1: Scatterplot
fig = plt.scatter([SepLeng] , [PetLeng]) 
fig = plt.scatter([SepWid] , [PetWid])
# specifies scatterplot graph required

# Code i had developed previously to show the histogram plots - see BasicGraphs.py

plt.figure(1)
plt.subplot(211) 
plt.title('Scatterplot')
plt.ylabel('Petal Length (cm)') # to label the y-axis of the first graph
plt.xlabel('Sepal Length (cm)') # to label the x-axis of the first graph
plt.scatter(SepLeng , PetLeng, c=cols) # scatterplot comparing sepal length to petal length

plt.show() # shows grapical results. If i had time i would add a legend identifying the species by its corresponding data point colour


