import requests, pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree
from sklearn.model_selection import train_test_split
import addfips
import numpy as np
from pandas import DataFrame



#load csv data
fields = ['Name','Median Gross Rent(monthly)','Total Household Income(yearly)','Total population', 'Transportation To Work','Wage','Health Insurance Coverage',  'Employment Status', 'Bedrooms', 'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 
'Monthly Housing Cost', 'Median Value 18']


df = pd.read_csv('realestate_data_all_tracts_2017.csv', skipinitialspace=True, usecols=fields)
count_zero = 0
count_one =1

datalist =[]
for index, row in df.iterrows():
    past = row['Median Value']
    current = row['Median Value 18']


    if ((current-past)/current >.08):
        datalist.append(1.0) 
        count_one +=1
    else:
        datalist.append(0.0) 
        count_zero +=1


df['Value Increase Index(17-18)'] = datalist
print("number of one: ",count_one)
print("number of zero: ",count_zero)

df.to_csv('realestate_data_all_tracts_2017_update.csv', encoding='utf-8', index=False)