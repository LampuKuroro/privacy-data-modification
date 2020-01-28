#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:30:21 2019

@author: NghiTran
"""

from pandas import DataFrame 

x_train =pd.read_csv('cx.csv')
y_train =pd.read_csv('cy.csv')
feature = x_train.columns[0:14]

forest = RandomForestClassifier(n_estimators= 100,random_state = 0,n_jobs = -1)
forest.fit(x_train,y_train)
importance = forest.feature_importances_
indices =np.argsort(importance)[::-1]
print("ranking of importances to attribute class")
for f in range(x_train.shape[1]):
    print("%2d) %-*s %f"%(f+ 1,30, feature[indices[f]],importance[indices[f]]))
    
    
