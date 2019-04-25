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



# 1: Scatterplot
fig = plt.scatter([SepLeng] , [PetLeng]) 
fig = plt.scatter([SepWid] , [PetWid])
# specifies scatterplot graph required

#25Apr - use code below to label the graph title, x and y axis after rereading https://matplotlib.org/users/pyplot_tutorial.html 
# Also used a practise file to practise creating graphs

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

###########################################


plt.figure(3)
plt.title(r'$\sigma_i=15$')
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
#####################################################

plt.show() # shows grapical results. 


