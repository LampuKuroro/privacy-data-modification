#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:54:19 2019

@author: NghiTran
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier 
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

df =pd.read_csv('adulttest.csv')
df.replace('?', np.nan, inplace = True)
for (name,series) in df.iteritems():
    temp = df[name].value_counts()
    freq = str(temp.index[0])
    df[name].fillna(freq,inplace=True)
df.to_csv('testfilled.csv',index=False)
list = ['class','workclass','education','marital-status','occupation','relationship','race','sex','native-country']  
for name in list:
    class_mapping = {label:idx for idx, label in enumerate(np.unique(df[name]))}
    df[name] = df[name].map(class_mapping)
    print(class_mapping)
    

#cy = df['class']
#cy.to_csv('testcy.csv',index=False)
#wcy = df['workclass']
#wcy.to_csv('testwcy.csv',index=False)
#df.pop('class')
#df.pop('workclass')
#df.to_csv('testx.csv',index=False)
#df.to_csv('testfilledmapped.csv',index=False)

    


