#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 05:37:44 2018
code to create correlation between jobs and study
@author: zoro
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
read = '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/month2/'
write= '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/'


def add_sector(df):
    df['Sector']=df['normTitleCategory']
    df['Sector'].replace(['sales','management','marketing','finance', 'hr','project','hospitality'], 
                          'Management',inplace=True)
    df['Sector'].replace(['customer', 'service', 'protective','personal'], 
                          'CustomerService',inplace=True)
    df['Sector'].replace(['admin', 'techsoftware','engcivil','techinfo','techhelp','engelectric',
                     'engid', 'engmech','engchem','tech'], 
                          'Engineering',inplace=True)
    df['Sector'].replace(['military','agriculture', 'mining', 'aviation'], 
                          'Government',inplace=True)
    df['Sector'].replace(['care','mednurse','pharmacy','medtech','sanitation','meddr',
                      'childcare','therapy','medinfo','meddental'], 
                          'HealthCare/Nutition',inplace=True)
    df['Sector'].replace(['manufacturing', 'retail','warehouse','install','construction','realestate'], 
                          'Industry',inplace=True)
    df['Sector'].replace(['insurance','legal','accounting'], 
                          'FinancialServices',inplace=True)
    df['Sector'].replace(['arts','media', 'veterinary'], 
                          'SocialServices',inplace=True)
    df['Sector'].replace(['uncategorized','food'], 
                          'Other',inplace=True)
    df['Sector'].replace(['transport','driver'], 
                          'Transport',inplace=True)
    df['Sector'].replace(['math', 'education','sports','science', 'arch','socialscience'], 
                          'Education',inplace=True)
    return df


def make_salary_label(df1):
    df11 = df1[df1.estimatedSalary<26000]
    df12 = df1[df1.estimatedSalary>=26000]
    df121 = df12[df12.estimatedSalary<60000]
    df122 = df12[df12.estimatedSalary>=60000]
    
    df11['salaryLabel'] = 0
    df121['salaryLabel'] = 1
    df122['salaryLabel'] = 2
    
    df2 = df11.append(df121, ignore_index=True)
    df2 = df2.append(df122, ignore_index=True)
    return df2

def create_miniframes(df):
    job_per_sector=df.groupby(['stateProvince','Sector'])['jobId'].nunique().sort_values().to_frame().reset_index()
    salary_per_sector=df.groupby(['stateProvince','Sector'])['estimatedSalary'].mean().sort_values().to_frame().reset_index()
    clicks_per_sector = df.groupby(['stateProvince','Sector'])['clicks'].sum().sort_values().to_frame().reset_index()
    localClicks_per_sector = df.groupby(['stateProvince','Sector'])['localClicks'].sum().sort_values().to_frame().reset_index()
    
    df2 = pd.merge(job_per_sector,salary_per_sector,on=['stateProvince','Sector'])
    df2 = pd.merge(df2,clicks_per_sector,on=['stateProvince','Sector'])
    df2 = pd.merge(df2,localClicks_per_sector,on=['stateProvince','Sector'])
    
    return df2

def create_mainframe(filename,datevalue):
    df = pd.read_csv(read+filename).drop(['Unnamed: 0'], axis=1) # read the file and drop first column
    df1 = df[df.educationRequirements.notnull()]
    df1 = add_sector(df1)
    EdSal = make_salary_label(df1)
    
    
    NoEd = EdSal[EdSal.educationRequirements == 'None']
    HSEd = EdSal[EdSal.educationRequirements == 'High School']
    HiEd = EdSal[EdSal.educationRequirements == 'Higher Education']
    
    NoEd_LowSal = NoEd[NoEd.salaryLabel == 0]
    NoEd_MedSal = NoEd[NoEd.salaryLabel == 1]
    NoEd_HiSal = NoEd[NoEd.salaryLabel == 2]
    HSEd_LowSal = HSEd[HSEd.salaryLabel == 0]
    HSEd_MedSal = HSEd[HSEd.salaryLabel == 1]
    HSEd_HiSal = HSEd[HSEd.salaryLabel == 2]
    HiEd_LowSal = HiEd[HiEd.salaryLabel == 0]
    HiEd_MedSal = HiEd[HiEd.salaryLabel == 1]
    HiEd_HiSal = HiEd[HiEd.salaryLabel == 2]
    
    df2 = create_miniframes(NoEd_LowSal)
    df2.columns = ['stateProvince','Sector','Jobs_NoEd_LowSal','estimatedSalary_NoEd_LowSal','clicks_NoEd_LowSal','localClicks_NoEd_LowSal']
    
    df3 = create_miniframes(NoEd_MedSal)
    df3.columns = ['stateProvince','Sector','Jobs_NoEd_MedSal','estimatedSalary_NoEd_MedSal','clicks_NoEd_MedSal','localClicks_NoEd_MedSal']
    
    df4 = create_miniframes(NoEd_HiSal)
    df4.columns = ['stateProvince','Sector','Jobs_NoEd_HiSal','estimatedSalary_NoEd_HiSal','clicks_NoEd_HiSal','localClicks_NoEd_HiSal']
    
    df5 = create_miniframes(HSEd_LowSal)
    df5.columns = ['stateProvince','Sector','Jobs_HSEd_LowSal','estimatedSalary_HSEd_LowSal','clicks_HSEd_LowSal','localClicks_HSEd_LowSal']
    
    df6 = create_miniframes(HSEd_MedSal)
    df6.columns = ['stateProvince','Sector','Jobs_HSEd_MedSal','estimatedSalary_HSEd_MedSal','clicks_HSEd_MedSal','localClicks_HSEd_MedSal']
    
    df7 = create_miniframes(HSEd_HiSal)
    df7.columns = ['stateProvince','Sector','Jobs_HSEd_HiSal','estimatedSalary_HSEd_HiSal','clicks_HSEd_HiSal','localClicks_HSEd_HiSal']
    
    df8 = create_miniframes(HiEd_LowSal)
    df8.columns = ['stateProvince','Sector','Jobs_HiEd_LowSal','estimatedSalary_HiEd_LowSal','clicks_HiEd_LowSal','localClicks_HiEd_LowSal']
    
    df9 = create_miniframes(HiEd_MedSal)
    df9.columns = ['stateProvince','Sector','Jobs_HiEd_MedSal','estimatedSalary_HiEd_MedSal','clicks_HiEd_MedSal','localClicks_HiEd_MedSal']
    
    df10 = create_miniframes(HiEd_HiSal)
    df10.columns = ['stateProvince','Sector','Jobs_HiEd_HiSal','estimatedSalary_HiEd_HiSal','clicks_HiEd_HiSal','localClicks_HiEd_HiSal']
    
    
    dfm = pd.merge(df2,df3,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df4,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df5,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df6,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df7,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df8,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df9,on=['stateProvince','Sector'])
    dfm = pd.merge(dfm,df10,on=['stateProvince','Sector'])
    
    dfm['date'] = datevalue

    cols = dfm.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    dfm = dfm[cols]
    
    return dfm


dfm = create_mainframe('nov16.csv','2016-11')

list1 = ['dec16.csv','jan17.csv','feb17.csv','mar17.csv','apr17.csv','may17.csv','jun17.csv','jul17.csv','aug17.csv','sep17.csv','oct17.csv','nov17.csv']

list2 = ['2016-12','2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11']

for i in range(len(list1)):
    print('writing from files : ' + list1[i])
    df3 = create_mainframe(list1[i],list2[i])
    dfm = dfm.append(df3, ignore_index=True)

print(dfm.shape)
dfm.to_csv(write + 'sector-education-salary.csv')
    
    
    