# Claire Nolan 26Apr2019

# PANDS Project 2019
# Data set to be analysed is Fisher's Iris Data Set
# Basic summary stats program (BasicSummStats.py) and graph program (BasicGraphs.py) joined into one program called "SummaryStatsGraph.py". 
# This is now a program that will take a data set, format data into an array for analysis then perform analysis on the data. 
# The output is summary statistics (mean standard, deiation, min/max), histogram and scatterplots for each variable.


# Below is the basic summary stats program (BasicSummStats.py)

import numpy

data = numpy.genfromtxt('DataSet.csv', delimiter=',')

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]

meanSepLeng = numpy.mean(data[:,0])
StdSepLeng = numpy.std(data[:,0])
MinSepLeng = numpy.min(data[:,0])
MaxSepLeng = numpy.max(data[:,0])

meanSepWid = numpy.mean(data[:,1])
StdSepWid = numpy.std(data[:,1])
MinSepWid = numpy.min(data[:,1])
MaxSepWid = numpy.max(data[:,1])

meanPetLeng = numpy.mean(data[:,2])
StdPetLeng = numpy.std(data[:,2])
MinPetLeng = numpy.min(data[:,2])
MaxPetLeng = numpy.max(data[:,2])

meanPetWid = numpy.mean(data[:,3])
StdPetWid = numpy.std(data[:,3])
MinPetWid = numpy.min(data[:,3])
MaxPetWid = numpy.max(data[:,3])



# Deleted the following code as i prefer the data output in a table format (see below):
#print("Sepal Length Summary Statistics are:" , "mean: ", meanSepLeng, ", Std Dev: ", StdSepLeng, ", min and max:", MinSepLeng , MaxSepLeng)
#print("Sepal Width Summary Statistics are:" , "mean: ", meanSepWid, ", Std Dev: ", StdSepWid, ", min and max:", MinSepWid , MaxSepWid)
#print("Petal Length Summary Statistics are:" , "mean: ", meanPetLeng, ", Std Dev: ", StdPetLeng, ", min and max:", MinPetLeng , MaxPetLeng)
#print("Petal Width Summary Statistics are:" , "mean: ", meanPetWid, ", Std Dev: ", StdPetWid, ", min and max:", MinPetWid , MaxPetWid)

##########################

# A Pandas series is a one-dimensional data structure that can hold any data type such as integers and strings.
# ref:https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# #ref: https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9
# This is a code that is used to give the results as a table using PANDAs.
import pandas as pd

Sepal = pd.DataFrame({'Stat': ['Mean', 'Std Dev' , 'Min' , 'Max'], 'Sepal Length': [meanSepLeng, StdSepLeng, MinSepLeng , MaxSepLeng], 'Sepal Width': [meanSepWid, StdSepWid, MinSepWid, MaxSepWid]})
Petal = pd.DataFrame({'Stat': ['Mean', 'Std Dev' , 'Min' , 'Max'], 'Petal Length': [meanPetLeng, StdPetLeng, MinPetLeng , MaxPetLeng], 'Petal Width': [meanPetWid, StdPetWid, MinPetWid, MaxPetWid]})
#this code creates a table of 3 columns with headers stats, Sepal Length and Sepal width. returns a table of the various stats for the sepal width and length
# Use code below to merge tables above to create a table of all the summary stats for the petal and sepal length and width 


print(pd.merge(Sepal, Petal, on='Stat'))
# It works a treat

#################


# Below is the graph program (BasicGraphs.py) 

import matplotlib.pyplot as plt

data = numpy.genfromtxt('DataSet.csv', delimiter=',')

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]

# 1: Scatterplot
fig = plt.scatter([SepLeng] , [PetLeng]) 
fig = plt.scatter([SepWid] , [PetWid])

plt.figure(1)
plt.subplot(211) 
plt.title('Scatterplot')
plt.ylabel('Petal Length (cm)') # to label the y-axis of the first graph
plt.xlabel('Sepal Length (cm)') # to label the x-axis of the first graph
plt.scatter([SepLeng] , [PetLeng]) # scatterplot comparing sepal length to petal length

plt.subplot(212)
plt.ylabel('Petal Width (cm)') # to label the y-axis of the second graph
plt.xlabel('Sepal Width (cm)') # to label the x-axis of the second graph
plt.scatter([SepWid] , [PetWid])

plt.figure(2) # Figured out this codes opens a second graph window
plt.subplot(211) # Figured out via practise that this relates to position and size in graph window
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.scatter([SepLeng] , [SepWid])

plt.subplot(212)
plt.ylabel('Pet Width (cm)')
plt.xlabel('Petal Length (cm)')
plt.scatter([PetLeng] , [PetWid])

#2 Histograms

plt.figure(3) # opens an third graph window ie window for each graph. could use "221,222,223,224" to have one window with four graphs
plt.title('Histogram - Sepal Length')
plt.xlabel('Sepal Length (cm)') # to label the x-axis of the first graph
plt.hist([SepLeng]) # scatterplot comparing sepal length to petal length

plt.figure(4)
plt.title('Histogram - Sepal Width')
plt.xlabel('Sepal Width (cm)') # to label the x-axis of the first graph
plt.hist([SepWid]) # scatterplot comparing sepal length to petal length

plt.figure(5)
plt.title('Histogram - Petal Length')
plt.xlabel('Petal Length (cm)') # to label the x-axis of the first graph
plt.hist([PetLeng]) # scatterplot comparing sepal length to petal length

plt.figure(6)
plt.title('Histogram - Petal Width')
plt.xlabel('Petal Width (cm)') # to label the x-axis of the first graph
plt.hist([PetWid]) # scatterplot comparing sepal length to petal length
# initial attempt 

plt.figure(7) # to get four histograms on one window
plt.subplot(221) # Figured out via practise that this relates to position and size in graph window
plt.title('Histogram - Sepal Length')
plt.xlabel('Sepal Length (cm)') # to label the x-axis of the first graph
plt.hist([SepLeng]) # scatterplot comparing sepal length to petal length

plt.subplot(222)
plt.title('Histogram - Sepal Width')
plt.xlabel('Sepal Width (cm)') # to label the x-axis of the first graph
plt.hist([SepWid]) # scatterplot comparing sepal length to petal length

plt.subplot(223)
plt.title('Histogram - Petal Length')
plt.xlabel('Petal Length (cm)') # to label the x-axis of the first graph
plt.hist([PetLeng]) # scatterplot comparing sepal length to petal length

plt.subplot(224)
plt.title('Histogram - Petal Width')
plt.xlabel('Petal Width (cm)') # to label the x-axis of the first graph
plt.hist([PetWid]) # scatterplot comparing sepal length to petal length
# initial attempt

plt.show() # shows grapical results. 7 windows open with various graphs

# Merging the two programs worked. This is a nice program for analysing a data set



