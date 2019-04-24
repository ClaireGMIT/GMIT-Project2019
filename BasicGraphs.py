# Claire Nolan 24April2019

# PANDS Project 2019
# Code to statistically analyse a data set and output graphs
# Data set to be analysed is Fisher's Iris Data Set
# The Iris dataset was published and discussed in RObert Fishers 1936 paper "The use of multiple measurements in taxonomic problem". The data was collected to quantify the physical variation of Iris flowers of three related species. 
# The data set consists of 50 samples from three species of iris (Iris setosa, Iris virginica, Iris versicolor). 
# The four features measured were the length and width of the sepals and petals in centimetres. 
# The combination of these four features can be used to identify each particular species


# Used code from smaller, simple basic statistical modules as well as code i had prepared for question 10 of the problem set

# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"
# Also ref: https://matplotlib.org/users/pyplot_tutorial.html and https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html


import numpy
# Impurt numpy finction

import matplotlib.pyplot as plt
# import Mat lab function


data = numpy.genfromtxt('DataSet.csv', delimiter=',')

# Code below identifies the data set
SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]

# Preparing code to show multiple graphs

#1. Histogram


#2. Scatterplot
fig = plt.scatter([SepLeng] , [SepWid]) 
fig = plt.scatter([PetLeng] , [PetWid])
# specifies scatterplot graph required

plt.show() # shows grapical results. 

# Initial output was a scatter-line plot. More work needed!!
# Next attempt gave a scatterplot as required but i need to work on labelling the axes and graph





