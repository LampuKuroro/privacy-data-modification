#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:45:07 2019

@author: NghiTran
"""


import pandas as pd
import numpy as np

df =pd.read_csv('filled.csv')
df2 = pd.read_csv('testfilled.csv')
noised = pd.read_csv('chosen.csv')

list = ['education','marital-status','occupation','relationship','race','sex','native-country']
for (name,series) in noised.iteritems():
    noised[name][noised[name]<0] = 0

for (name,series) in noised.iteritems():
    if name in list:
        class_mapping = {label:idx for idx, label in enumerate(np.unique(df[name]))}
        for stuff in class_mapping:
            noised[name].replace(class_mapping.get(stuff),stuff,inplace = True)

noised['workclass'] = df['workclass']
noised['class'] = df['class']
noised.append(df2)
noised.to_csv('remapped.csv',index=False)
