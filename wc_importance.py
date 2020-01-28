#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 00:45:18 2019

@author: NghiTran
"""
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier 
import numpy as np

x_train =pd.read_csv('x.csv')
y_train =pd.read_csv('wcy.csv')
feature = x_train.columns[0:14]

forest = RandomForestClassifier(n_estimators= 300,random_state = 0,n_jobs = -1)
forest.fit(x_train,y_train)
importance = forest.feature_importances_
indices =np.argsort(importance)[::-1]
print("ranking of importances to attribute workclass")
for f in range(x_train.shape[1]):
    print("%2d) %-*s %f"%(f+ 1,30, feature[indices[f]],importance[indices[f]]))
    
    
