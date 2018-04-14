#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 18:35:50 2018

@author: zoro
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
read = '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/'
write= '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/'

dfnan = pd.read_csv(write+'nanCompanies.csv').drop(['Unnamed: 0'], axis=1) # read the file and drop first column
df1= pd.read_csv(write+'filledCompanies.csv').drop(['Unnamed: 0'], axis=1) # read the file and drop first column
df3= pd.read_csv(write+'lookuptable.csv').drop(['Unnamed: 0'], axis=1) # read the file and drop first column

def check_table(nT):
    print df3[df3['normTitle'] == nT]
    
for index,row in dfnan.iterrows():
    print row[index]
    print row['estimatedSalary']
    print row['normTitle']
    check_table(row['normTitle'])
    break