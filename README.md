# privacy-data-modification
Inject noises into a data set using python so that we can project privacy information without hurting utility
HOW TO RUN THE CODE:
____________________________________________
1/ Run either ignoise.py (if you want to use information gain) or corrnoise.py (if you want to use corelation), or both if you want to compare
	=> it will generate 1 privacy graph and one utility graph
	=> it will also generate a table of utility/privacy, the higher the number, the better the module
_______________________________________________

2/ Based on the info given, choose the file you think is the best, name it ‘chosen.csv’
_________________________________________________

3/ Run remap.py, it will generate the final NoisedData.csv the you desire
___________________________________________________





*******************************************

Optional:
____________________________________________________________________________________

Walkthrough all project 1 files:

1/	adult.cvs and adulttest.csv are training and testing dataset. The code provided only modify training data, you can change the code to add noise in testing data if you want.

2/	adult_process.py and testprocess.py are code to fill in missing data in adult.cvs and adulttest.csv, mapping categorical data to numeric values and split data set in to x and y sets for training and testing. You can uncomment the last few lines to generate new x and y sets however it is recommended to us the x and y sets provided to prevent errors.

3/	x.csv, cy.csv, wcy.csv are training datasets with cy= class as y, wc=workclass as y, these are generated using adult_process.py

4/	testx.csv, testcy.csv, testwcy.csv are testing datasets with testcy= class as y, testwc= workclass as y, these are generated using adult_process.py

5/	classimportance.py and wc_importance.py generate a list of attributes in order of their information gain based of class and workclass respectedly, used to decide ground truth and what to add noised using INFORMATION GAIN.

6/	correlation.csv a table of correlation between classes, used to decide ground truth and what to add noised using CORRELATION.

7/	ignoise.py (Information gain noise) is the code used to generate 10 csv files that add noises using gausian normal distribution. The noise is added to the least information gain compare to workclass and the most compare to class.

8/	corrnoise.py (correlation noise) is the code used to generate 10 csv files that add noises using gausian normal distribution. The noise is added to the least correlated  to workclass and the most correlated to class.

9/	remap.py is the code used to transfered the numeric data back to categorical data set at the begining.

10/	check.py used the 10 csv files to draw out the different decision trees to give us the bigger picture than just a slice of the truth, used to check you answer.

11/	treechoose.py is used to choose which decision tree is the best for learning methods, in this case I choose entropy tree with level limit of 7, you can change the method for different results
**********************************************************

Incase code doesn’t run, replace all x and y sets with backup x and y sets.
