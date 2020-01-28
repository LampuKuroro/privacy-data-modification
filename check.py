#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:43:32 2019

@author: NghiTran
"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

y1_train =pd.read_csv('cy.csv')
y2_train =pd.read_csv('wcy.csv')
x_test =pd.read_csv('testx.csv')
y1_test =pd.read_csv('testcy.csv')
y2_test =pd.read_csv('testwcy.csv')
list = ['1.csv','2.csv','3.csv','4.csv','5.csv','6.csv','7.csv','8.csv','9.csv','10.csv']
for i in list:
    x_train =pd.read_csv(i)
    resultsE = pd.DataFrame(columns = ['Level Limit','Score for Training','Score for Testing'])
    for treeDepth in range (1,12 ):
        dct = DecisionTreeClassifier(criterion='entropy',max_depth = treeDepth, random_state = 2)
        dct = dct.fit(x_train,y1_train)
        dct.predict(x_test)
        scoreTrain = dct.score(x_train,y1_train)
        scoreTest = dct.score(x_test,y1_test)
        resultsE.loc[treeDepth] = [treeDepth,scoreTrain, scoreTest]
        
    resultsE.pop('Level Limit')
    fig,ax = plt.subplots(1,1 )
    ax.set_title('class (privacy) tree'+i)
    ax.plot(resultsE)

    resultsG = pd.DataFrame(columns = ['Level Limit','Score for Training','Score for Testing'])
    for treeDepth in range (1,12 ):
        dct1 = DecisionTreeClassifier(criterion='entropy',max_depth = treeDepth, random_state = 2)
        dct1 = dct1.fit(x_train,y2_train)
        dct1.predict(x_test)
        scoreTrain = dct1.score(x_train,y2_train)
        scoreTest = dct1.score(x_test,y2_test)
        resultsG.loc[treeDepth] = [treeDepth,scoreTrain, scoreTest]

    resultsG.pop('Level Limit')
    fig,ax = plt.subplots(1,1 )
    ax.set_title('workclass (utility) tree'+i)
    ax.plot(resultsG)
