# Claire Nolan 26Apr2019

# PANDS Project 2019
# Small module to analyse a data set and output the mean per variable by species
# Data set to be analysed is Fisher's Iris Data Set

# I'm starting with initial program from the mean.py program. once I get this right i can then look at combining all the statitistical files into one file.

# Step 1: Format data set for analysis. I found this reference which i think will do what i want the program to do. 
# Ref: https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9. I'm going to start from section 4.
# i am going to copy program word for word and see what i get

# another ref to try: https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/

# from research, ie references above, i know the iris dataset is known in PANDAs as a DataFrame.
# A dataframe is a two or more dimensial data structure ie a table with rows and columns where the columns have headers (eg sepal length, petal width) and the rows have index (ie the iris species)


import pandas as pd # imports the Python PANDAs program
import numpy as np # imports the Python Numpy program

pd.read_csv('DataSetHeader.csv', delimiter=',')
# identifies data file to be anlysed and how to format data into columns
# data is now loaded into PANDAs
# although my data has headers already there is code that could be created to insert headers.

species = pd.read_csv('DataSetHeader.csv', delimiter=',' , names = ['Sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species'])
# can use "species" to print my data frame
# initially wrote names with a capital N but kept getting an error message. Once fixed all was well. Output was a dataframe

# Number of commands i can use to showonly art of the data. For example:
# species.head() shows the first 5 rows of data
# species.sample(5) shows five sample rows of data

# will now use this code as suggested by reference https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
# The aim is to output the mean variable for each species
species.Sepal_length.mean()

# initial result gave a number of errors ie - Traceback (most recent call last):File "C:\Users\Claire Laptop\Anaconda3\lib\site-packages\pandas\core\nanops.py", line 822, in _ensure_numeric x = float(x) ValueError: could not convert string to float: '










