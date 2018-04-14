#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:32:21 2018
This file contains code to perform file cleaning based on month files
@author: zoro
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
read = '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/'
write= '/home/zoro/Desktop/datafest2018/DataFest-Dataset-2018.csv/output/'
filename = 'US_companies.csv'

df = pd.read_csv(read+filename).drop(['Unnamed: 0'], axis=1) # read the file and drop first column

df['label'] = df.groupby(['companyId', 'jobId']).ngroup() # create group label based on companyid and JObid

df.groupby('stateProvince')['companyId'].nunique().sort_values().to_csv(write+'companies_'+filename)  # no of unique companies per state per month

df.groupby('stateProvince')['jobId'].nunique().sort_values().to_csv(write+'jobs_'+filename)  # no of unique jobs per state per month
#%%
df['industrynew'] = df['industry']
#%%
df['industrynew'].replace(['HEALTH_CARE','HEALTH_CARE,INDUSTRIAL_MANUFACTURING',
                           'HEALTH_CARE,ORGANIZATION','BANKS_AND_FINANCIAL_SERVICES,HEALTH_CARE','INDUSTRIAL_MANUFACTURING,PHARMACEUTICALS','FOOD_AND_BEVERAGES,HEALTH_CARE', 'HEALTH_CARE,PHARMACEUTICALS', 'HEALTH_CARE,INDUSTRIAL_MANUFACTURING,PHARMACEUTICALS', 'HEALTH_CARE,BANKS_AND_FINANCIAL_SERVICES','HEALTH_CARE,RETAIL'], 
                          'Healthcare',inplace=True)

#%%
df['industrynew'].replace(['ORGANIZATION'], 'Other Services',inplace = True)
#%%
df['industrynew'].replace(['AEROSPACE_AND_DEFENSE,HEALTH_CARE',
                                            'AEROSPACE_AND_DEFENSE','GOVERNMENT',
                                            'GOVERNMENT,HEALTH_CARE',
                                             'AEROSPACE_AND_DEFENSE,INDUSTRIAL_MANUFACTURING',
                                             'CONSULTING_AND_BUSINESS_SERVICES,GOVERNMENT',
                                            'AEROSPACE_AND_DEFENSE,HUMAN_RESOURCES_AND_STAFFING','BANKS_AND_FINANCIAL_SERVICES,GOVERNMENT', 'AEROSPACE_AND_DEFENSE,TRANSPORT_AND_FREIGHT',  'AEROSPACE_AND_DEFENSE,CONSUMER_GOODS_AND_SERVICES', 'AEROSPACE_AND_DEFENSE,GOVERNMENT', 'ENERGY_AND_UTILITIES,GOVERNMENT', 'AEROSPACE_AND_DEFENSE,CONSULTING_AND_BUSINESS_SERVICES', 'AEROSPACE_AND_DEFENSE,BANKS_AND_FINANCIAL_SERVICES', 'INDUSTRIAL_MANUFACTURING,AEROSPACE_AND_DEFENSE', 'HEALTH_CARE,AEROSPACE_AND_DEFENSE', 'CONSULTING_AND_BUSINESS_SERVICES,AEROSPACE_AND_DEFENSE','CONSTRUCTION,GOVERNMENT', 'GOVERNMENT,INTERNET_AND_SOFTWARE,ORGANIZATION','TRANSPORT_AND_FREIGHT,AEROSPACE_AND_DEFENSE'
                                            ], 'Government',inplace = True)
#%%
df['industrynew'].replace(['RESTAURANTS_TRAVEL_AND_LEISURE',
                                            'AUTO,RESTAURANTS_TRAVEL_AND_LEISURE','FOOD_AND_BEVERAGES,RESTAURANTS_TRAVEL_AND_LEISURE', 'HEALTH_CARE,RESTAURANTS_TRAVEL_AND_LEISURE', 'CONSULTING_AND_BUSINESS_SERVICES,RESTAURANTS_TRAVEL_AND_LEISURE', 'BANKS_AND_FINANCIAL_SERVICES,RESTAURANTS_TRAVEL_AND_LEISURE', 'MEDIA_NEWS_AND_PUBLISHING,RESTAURANTS_TRAVEL_AND_LEISURE', 'CONSUMER_GOODS_AND_SERVICES,RESTAURANTS_TRAVEL_AND_LEISURE', 'RESTAURANTS_TRAVEL_AND_LEISURE,AUTO','RESTAURANTS_TRAVEL_AND_LEISURE,RETAIL', 'INTERNET_AND_SOFTWARE,RESTAURANTS_TRAVEL_AND_LEISURE','FOOD_AND_BEVERAGES,BANKS_AND_FINANCIAL_SERVICES'],
                                           'Hospitality',inplace = True)
