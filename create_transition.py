#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 22:12:17 2018

@author: zoro
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
read = '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/month2/'
#write= '/Users/Apoorva.Rajesh.Joshi@ibm.com/Desktop/Ap version/'
filename = 'nov16.csv'
f = pd.read_csv(read+filename).drop(['Unnamed: 0'], axis=1) # read the file and drop first column

df = f.stateProvince.unique()

dict1={}
for key in df:
    if key in dict1:
        continue
    else:
        dict1[key]=0
        
dict_company = dict1
dict_job = dict1
dict_click = dict1
dict_localclick = dict1

f['acc_company']=0
f['acc_job']=0
f['acc_clicks']=0
f['acc_local_clicks']=0


for index, row in f.iterrows():
    
    sp = row['stateProvince']
    clicks = row['clicks']
    local_clicks = row['localClicks']
    print(sp)
    
    
    val1 = dict_click[sp]
    val1 = val1 + clicks
    dict_click[sp] = val1
    
    print(val1)
    row['acc_clicks']=val1
    f.set_value(index,'acc_clicks',val1)
    
    print(row['acc_clicks'])
    val2 = dict_localclick[sp]
    val2 = val2 + local_clicks
    dict_localclick[sp] = val2
    
    row['acc_local_clicks']=val2
    f.set_value(index,'acc_local_clicks',val2)
    

print(f.head())
print(f.shape)