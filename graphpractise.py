# This is a practise file


import numpy

import matplotlib.pyplot as plt
import pandas as pd

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


df1 = pd.DataFrame([{'Variable' : 'Sepal Length', 'Mean' :  meanSepLeng, 'Std Dev' : StdSepLeng},{'Variable' : 'Sepal Width', 'Mean' :  meanSepWid, 'Std Dev' : StdSepWid},{'Variable' : 'Petal Length', 'Mean' :  meanPetLeng, 'Std Dev' : StdPetLeng}],index=['1','2','3'] )
df1