#%%
df['industrynew'].replace(['EDUCATION_AND_SCHOOLS','CONSULTING_AND_BUSINESS_SERVICES',
                                            'EDUCATION_AND_SCHOOLS,HEALTH_CARE','CONSUMER_GOODS_AND_SERVICES,EDUCATION_AND_SCHOOLS', 'EDUCATION_AND_SCHOOLS,HUMAN_RESOURCES_AND_STAFFING', 'EDUCATION_AND_SCHOOLS,MEDIA_NEWS_AND_PUBLISHING', 'HEALTH_CARE,MEDIA_NEWS_AND_PUBLISHING', 'EDUCATION_AND_SCHOOLS,INTERNET_AND_SOFTWARE'], 
                                           'Education',inplace = True)

#%%
df['industrynew'].replace(['CONSULTING_AND_BUSINESS_SERVICES,HUMAN_RESOURCES_AND_STAFFING',
                   'HEALTH_CARE,HUMAN_RESOURCES_AND_STAFFING',
                  'CONSULTING_AND_BUSINESS_SERVICES,HEALTH_CARE',
                 'HUMAN_RESOURCES_AND_STAFFING',
                   'CONSULTING_AND_BUSINESS_SERVICES,INTERNET_AND_SOFTWARE',
                   'CONSULTING_AND_BUSINESS_SERVICES,RETAIL',
                   'HUMAN_RESOURCES_AND_STAFFING,INTERNET_AND_SOFTWARE',
                   'CONSULTING_AND_BUSINESS_SERVICES,TELECOMMUNICATIONS','CONSULTING_AND_BUSINESS_SERVICES,INSURANCE','COMPUTERS_AND_ELECTRONICS,CONSULTING_AND_BUSINESS_SERVICES','CONSULTING_AND_BUSINESS_SERVICES,INTERNET_AND_SOFTWARE,MEDIA_NEWS_AND_PUBLISHING', 'BANKS_AND_FINANCIAL_SERVICES,MEDIA_NEWS_AND_PUBLISHING,RETAIL', 'CONSULTING_AND_BUSINESS_SERVICES,MEDIA_NEWS_AND_PUBLISHING', 'CONSULTING_AND_BUSINESS_SERVICES,INDUSTRIAL_MANUFACTURING', 'AUTO,CONSULTING_AND_BUSINESS_SERVICES', 'CONSULTING_AND_BUSINESS_SERVICES,ORGANIZATION', 'AGRICULTURE_AND_EXTRACTION,CONSULTING_AND_BUSINESS_SERVICES'
                  ], 'Business',inplace = True)
#%%
df['industrynew'].replace(['BANKS_AND_FINANCIAL_SERVICES,INSURANCE',
                                            'BANKS_AND_FINANCIAL_SERVICES','INSURANCE',
                               'BANKS_AND_FINANCIAL_SERVICES,REAL_ESTATE',
                               'AUTO,BANKS_AND_FINANCIAL_SERVICES','INDUSTRIAL_MANUFACTURING,INSURANCE',
                               'INSURANCE,MEDIA_NEWS_AND_PUBLISHING','HEALTH_CARE,INSURANCE',
                               'BANKS_AND_FINANCIAL_SERVICES,ENERGY_AND_UTILITIES',
                                 'BANKS_AND_FINANCIAL_SERVICES,CONSTRUCTION',
                               'BANKS_AND_FINANCIAL_SERVICES,CONSULTING_AND_BUSINESS_SERVICES'  , 'BANKS_AND_FINANCIAL_SERVICES,HUMAN_RESOURCES_AND_STAFFING', 'CONSULTING_AND_BUSINESS_SERVICES,BANKS_AND_FINANCIAL_SERVICES', 'ENERGY_AND_UTILITIES,BANKS_AND_FINANCIAL_SERVICES', 'INSURANCE,BANKS_AND_FINANCIAL_SERVICES','GOVERNMENT,BANKS_AND_FINANCIAL_SERVICES', 'REAL_ESTATE,BANKS_AND_FINANCIAL_SERVICES', 'BANKS_AND_FINANCIAL_SERVICES,CONSULTING_AND_BUSINESS_SERVICES,HUMAN_RESOURCES_AND_STAFFING','BANKS_AND_FINANCIAL_SERVICES,ORGANIZATION','RETAIL,BANKS_AND_FINANCIAL_SERVICES'
                              ], 'Financial Activities',inplace = True)
