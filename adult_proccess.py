#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:54:42 2019

@author: NghiTran
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

df =pd.read_csv('adult.csv')
print(df.describe())
list = ['class','workclass','education','marital-status','occupation','relationship','race','sex','native-country']
for name in list:
    fig,ax=plt.subplots(1,1)
    ax = (df[name].value_counts().plot(kind='bar') )
    ax.set_title(name)


df.replace('?', np.nan, inplace = True)
df.to_csv('nan.csv',index=False)

for (name,series) in df.iteritems():
    print('\nAtribute\'s name: '+ str(name))
    print('Count:' +str(df[name].size))
    print('Missing values:',(sum(df[name].isnull().values.ravel()) ))
    
for (name,series) in df.iteritems():
    temp = df[name].value_counts()
    freq = str(temp.index[0])
    df[name].fillna(freq,inplace=True)

#df.to_csv('filled.csv',index=False)

for name in list:
    class_mapping = {label:idx for idx, label in enumerate(np.unique(df[name]))}
    df[name] = df[name].map(class_mapping)
    print(class_mapping)
    
correlation = df.corr()
correlation.to_csv('corr.csv',index=False)
#df.to_csv('mapped.csv',index=False)

#cy = df['class']
#cy.to_csv('cy.csv',index=False)
#cy = df['workclass']
#cy.to_csv('wcy.csv',index=False)
#df.pop('class')
#df.pop('workclass')
#df.to_csv('x.csv',index=False)





