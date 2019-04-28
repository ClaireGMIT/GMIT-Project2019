# Claire Nolan 25April2019

# PANDS Project 2019
# Code to ask the user to input values tfor petal width, petal length, sepal width and sepal length to output the probable Iris species
# Data set to be analysed is Fisher's Iris Data Set
# The Iris dataset was published and discussed in Robert Fishers 1936 paper "The use of multiple measurements in taxonomic problem". The data was collected to quantify the physical variation of Iris flowers of three related species. 
# The data set consists of 50 samples from three species of iris (Iris setosa, Iris virginica, Iris versicolor). 
# The four features measured were the length and width of the sepals and petals in centimetres. 
# The combination of these four features can be used to identify each particular species

# Below is an adaptation of the code I prepared for question 4 of the problem set from March2019
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"

# I will ask the user to in

SW = int(input("Please enter the Sepal Width: "))
SL = int(input("Please enter the Sepal Length: "))
PW = int(input("Please enter the Petal Length: "))
PL = int(input("Please enter a positive integer: "))

while x > 1: 

    if x % 2 == 0: 
        x = x / 2 # ie if X is divisible by 2 then provide a new number which is the result of x divided by 2

    elif x % 2 != 0:
                x = (x*3)+1 # ie if X is not divisible by 2 then provide a new number which is the result of x multiplied by 3 plus 1

    print(int(x)) #print the list of values as integer






