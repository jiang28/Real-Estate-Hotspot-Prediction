import requests, pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np
from pandas import DataFrame



#load csv data
#fields = ['Name','Median Gross Rent(monthly)','Total Household Income(yearly)','Total population', 'Transportation To Work','Wage','Health Insurance Coverage',  'Employment Status', 'Bedrooms', 'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 
#'Monthly Housing Cost', 'Median Value 18']


df = pd.read_csv('data_census_location.csv')
df2 = pd.read_csv('data_census_location.csv')
count_zero = 0
count_one =0
count_two =0

indexlist = []


datalist =[]
graph_index = 0
idx = 0
for index, row in df.iterrows():
    for index1, row1 in df2.iterrows():
        #index = index+1
        county1 = row['CountyName']
        county2 = row1['CountyName']
        metro1 = row['Metro']
        metro2 = row1['Metro']
        region1 = row['RegionID']
        region2 = row1['RegionID']
        state1 = row['State']
        state2 = row1['State']
        city1 = row['City']
        city2 = row1['City']
        graph_index = 0
        if(state1 == state2):
            graph_index = 1
        if(metro1 == metro2 and state1 == state2):
            graph_index = 2
        if(county1 == county2 and metro1 == metro2 and state1 == state2):
            graph_index = 3
        if(city1 == city2 and county1 == county2 and metro1 == metro2 and state1 == state2):
            graph_index = 4
        if(region1 == region2):
            graph_index = -1
        
            
        idx = idx+1
        datalist.append(graph_index)
        print(graph_index)
        print(idx)

print(datalist)
print("The length is: ", len(datalist))

f=open('matrix.txt','w')
for i in datalist:
    f.write(str(i)+'\n')

f.close()

"""     
    past = row['Avg 17']
    current = row['Avg 18'] 

    if ((current-past)/current <.045):
        datalist.append(0.0) 
        count_zero +=1
    if ((current-past)/current >.045 and (current-past)/current <.075):
        datalist.append(1.0) 
        count_one +=1
    if ((current-past)/current >.075):
        datalist.append(2.0) 
        count_two +=1 



    if ((current-past)/current >.06):
        datalist.append(1.0) 
        count_one +=1
    else:
        datalist.append(0.0) 
        count_zero +=1  """
 

#df['neighborhood Index'] = indexlist
#print("number of zero: ",count_zero)Index
#print("number of one: ",count_one)index
#print("number of two: ",count_two)

""" n_neighborhood = len(pd.unique(df['RegionName']))
n_county = len(pd.unique(df['CountyName']))
n_city = len(pd.unique(df['City']))
n_metro = len(pd.unique(df['Metro']))
n_state = len(pd.unique(df['State']))
n_RegionID = len(pd.unique(df['RegionID']))

print("neighborhood: ", n_neighborhood)
print("county: ", n_county)
print("city: ", n_city)
print("metro: ", n_metro)
print("state: ", n_state)
print("RegionID: ", n_RegionID) """



#df.to_csv('data_census_neighborhood_index.csv', encoding='utf-8', index=False)