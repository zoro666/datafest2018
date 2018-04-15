#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:05:19 2018
this is a python code to select data from each month file
@author: zoro
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
read = '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/month2/'
filename = 'nov16.csv'

def series_toframe(frame):
    f = frame.to_frame()
    f = f.reset_index()
    return f


def create_main_dataframe(filename,datevalue):
    df = pd.read_csv(read+filename).drop(['Unnamed: 0'], axis=1) # read the file and drop first column
    
    Company_per_state = df.groupby('stateProvince')['companyId'].nunique().sort_values()
    Job_per_state = df.groupby('stateProvince')['jobId'].nunique().sort_values()
    estimated_salary = df.groupby('stateProvince')['estimatedSalary'].mean().sort_values()
    min_estimated_salary = df.groupby('stateProvince')['estimatedSalary'].min().sort_values()
    max_estimated_salary = df.groupby('stateProvince')['estimatedSalary'].max().sort_values()

    cps = series_toframe(Company_per_state)
    jps = series_toframe(Job_per_state)
    es = series_toframe(estimated_salary)
    mines = series_toframe(min_estimated_salary)
    maxes = series_toframe(max_estimated_salary)
    
    df2 = pd.merge(cps,jps,on='stateProvince')
    df2 = pd.merge(df2,es,on='stateProvince')
    df2 = pd.merge(df2,mines,on='stateProvince')
    df2 = pd.merge(df2,maxes,on='stateProvince')
    
    
    mean_estimatedSalary_y = df2['estimatedSalary_y'].mean(skipna=True)
    df2=df2.replace({'estimatedSalary_y': {0: mean_estimatedSalary_y}}) 
    
    df2.columns = ['stateProvince','companyId','jobId','mean_estimatedSalary','min_estimatedSalary','max_estimatedSalary']
    
    dateSelect = datevalue
    df2['date'] = dateSelect
    cols = df2.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df2 = df2[cols]
    
    total_clicks = df.groupby('stateProvince')['clicks'].sum().sort_values()
    tc = series_toframe(total_clicks)


    total_local_clicks = df.groupby('stateProvince')['localClicks'].sum().sort_values()
    tlc = series_toframe(total_local_clicks)
    
    df2 = pd.merge(df2,tc,on='stateProvince')
    df2 = pd.merge(df2,tlc,on='stateProvince')
    
    return df2


df = create_main_dataframe('nov16.csv',"2016-11")

print(df.head())
print(df.shape)
print(df.min_estimatedSalary)
