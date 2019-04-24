# Claire Nolan 24Apr2019

# PANDS Project 2019
# Combining mean.py, StdDev.py, MinMax.py and Graph.py small modules into one larger module to out  the basic summary stats for each column
# Data set to be analysed is Fisher's Iris Data Set

import numpy

data = numpy.genfromtxt('DataSet.csv', delimiter=',')

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]

# Initally copied and pasted all code into this file but the out put was too crude

meanSepLeng = numpy.mean(data[:,0])
print("Mean Sepal length is ", meanSepLeng)

meanSepWid = numpy.mean(data[:,1])
print("Mean Sepal Width is ", meanSepWid)

meanPetLeng = numpy.mean(data[:,2])
print("Mean Petal length is ", meanPetLeng)

meanPetWid = numpy.mean(data[:,3])
print("Mean Petal Width is ", meanPetWid)

StdSepLeng = numpy.std(data[:,0])
print("Sepal length standard deviation is ", StdSepLeng)

StdSepWid = numpy.std(data[:,1])
print("Sepal Width standard deviation is ", StdSepWid)

StdPetLeng = numpy.std(data[:,2])
print("Petal length standard deviation is ", StdPetLeng)

StdPetWid = numpy.std(data[:,3])
print("Petal Width standard deviation is ", StdPetWid)

MinSepLeng = numpy.min(data[:,0])
MaxSepLeng = numpy.max(data[:,0])
print("Sepal length min value is ", MinSepLeng , "and the max value is", MaxSepLeng)

MinSepWid = numpy.min(data[:,1])
MaxSepWid = numpy.max(data[:,1])
print("Sepal Width min value is ", MinSepWid , "and the max value is", MaxSepWid)

MinPetLeng = numpy.min(data[:,2])
MaxPetLeng = numpy.max(data[:,2])
print("Petal Length min value is ", MinPetLeng , "and the max value is", MaxPetLeng)

MinPetWid = numpy.min(data[:,3])
MaxPetWid = numpy.max(data[:,3])
print("Petal Width min value is ", MinPetWid , "and the max value is", MaxPetWid)




