# GMIT-Project2019
PANDS Project 2019 - Project 2019 for Programming and scripting course

Code to statistically analyse a data set
Data set to be analysed is Fisher's Iris Data Set
The Iris dataset was published and discussed in RObert Fishers 1936 paper "The use of multiple measurements in taxonomic problem". The data was collected to quantify the physical variation of Iris flowers of three related species. 
The data set consists of 50 samples from three species of iris (Iris setosa, Iris virginica, Iris versicolor). 
The four features measured were the length and width of the sepals and petals in centimetres. 
The combination of these four features can be used to identify each particular species

23April2019
    *Have created code to import the numpy program for performing scientific calculations
    *Have used iPython on CMDER to check that code i am writing is error free. i have found some errors but have resolved them. see notes in code for examples
    *Have written code to find the mean value for data in each column
    *Prepared a HIPO project plan which is a hierarchy Input Process Output flow chart showing how i will create small simple modules for codes then joining together into a larger module.


24April2019
    *Updated initial code and broke into smaller, simple modules to perform each data analysis - mean, standard deviation, min/max values and graphs - s per HIPO project plan
    *Combined smaller modules into one larger module for basic statisitics. If i have time I would like to look at having the output be in a table.
    *Began some initial graphs - scatterplot successful, histograms next
    *Next step is to sub divide it by species and create graphs.
    *Need to look at how to report output in 1 or 2 decimal places

25April2019
    *Worked on labelling the scatter graph title and axes. Used and reread https://matplotlib.org/users/pyplot_tutorial.html using a practise file to copy and paste code from tutorial so i could understand what each line of code would do. 
    *I was also able to create histograms. 
    *Currently output in "BasicGraphs.py" shows scatter plots (four graphs - two proahs per two window) and histograms (four graphs pn one window and one graph on four windows)  
    *Next steps to look at dividing output by species

26April2019
    *Basic summary stats program (BasicSummStats.py) and graph program (BasicGraphs.py) joined into one program called "SummaryStatsGraph.py". this is now a program that will take a data set, format data into an array for analysis then perform analysis on the data. The output is summary statistics (mean standard, deiation, min/max), histogram and scatterplots for each variable.
    *As per my HIPO plan i have completed one section of my project plan. The next step is to repeat the same program but sub divide the output by species.
    *Began looking at using PANDAs to organise my data into 2D dataframes ie columne containing data and rows containing indexes. Having some issues with errors which i'll look into more tomorrow.

27April2019 Morning
    *This morning i am rereading the 10 minutes to PANDs notes (ref:https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) and practising to understand what it does via using ipython
    *During my reading i think i code some code which i may be able to use to allow my summary stats be displayed as a table via the append section of the notes. I am going to practise via ipython and using the BasicSummStats.py file. After much practice on ipython i got wrote code to output the summary stats in a table. the Summary StatsGraph.py file has been updated
   
27April2019 Afternoon
    *Successfully able to display stats by species type - references in the files to be added here
    *I'm stuck on trying to dispplay graphs whihc colour code by species. i ahve done some research but i think i am over complicating it. Will try again tomorrow.
    *will also try to write program for estimating probable Iris species based on inputted data tomorrow.
