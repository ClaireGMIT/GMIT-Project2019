# Claire Nolan 24Apr2019

# PANDS Project 2019

# AIM: To creat scatterplots for the variables data with different colour data points for each species
# References:https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html ; https://matplotlib.org/users/pyplot_tutorial.html

# Data set to be analysed is Fisher's Iris Data Set
# Note 28April - Current status of trying to create graphs where data points are differentiated by colour for each species
# I have not been successful so far using the code below adapted from referenced articles
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('DataSet.csv', delimiter=',')

SepLeng = data[:,0]
SepWid = data[:,1]
PetLeng = data[:,2]
PetWid = data[:,3]
Species = data[:,4]


# Code below from in reference https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f does what i would like it to do but i can't get it to work on my data
# I will save it here copied directly from the article to retrn to it later to see if i can run it
# Explanation from article: "Now for the code. We first import Matplotlib’s pyplot with the alias “plt”. To create a new plot figure we call plt.subplots() . We pass the x-axis and y-axis data to the function and then pass those to ax.scatter() to plot the scatter plot. 
# We can also set the point size, point color, and alpha transparency. You can even set the y-axis to have a logarithmic scale. The title and axis labels are then set specifically for the figure. That’s an easy to use function that creates a scatter plot end to end!

import matplotlib.pyplot as plt
import numpy as np

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


# Below is another code that could be used is:
# Reference: https://towardsdatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f
import pandas as pd
import matplotlib.pyplot as plt
#loading dataset
df = pd.read_csv(‘workout_log.csv’)
df.columns = [‘date’, ‘distance_km’, ‘duration_min’, ‘delta_last_workout’, ‘day_category’]
def scatterplot(df, x_dim, y_dim):
  x = df[x_dim]
  y = df[y_dim]
fig, ax = plt.subplots(figsize=(10, 5))
 
  #defining an array of colors  
  colors = ['#2300A8', '#00A658']
  #assigns a color to each data point
  ax.scatter(x, y, alpha=0.70, color=colors)
 
  #adds a title and axes labels
  ax.set_title('Distance vs Workout Duration')
  ax.set_xlabel('Distance (Km)')
  ax.set_ylabel('Workout Duration (min)')
 
  #removing top and right borders
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
#adds major gridlines
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.show()
scatterplot(df, ‘distance_km’, ‘duration_min’)

# and this in the same article:
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
#loading dataset
df = pd.read_csv(‘workout_log.csv’)
df.columns = [‘date’, ‘distance_km’, ‘duration_min’, ‘delta_last_workout’, ‘day_category’]
def scatterplot(df, x_dim, y_dim, category):
  x = df[x_dim]
  y = df[y_dim]
  fig, ax = plt.subplots(figsize=(10, 5))
  #applies the custom color map along with the color sequence
  ax.scatter(x, y, alpha=0.70, c= df[category], cmap=cm.brg)
 
  #adds a title and axes labels
  ax.set_title('Distance vs Workout Duration')
  ax.set_xlabel('Distance (Km)')
  ax.set_ylabel('Workout Duration (min)')
 
  #removing top and right borders
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  #adds major gridlines
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
  plt.show()
scatterplot(df, ‘distance_km’, ‘duration_min’, ‘day_category’)



#############


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



