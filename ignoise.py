#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:37:24 2019

@author: NghiTran
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import random 

x_train =pd.read_csv('x.csv')
cy_train =pd.read_csv('cy.csv')
wy_train =pd.read_csv('wcy.csv')
x_test =pd.read_csv('testx.csv')
cy_test =pd.read_csv('testcy.csv')
wy_test =pd.read_csv('testwcy.csv')
#information gain noise:

list = {'capital-gain':0,'relationship':5,'marital-status':6 ,'capital-loss':0,'native-country':40,'race':4,'sex':1}
resultsC = pd.DataFrame(columns = ['noise level','Score for Training','Score for Testing'])
resultsW = pd.DataFrame(columns = ['noise level','Score for Training','Score for Testing'])
results = pd.DataFrame(columns = ['uti/privacy'])
for noise in range(1,10):
    #x_train['native-country'] += random.randint(0,2)
    #x_train['native-country'][x_train['native-country']>40] -= 40
    #for name in list:
    #    x_train[name] += random.randint(0,5)
    #    x_train[name][x_train[name]>list[name]] -= list[name]
    for name in list:
        mu, sigma = 0, 0.1 
        gause = np.random.normal(mu, sigma, 32561)
        x_train[name] = x_train[name] + gause
        x_train[name][x_train[name]>list[name]] -= list[name]
    dct = DecisionTreeClassifier(criterion='entropy',max_depth = 7, random_state = 2)
    dct = dct.fit(x_train,cy_train)
    dct.predict(x_test)
    classTrain = dct.score(x_train,cy_train)
    classTest = dct.score(x_test,cy_test)
    resultsC.loc[noise] = [noise,classTrain, classTest]
    dct1 = DecisionTreeClassifier(criterion='entropy',max_depth = 7, random_state = 2)
    dct1 = dct1.fit(x_train,wy_train)
    dct1.predict(x_test)
    wcTrain = dct.score(x_train,wy_train)
    wcTest = dct.score(x_test,wy_test)
    resultsW.loc[noise] = [noise,wcTrain, wcTest]
    wcRatio = wcTest/classTest
    results.loc[noise] = [wcRatio]
    x_train.to_csv(str(noise)+'.csv',index=False, float_format='%.f')

resultsC.pop('noise level')
fig,ax = plt.subplots(1,1 )
ax.set_title('class(privacy)')
ax.plot(resultsC)

resultsW.pop('noise level')
fig,ax = plt.subplots(1,1 )
ax.set_title('workclass(utility)')
ax.plot(resultsW)

print(results)