#%%
df['industrynew'].replace(['INTERNET_AND_SOFTWARE','COMPUTERS_AND_ELECTRONICS',
                                            'TELECOMMUNICATIONS',
                                              'MEDIA_NEWS_AND_PUBLISHING',
                                            'INTERNET_AND_SOFTWARE,MEDIA_NEWS_AND_PUBLISHING,TELECOMMUNICATIONS',
                                              'INTERNET_AND_SOFTWARE,MEDIA_NEWS_AND_PUBLISHING',
                                            'COMPUTERS_AND_ELECTRONICS,ENERGY_AND_UTILITIES','COMPUTERS_AND_ELECTRONICS,INTERNET_AND_SOFTWARE','COMPUTERS_AND_ELECTRONICS,INDUSTRIAL_MANUFACTURING', 'INDUSTRIAL_MANUFACTURING,INTERNET_AND_SOFTWARE', 'RETAIL,TELECOMMUNICATIONS' 'INTERNET_AND_SOFTWARE,TELECOMMUNICATIONS', 'CONSULTING_AND_BUSINESS_SERVICES,INDUSTRIAL_MANUFACTURING,INTERNET_AND_SOFTWARE','RETAIL,COMPUTERS_AND_ELECTRONICS' 'CONSULTING_AND_BUSINESS_SERVICES,COMPUTERS_AND_ELECTRONICS','MEDIA_NEWS_AND_PUBLISHING,AUTO','RETAIL,TELECOMMUNICATIONS','INTERNET_AND_SOFTWARE,TELECOMMUNICATIONS','CONSULTING_AND_BUSINESS_SERVICES,COMPUTERS_AND_ELECTRONICS','RETAIL,COMPUTERS_AND_ELECTRONICS'], 
                                           'Technology',inplace = True)
#%%
df['industrynew'].replace(['TRANSPORT_AND_FREIGHT','TRANSPORT_AND_FREIGHT',
                                         'CONSULTING_AND_BUSINESS_SERVICES,TRANSPORT_AND_FREIGHT',
                                         'INDUSTRIAL_MANUFACTURING,TRANSPORT_AND_FREIGHT',
                                            'AUTO,TRANSPORT_AND_FREIGHT',
                                         'FOOD_AND_BEVERAGES,TRANSPORT_AND_FREIGHT','AUTO,INDUSTRIAL_MANUFACTURING','CONSUMER_GOODS_AND_SERVICES,TRANSPORT_AND_FREIGHT', 'BANKS_AND_FINANCIAL_SERVICES,CONSUMER_GOODS_AND_SERVICES', 'ORGANIZATION,TRANSPORT_AND_FREIGHT', 'AGRICULTURE_AND_EXTRACTION,TRANSPORT_AND_FREIGHT', 'ENERGY_AND_UTILITIES,TRANSPORT_AND_FREIGHT', 'RESTAURANTS_TRAVEL_AND_LEISURE,TRANSPORT_AND_FREIGHT', 'HEALTH_CARE,TRANSPORT_AND_FREIGHT','INDUSTRIAL_MANUFACTURING,AUTO', 'TRANSPORT_AND_FREIGHT,AGRICULTURE_AND_EXTRACTION','TRANSPORT_AND_FREIGHT,AUTO','INTERNET_AND_SOFTWARE,TRANSPORT_AND_FREIGHT'], 
                                           'Transportation and Warehousing',inplace = True)
