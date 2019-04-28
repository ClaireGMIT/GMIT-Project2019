# GMIT-Project2019
PANDS Project 2019 - Project 2019 for Programming and scripting course
Claire Nolan 28April2019

1. EXECUTIVE SUMMARY
The aim of this project was to take a data set and create code which would to analyse the data. The dataset used was Fishers Iris Data Set. Upon completion of this project for the final commit to ClaireGMIT/GMIT-Project2019 i was able to take the data set, describe the basic summary statisitics, and publish histogram and scatterplots. This was also performed on a species by species basis. See files SummaryStatsGraph.py and StatSpecies.py. The scatterplot of variables using different coloured data points identiying each species was also created as per file SummGraphSps.py. More work is required for this as the output is crude. I was unsuccessful in creating code to isdentify the iris type when the user inputted the sepal width and length and petal width and length. The work to resolve these issues are shown in various screenshots and in files GraphbySpecies.py, GraphSps.py and SpesProb.py. 


2. INTRODUCTION
This project has been prepared to show the power of the Python programming language in interpreting a dataset. The sample dataset to be interpreted is Fisher’s Iris Dataset. 

Ronald Fisher  (1890 - 1962) was a biologist who through his work on population genetics invented statistical hypothesis testing and design of experiments (DOE). The Iris dataset was published and discussed in his 1936 paper The use of multiple measurements in taxonomic problems . The data was collected to quantify the physical variation of Iris flowers of three related species. The data set consists of 50 samples from all three species of iris (Iris setosa, Iris virginica, Iris versicolor). The four features measured were the length and width of the sepals and petals in centimetres. The combination of these four features can be used to identify each particular species.

Python is a computing programming language which is high-level and general-purpose. It was created in 1991 by Guido van Rossum with the aim of emphasising code readability by being user-friendly and easy to learn   .

First research will be performed via an internet search on the Iris dataset. This aim will be to find the dataset, investigate techniques for manipulating and formatting the dataset, and research what work has previously been performed on the dataset that can be incorporate into this project. 
Next, the project will be broken down into several simple modules to allow the project to easily managed in small parts. For each module the input, process and output will be identified. Research will also be performed to find code that can be used to get meaningful output from the data.
Then, using the formatted dataset, code will be developed to evaluate the dataset and provide an output. The result of this output will be discussed. Conclusions on the output and the work performed will be discussed.

A project plan was created (HIPO Project Plan.pptx) to breakdown the project into small units. This also aided a full literature review. 

The first aim was to create a code that would output the mean, standard deviation and minimum, maximum values for each variable. Code for each of these variables was created individually then combined into one file (BasicSummStats.py) The next step was to create code to output histogram and scatterbox plots. These smaller modules would then be combined so when the program is run the user woudl see the basic summary statistics for each variable and the corresponding histograms and scatterplots.

The second aim would then take the code created above and subdivide them by species type. Again code for each of these variables was created individually then combined into one file (StatSpecies.py) The next step was to create code to output histogram and scatterbox plots. These smaller modules would then be combined so when the program is run the user woudl see the basic summary statistics for each variable and the corresponding histograms and scatterplots differentiated by species type.

The third aim is create code to allow the user to input variables for the Iris they have and identify the most probable Iris species.

The report details the literature which was reviewed for the project, the steps taken to complete the project forllowed by resulsts and conclusion.


3. LITERATURE REVIEW
Below are all the references used for this project. Each file contains the specific reference used for the particular piece of code. I also reguarly consulted the course web tutorials and my own notess.

a.	Fisher’s Iris Data Set
https://en.wikipedia.org/wiki/Ronald_Fisher
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching/74901

b.	Formatting a data set
https://gist.github.com/curran/a08a1080b88344b0c8a7
https://archive.ics.uci.edu/ml/datasets/iris
https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset

c.	Python code for statistics and graphical output
https://docs.python.org/3/tutorial/introduction.html
http://spronck.net/pythonbook/pythonbook.pdf
https://www.youtube.com/watch?v=Nu7pGuenbwo
https://www.youtube.com/watch?v=Nu7pGuenbwo
https://www.youtube.com/watch?v=ywIWUfjPCyY
https://datascience.stackexchange.com/questions/43057/how-to-classify-iris-flowers
https://matplotlib.org/users/pyplot_tutorial.html

d. Other
https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
https://matplotlib.org/users/pyplot_tutorial.html 
https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f 
https://towardsdatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f3
https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html 
https://docs.scipy.org/doc/numpy-1.13.0/user/whatisnumpy.html
https://www.numpy.org/
https://www.dataquest.io/blog/basic-statistics-in-python-probability/
https://towardsdatascience.com/python-for-data-science-part-3-be9b08660af9
https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/
https://towardsdatascience.com/python-for-data-science-part-1-759524eb493b 
https://towardsdatascience.com/python-for-data-science-part-2-373d6473fa40 
https://towardsdatascience.com/python-for-data-science-part-4-6087cb811a29 
Book: "python in easy steps" by Mike Mcgrath"
https://stackoverflow.com/questions/8202605/matplotlib-scatterplot-colour-as-a-function-of-a-third-variable


4. PROJECT PLAN and WORK FLOW TO DEVELOP THE PROGRAM
Below is a description of all the work I performed on a regular basis. More specific explanations and information can also be found in each of the project files. There are also screenshots showing some of my attempts at writing the code attached to the project as well.

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

28April2019
    *Today the plan is to finish printing graphs for each variable by species,create a program to ask user to input variables and get an output identifying probable Iris species, then tidy code and complete the readme file as a project report.
    *Yesterday i got stuck on the graph outputs displaying different colours by species. Today i reread the matplot library tutorial https://matplotlib.org/users/pyplot_tutorial.html to get back to basics. I was not successful. *I also rewateched the MatPlotLib tutorial and read the following articles. https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html ; https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f ; https://towardsdatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f 
    *I was not successful in adapting the sample codes in these articles but i have added them to program "GraphbySpecies.py" to try again at a later date
    *I moved on the creating a program that would help identify the most probable Iris species when the user inputs the petal length and width, and the Sepal length and width. Unfortunately i had to create data in excel for the caluculating the range (mean+/-(3*StdDev)) but i contnued with the rest of the program
    *Update after final commit - i was also able to find code which gave the result for the scatterplots by species. This is saved in SummGraphSps.py and gives very crude output. The next steps would be to refine the output by adding a legend, making more charts etc.

5. RESULTS
The aim of this project was to take a data set and create code which would to analyse the data. The dataset used was Fishers Iris Data Set. I broke the project into small modules and worked on the small modules independently then combined them when they were successful. 

Upon completion of this project for the final commit to ClaireGMIT/GMIT-Project2019 i was able to take the data set, describe the basic summary statisitics, and publish histogram and scatterplots. This was also performed on a species by species basis. See files SummaryStatsGraph.py, SummGraphSps.py and StatSpecies.py. 

An attempt was made to output scatterplots with coloured data points for each Iris species but this was not successful. I was also unsuccessful in creating code to isdentify the iris type when the user inputted the sepal width and length and petal width and length. This was also unsuccessful. My work to resolve is shown in various screenshots and in files GraphbySpecies.py, GraphSps.py and SpesProb.py.


6. CONCLUSION
From this project I learnt how code could be created to manipulated any dataset, in this case the Fisher Iris dataset, and output some useful information about the data. I also learnt that syntax, case, spelling etc are important when writing a program. Also that Python is a language and like any langauge has to be practised on a regular basis. From my research there is a lot more i can do when exploring datasets and I'm excited to keep practising and getting better at using Python.
