#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:48:06 2018
code to create_transition by day
@author: zoro
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
read = '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/month2/'
write= '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/'
filename = 'nov16.csv'


def create_mini_dataframe(df1,datevalue):
    Company_per_state = df1.groupby('stateProvince')['companyId'].nunique().sort_values()
    cps = Company_per_state.to_frame()
    cps = cps.reset_index()

    Job_per_state = df1.groupby('stateProvince')['jobId'].nunique().sort_values()
    jps = Job_per_state.to_frame()
    jps = jps.reset_index()

    estimated_salary = df1.groupby('stateProvince')['estimatedSalary'].mean().sort_values()
    es = estimated_salary.to_frame()
    es = es.reset_index()

    min_estimated_salary = df1.groupby('stateProvince')['estimatedSalary'].min().sort_values()
    mines = min_estimated_salary.to_frame()
    mines = mines.reset_index()

    max_estimated_salary = df1.groupby('stateProvince')['estimatedSalary'].max().sort_values()
    maxes = max_estimated_salary.to_frame()
    maxes = maxes.reset_index()

    total_clicks = df1.groupby('stateProvince')['clicks'].sum().sort_values()
    tc = total_clicks.to_frame()
    tc = tc.reset_index()

    total_local_clicks = df1.groupby('stateProvince')['localClicks'].sum().sort_values()
    tlc = total_local_clicks.to_frame()
    tlc = tlc.reset_index()

    df2 = pd.merge(cps,jps,on='stateProvince')
    df2 = pd.merge(df2,es,on='stateProvince')
    df2 = pd.merge(df2,mines,on='stateProvince')
    df2 = pd.merge(df2,maxes,on='stateProvince')
    df2 = pd.merge(df2,tc,on='stateProvince')
    df2 = pd.merge(df2,tlc,on='stateProvince')

    mean_estimatedSalary_y = df2['estimatedSalary_y'].mean(skipna=True)
    df2=df2.replace({'estimatedSalary_y': {0: mean_estimatedSalary_y}}) 

    df2.columns = ['stateProvince','companyId','jobId','mean_estimatedSalary','min_estimatedSalary','max_estimatedSalary','clicks','localClicks']

    df2['date'] = datevalue

    cols = df2.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df2 = df2[cols]
    
    return df2

def create_main_dataframe(filename):
    
    df = pd.read_csv(read+filename).drop(['Unnamed: 0'], axis=1) # read the file and drop first column
    datestamp = df['date'].unique()
    l = np.shape(datestamp)
    df1 = df[df.date == datestamp[0]]
    df2 = create_mini_dataframe(df1,datestamp[0])
    #print(df2.shape)
    
    for i in range(1,l[0]):
       # print(i)
        df1 = df[df.date == datestamp[i]]
        df21 = create_mini_dataframe(df1,datestamp[i])
        #print(df21.shape)
        df2 = df2.append(df21, ignore_index=True)
        
    return df2

df_main = create_main_dataframe('nov16.csv')

list1 = ['dec16.csv','jan17.csv','feb17.csv','mar17.csv','apr17.csv','may17.csv','jun17.csv','jul17.csv','aug17.csv','sep17.csv','oct17.csv','nov17.csv']

for files in list1:
    print('writing from files : ' + files)
    df3 = create_main_dataframe(files)
    df_main = df_main.append(df3, ignore_index=True)


print(df_main.head())
print(df_main.tail())
print(df_main.shape)

df_main.to_csv(write + 'day_transition1.csv')
