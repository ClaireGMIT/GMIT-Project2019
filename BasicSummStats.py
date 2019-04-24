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

# Initally copied and pasted all code into this file but while i got all the statistic values, the output was too crude. Next step is tidy up the output

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

print("Sepal Length Summary Statistics are:" , "mean: ", meanSepLeng, ", Std Dev: ", StdSepLeng, ", min and max:", MinSepLeng , MaxSepLeng)

print("Sepal Width Summary Statistics are:" , "mean: ", meanSepWid, ", Std Dev: ", StdSepWid, ", min and max:", MinSepWid , MaxSepWid)

print("Petal Length Summary Statistics are:" , "mean: ", meanPetLeng, ", Std Dev: ", StdPetLeng, ", min and max:", MinPetLeng , MaxPetLeng)

print("Petal Width Summary Statistics are:" , "mean: ", meanPetWid, ", Std Dev: ", StdPetWid, ", min and max:", MinPetWid , MaxPetWid)

# This tidies up the data but if i have time i will try to give the output in a table format