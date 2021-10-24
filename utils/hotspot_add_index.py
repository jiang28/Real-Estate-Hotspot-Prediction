import requests, pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np
from pandas import DataFrame
import pickle



#load csv data
#fields = ['Name','Median Gross Rent(monthly)','Total Household Income(yearly)','Total population', 'Transportation To Work','Wage','Health Insurance Coverage',  'Employment Status', 'Bedrooms', 'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 
#'Monthly Housing Cost', 'Median Value 18']


df = pd.read_csv('data_census_inflation.csv')
count_zero = 0
count_one =0
count_two =0
count_three =0
count_four =0

indexlist = []


datalist =[]
index = 1
for index, row in df.iterrows():
    indexlist.append(index)
    index = index+1
    #if(row['Hotspot Index(17-18)'] ==2):
    #datalist.append(row['City']+', '+row['State'])

  
    past = row['Avg 17']
    current = row['Avg 18'] 

    if ((current-past)/current <.03):
        datalist.append(0.0) 
        count_zero +=1
    if ((current-past)/current >.030 and (current-past)/current <.05):
        datalist.append(1.0) 
        count_one +=1
    if ((current-past)/current >.05 and (current-past)/current <.070):
        datalist.append(2.0) 
        count_two +=1 
    if ((current-past)/current >.070 and (current-past)/current <.1):
        datalist.append(3.0) 
        count_three +=1 
    if ((current-past)/current >.1):
        datalist.append(4.0) 
        count_four +=1 


 

#df['unique county'] = indexlist
print("number of zero: ",count_zero)
print("number of one: ",count_one)
print("number of two: ",count_two)
print("number of three: ",count_three)
print("number of four: ",count_four)

"""

#print(pd.unique(df['Metro']))
a = df['Metro'].unique()
#b = df['CountyName'].unique()

b = pd.unique(df['Metro'])
#dict = {'county':b}

datalist = set(datalist)
print(*datalist, sep = "\n")
print(index)

with open("file.txt", "w") as f:
    for s in datalist:
        f.write(str(s) +"\n")

#dict = {'county':datalist}
#df = pd.DataFrame(dict)
#df.to_csv('county.csv')
"""

df["hotspot Index"] = datalist
df.to_csv('data_census_hotspot_3.csv', encoding='utf-8', index=False)