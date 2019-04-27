# Claire Nolan 27Apr2019

# PANDS Project 2019
# Small module to analyse a data set and output the mean per variable by species
# Data set to be analysed is Fisher's Iris Data Set

# From my research i found code in references https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9. I'm going to start from section 4.
# and https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/
# This is the links for Parts 1 and 2 of the same series https://towardsdatascience.com/python-for-data-science-part-1-759524eb493b ; https://towardsdatascience.com/python-for-data-science-part-2-373d6473fa40 
# i tried it out in ipythons (see attached images) and eventually got it to work to calculate the mean value by species. I was also able to repeat for standard deviation, min and max value.
# The following reference https://towardsdatascience.com/python-for-data-science-part-4-6087cb811a29 is also useful for performing a more in-depth manipulation of the data set
import pandas as pd # imports the Python PANDAs program
import numpy as np # imports the Python Numpy program
import matplotlib.pyplot as plt # imports the Python PANDAs program

df1 = pd.read_csv('DataSetHeader.csv', delimiter=',') #identifies dataset to be analysed and how to format

#1 Generating basic statistics by species

SpMean = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].mean()
# this is the code form reference above which i found worked by practising on ipython first (see screenshots). the output is a table of the mean value of each varaible (ie sepal length and width, petal length and width) by species type
# this code is repeated below for standard deviation, min and max values
print('Mean') 
# Tried following code but found it skewed the table headers: print('Standard Deviation',SpStd) so decided to add table title separately.
print(SpMean)

# Repeated the same code for the other statistics 

SpStd = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].std()
print('Standard Deviation') 
print(SpStd)

SpMin = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].min()
print('Minimum Values') 
print(SpMin)

SpMax = df1.groupby('species')[['Sepal_length','sepal_width','petal_length','petal_width']].max()
print('Maximum') 
print(SpMax)









#################
#reference for graphs - https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f

################

#2 Generating graphs by species type

# Used the code from this reference and adapted it to suit my data set: https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f
data = np.genfromtxt('DataSetHeader.csv', delimiter=',')

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

def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, color = color, alpha = 0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)



# Overlay 2 histograms to compare them
def overlaid_histogram(data1, data2, n_bins = 0, data1_name="", data1_color="#539caf", data2_name="", data2_color="#7663b0", x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 10
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins


    if n_bins == 0
    	bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    else: 
    	bins = n_bins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins = bins, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(data2, bins = bins, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')

    ###################################
    # box plot
    def boxplot(x_data, y_data, base_color="#539caf", median_color="#297083", x_label="", y_label="", title=""):
    _, ax = plt.subplots()

    # Draw boxplots, specifying desired style
    ax.boxplot(y_data
               # patch_artist must be True to control box fill
               , patch_artist = True
               # Properties of median line
               , medianprops = {'color': median_color}
               # Properties of box
               , boxprops = {'color': base_color, 'facecolor': base_color}
               # Properties of whiskers
               , whiskerprops = {'color': base_color}
               # Properties of whisker caps
               , capprops = {'color': base_color})

    # By default, the tick label starts at 1 and increments by 1 for
    # each box drawn. This sets the labels to the ones we want
    ax.set_xticklabels(x_data)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)






