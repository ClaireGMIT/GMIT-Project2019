# Claire Nolan 25Apr2019

########
# To be started
########



# PANDS Project 2019
# Small module to analyse a data set and output the standard deviation per variable by species
# Data set to be analysed is Fisher's Iris Data Set

# code copied from initial work done for mean values.
# I'm going to try loops to get results by mean

# Step 1: Format data set for analysis

import numpy

data = numpy.genfromtxt('DataSet.csv', delimiter=',')

# this line of code states that the data to be analysed is generated from the DataSet.csv file and that the data should be separated into columns using the comma as a delimiter.

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]
# SepLen is used to identify all Sepal length data, SepWid identifies Sepal Width, PetLeng identifes petal length, PetWid identifes petal width and species defines the iris species

# First code: Try with one variable first and if works then repeat


StdSepLeng = numpy.std(data[:,0])


print("Sepal length standard deviation is ", StdSepLeng)



# Output gives the standard deviation





