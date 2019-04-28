# Claire Nolan 28April2019

# PANDS Project 2019

# AIM: Code to ask the user to input values tfor petal width, petal length, sepal width and sepal length to output the probable Iris species
# Data set to be analysed is Fisher's Iris Data Set

# The Iris dataset was published and discussed in Robert Fishers 1936 paper "The use of multiple measurements in taxonomic problem". The data was collected to quantify the physical variation of Iris flowers of three related species. 
# The data set consists of 50 samples from three species of iris (Iris setosa, Iris virginica, Iris versicolor). 
# The four features measured were the length and width of the sepals and petals in centimetres. 
# The combination of these four features can be used to identify each particular species
# These are some references i found for calculating the probabilty which i consulted. https://www.dataquest.io/blog/basic-statistics-in-python-probability/


# Step 1: Identify the dataset to be analysed and the stats to be claulculate as per code created in file StatSpecies.py
import pandas as pd # imports the Python PANDAs program
import numpy as np # imports the Python Numpy program
import matplotlib.pyplot as plt # imports the Python PANDAs program

data = pd.read_csv('DataSetHeader.csv', delimiter=',') #identifies dataset to be analysed and how to format



# Below is an adaptation of the code I prepared for questions 4 and 5 of the problem set from March2019
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"

# Step 2: code below asks the user to input the various variables. 
SW = int(input("Please enter the Sepal Width: ")) 
SL = int(input("Please enter the Sepal Length: "))
PL = int(input("Please enter the Petal Length: "))
PW = int(input("Please enter the Petal Width: "))

# Step 3: Most data should be contained in the following range (mean-3*StdDev, mean+3*StdDev). 
# I haven't been able to create the code to calculate these ranges for each variable by species so i used the output from program file "statSpecies.py" to claculate the number manually
# Ranges:
#       Sepal Length: Setosa (3.95-6.06); Versicolor (4.39-7.48); Virginica (4.68-8.50) 
#       Sepal Width: Setosa (2.27-4.56); Versicolor (1.83-3.71); Virginica (2.01-3.94) 
#       Petal Length: Setosa (0.94-1.98); Versicolor (2.85-5.67); Virginica (3.90-7.21) 
#       Petal Width: Setosa (-0.08-0.57); Versicolor (0.73-1.92); Virginica (1.20-2.85) 
# screenshot is saved to github file 

#Below is initial attempt at code. My thought process is that if the user has an Iris flower then if they inputted the various parameters then the program could identify the iris species.  


for i in range(4, 6): #ie for all numbers in this range
    if SL isin range(3.95, 6.06): 
        and SW is in range(2.27, 4.56)
        and PL is in range(0.94, 1.98)
        and PW is in range(-0.08,0.57)
        print(i, "is probably a Setosa Iris")
        break # required to stop an inifinite loop and to allow program to move to the next step
            
else: #otherwise if i has no factors then it must be a prime number
    if SL is in range(4.39, 7.48): 
        and SW is in range(1.83, 3.71)
        and PL is in range(2.85, 5.67)
        and PW is in range(0.73, 1.92)
        print(i, "is probably a Versicolor Iris")
        break # required to stop an inifinite loop and to allow program to move to the next step

else: #otherwise if i has no factors then it must be a prime number
    if SL is in range(4.68, 8.50): 
        and SW is in range(2.1, 3.94)
        and PL is in range(3.90, 7.21)
        and PW is in range(1.20, 2.85)
        print(i, "is probably a Setosa Iris")
        break # required to stop an inifinite loop and to allow program to move to the next step


# there were a lot of issues with this code including integers vs floats


#################
#Could also try adapt the code below which i used for the ProblemSet2019 project
x = int(input("Please enter a positive integer: "))

while x > 1: 

    if x % 2 == 0: 
        x = x / 2 # ie if X is divisible by 2 then provide a new number which is the result of x divided by 2

    elif x % 2 != 0:
                x = (x*3)+1 # ie if X is not divisible by 2 then provide a new number which is the result of x multiplied by 3 plus 1

    print(int(x)) #print the list of values as integer


for n in range(1000 , 10000):

   for x in range(1000, n):

      if n % 6 == 0: #ie if the number is divisible by 6 then go to next step and check if it divisible by 12
         if n % 12 != 0: # if the number is not divisible by 12...
              print(n, "is divisible by 6 but not 12" ) #print the list of number
              break # stops the program at each number otherwise goes into an inifinite loop. this happened a few times
              
   