#%%
df['industrynew'].replace(['FOOD_AND_BEVERAGES','RETAIL','CONSUMER_GOODS_AND_SERVICES','CONSTRUCTION,CONSUMER_GOODS_AND_SERVICES',
                        'AUTO','INDUSTRIAL_MANUFACTURING','CONSUMER_GOODS_AND_SERVICES,FOOD_AND_BEVERAGES',
                        'CONSTRUCTION,INDUSTRIAL_MANUFACTURING',
                       'CONSUMER_GOODS_AND_SERVICES,INDUSTRIAL_MANUFACTURING','PHARMACEUTICALS',
                        'CONSUMER_GOODS_AND_SERVICES,RETAIL',
                        'COMPUTERS_AND_ELECTRONICS,RETAIL','INDUSTRIAL_MANUFACTURING,RETAIL',
                        'INDUSTRIAL_MANUFACTURING,TELECOMMUNICATIONS','FOOD_AND_BEVERAGES,INDUSTRIAL_MANUFACTURING','AGRICULTURE_AND_EXTRACTION,RETAIL',  'BANKS_AND_FINANCIAL_SERVICES,FOOD_AND_BEVERAGES', 'CONSUMER_GOODS_AND_SERVICES,FOOD_AND_BEVERAGES,INTERNET_AND_SOFTWARE,RETAIL','CONSUMER_GOODS_AND_SERVICES,INTERNET_AND_SOFTWARE,RETAIL','AUTO,RETAIL', 'HUMAN_RESOURCES_AND_STAFFING,INDUSTRIAL_MANUFACTURING','RETAIL,AUTO'
                       ], 'Manufacturing_and_Retail',inplace = True)
#%%
df['industrynew'].replace(['CONSTRUCTION','REAL_ESTATE','CONSTRUCTION,CONSULTING_AND_BUSINESS_SERVICES,REAL_ESTATE',
                       'CONSTRUCTION,REAL_ESTATE','CONSTRUCTION,ENERGY_AND_UTILITIES',
                       'CONSTRUCTION,CONSULTING_AND_BUSINESS_SERVICES','CONSTRUCTION,HUMAN_RESOURCES_AND_STAFFING', 'HUMAN_RESOURCES_AND_STAFFING,REAL_ESTATE', 'CONSULTING_AND_BUSINESS_SERVICES,REAL_ESTATE', 'CONSTRUCTION,CONSUMER_GOODS_AND_SERVICES,REAL_ESTATE','CONSULTING_AND_BUSINESS_SERVICES,REAL_ESTATE,CONSTRUCTION', 'INDUSTRIAL_MANUFACTURING,CONSTRUCTION', 'CONSUMER_GOODS_AND_SERVICES,CONSTRUCTION','CONSTRUCTION,MEDIA_NEWS_AND_PUBLISHING','AUTO,REAL_ESTATE','REAL_ESTATE,CONSTRUCTION','REAL_ESTATE,AUTO'], 'construction/real_estate',inplace = True)
#%%
df['industrynew'].replace(['ENERGY_AND_UTILITIES','ENERGY_AND_UTILITIES,INDUSTRIAL_MANUFACTURING',
                    'ENERGY_AND_UTILITIES,PHARMACEUTICALS','ENERGY_AND_UTILITIES,REAL_ESTATE', 'AUTO,ENERGY_AND_UTILITIES','ENERGY_AND_UTILITIES,HUMAN_RESOURCES_AND_STAFFING'], 'Utilities',inplace = True)

#%%
df['industrynew'].replace(['AGRICULTURE_AND_EXTRACTION','AGRICULTURE_AND_EXTRACTION,CONSUMER_GOODS_AND_SERVICES','AGRICULTURE_AND_EXTRACTION,ENERGY_AND_UTILITIES','AGRICULTURE_AND_EXTRACTION,FOOD_AND_BEVERAGES', 'AGRICULTURE_AND_EXTRACTION,INDUSTRIAL_MANUFACTURING', 'INDUSTRIAL_MANUFACTURING,AGRICULTURE_AND_EXTRACTION', 'FOOD_AND_BEVERAGES,AGRICULTURE_AND_EXTRACTION', 'CONSUMER_GOODS_AND_SERVICES,AGRICULTURE_AND_EXTRACTION','ENERGY_AND_UTILITIES,AGRICULTURE_AND_EXTRACTION'], 'Agriculture',inplace = True)
#%%
print(df.industry.nunique())
print(df.industrynew.nunique())
print(df.stateProvince.nunique())
print(df.industrynew.isnull().sum())
#%%
print(df.industrynew.unique())


#%%
df.to_csv(write+'new_'+filename)