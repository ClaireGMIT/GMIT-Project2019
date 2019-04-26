# Claire Nolan 26Apr2019

# PANDS Project 2019
# Small module to analyse a data set and output the mean per variable by species
# Data set to be analysed is Fisher's Iris Data Set

# I'm starting with initial program form the 

# Step 1: Format data set for analysis. Note i had to save a new CSV file as i had deleted the headers on my original dataset CSV file.
# Data set used saved as DataSetHeader.csv. Sata set downloaded from this location: https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv


import pandas as pd
import numpy as np

data = numpy.genfromtxt('DataSet.csv', delimiter=',')