# Claire Nolan 24Apr2019

# PANDS Project 2019
# AIM: Small module to analyse a data set and output the min and max values
# Data set to be analysed is Fisher's Iris Data Set

# code copied from initial work done for mean values.

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

# First code: Get the min ad max value of each column with numerical values
# Using ipython i found that "std" is used to calculate the standard deviation

MinSepLeng = numpy.min(data[:,0])
MaxSepLeng = numpy.max(data[:,0])
print("Sepal length min value is ", MinSepLeng , "and the max value is", MaxSepLeng)

# syntax for the print command is critical - commas are key ;)

MinSepWid = numpy.min(data[:,1])
MaxSepWid = numpy.max(data[:,1])
print("Sepal Width min value is ", MinSepWid , "and the max value is", MaxSepWid)

MinPetLeng = numpy.min(data[:,2])
MaxPetLeng = numpy.max(data[:,2])
print("Petal Length min value is ", MinPetLeng , "and the max value is", MaxPetLeng)

MinPetWid = numpy.min(data[:,3])
MaxPetWid = numpy.max(data[:,3])
print("Petal Width min value is ", MinPetWid , "and the max value is", MaxPetWid)


# Output gives the min and max values
