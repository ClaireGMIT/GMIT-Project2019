# Claire Nolan 24Apr2019

# PANDS Project 2019
# AIM: Small module to analyse a data set and output the standard deviation
# Data set to be analysed is Fisher's Iris Data Set

# code copied from initial work done for mean values (Mean.py).

# Step 1: Format data set for analysis

import numpy

data = numpy.genfromtxt('DataSet.csv', delimiter=',')

# this line of code states that the data to be analysed is generarted from the DataSet.csv file and that the data should be separated into columns using the comma as a delimiter.

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]
# SepLen is used to identify all Sepal length data, SepWid identifies Sepal Width, PetLeng identifes petal length, PetWid identifes petal width and species defines the iris species

# First code: Get the standard deviation of each column with numerical values
# Using ipython i found that "std" is used to calculate the standard deviation

StdSepLeng = numpy.std(data[:,0])
print("Sepal length standard deviation is ", StdSepLeng)

StdSepWid = numpy.std(data[:,1])
print("Sepal Width standard deviation is ", StdSepWid)

StdPetLeng = numpy.std(data[:,2])
print("Petal length standard deviation is ", StdPetLeng)

StdPetWid = numpy.std(data[:,3])
print("Petal Width standard deviation is ", StdPetWid)

# Output gives the standard deviation





