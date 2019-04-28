# Claire Nolan 23Apr2019

# PANDS Project 2019

# AIM: Small module to analyse a data set and output the min and max values
# Data set to be analysed is Fisher's Iris Data Set
# note i did not continue with any further work on this file

# Code to statistically analyse a data set
# Data set to be analysed is Fisher's Iris Data Set
# The Iris dataset was published and discussed in RObert Fishers 1936 paper "The use of multiple measurements in taxonomic problem". The data was collected to quantify the physical variation of Iris flowers of three related species. 
# The data set consists of 50 samples from three species of iris (Iris setosa, Iris virginica, Iris versicolor). 
# The four features measured were the length and width of the sepals and petals in centimetres. 
# The combination of these four features can be used to identify each particular species


# Step 1: Format data set for analysis
# Note: Using ipython to check code quality before importing into python file

import numpy

# numpy is the package for scientific computing in Python and is the script used to analyse a data file.
# https://docs.scipy.org/doc/numpy-1.13.0/user/whatisnumpy.html
# https://www.numpy.org/

data = numpy.genfromtxt('DataSet.csv', delimiter=',')

# this line of code states that the data to be analysed is generarted from the DataSet.csv file and that the data should be separated into columns using the comma as a delimiter.
# this line of code was written in iPython mode first to ensure no erros. i initially got a syntax error message but this was because i firgot to put an equal sign after the word delimite
# in iPython can type "data" to return array of data etc. This can be useful if need to 2eyeball" the data to sensecheck any of the results in the future

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]
# SepLen is used to identify all Sepal length data, SepWid identifies Sepal Width, PetLeng identifes petal length, PetWid identifes petal width and species defines the iris species
# this idea was taken from the Numpy Library online video from week 9. i used iPython to confirm i got the correct data from each column
# realised i needed to remove column headers from dataset.csv file as the code wasn't working. once fixed all worked well. I noticed this is iPython

# First code: Get the mean of each column with numerical values

meanSepLeng = numpy.mean(data[:,0])
print("Mean Sepal length is ", meanSepLeng)

meanSepWid = numpy.mean(data[:,1])
print("Mean Sepal Width is ", meanSepWid)

meanPetLeng = numpy.mean(data[:,2])
print("Mean Petal length is ", meanPetLeng)

meanPetWid = numpy.mean(data[:,3])
print("Mean Petal Width is ", meanPetWid)

# Output gives the mean values. I will copy this code for standard deviation and min/max values
# I will also eventually these single modules into one module to give basic summary stats as an output
# But there are three species of Iris so will need to break down the average by each species




