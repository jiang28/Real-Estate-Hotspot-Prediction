#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import requests, pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json


# In[2]:


#Set variables
with open('census_key.txt') as key:
    api_key=key.read().strip()
year='2018'
dsource='acs'
dname='acs5'
table = 'profile'

#"B25031_001E label": "Estimate!!Median gross rent!!Total",
# B19001_001E: HOUSEHOLD INCOME IN THE PAST 12 MONTHS
# B01003_001E: Total population
# B08141_016E MEANS OF TRANSPORTATION TO WORK BY VEHICLES AVAILABLE
# B19052_002E WAGE OR SALARY INCOME IN THE PAST 12 MONTHS FOR HOUSEHOLDS
# C27021_001E	Estimate!!Total	HEALTH INSURANCE COVERAGE STATUS BY LIVING ARRANGEMENT
cols='B25031_001E,B19001_001E,B01003_001E,B08141_016E,B19052_002E,C27021_001E'
state='36'
county = '*'
#county='005,047,061,081,085'


# In[3]:


base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}/'
base_url


# In[4]:


data_url = f'{base_url}?get=NAME,{cols}&for=county:{county}&in=state:{state}&key={api_key}'
data_url


# In[5]:


#Retrieve Data
response=requests.get(data_url)
print(response.status_code)
print(response.text)


# In[13]:


data=response.json()
df=pd.DataFrame(data[1:], columns=data[0]).    rename(columns={"B25031_001E": "Median Gross Rent(month)", "B19001_001E":"Total Household Income(year)","B01003_001E":"Total population", 
                    'B08141_016E':'Transportation To Work', 'B19052_002E':'WAGE OR SALARY INCOME', 'C27021_001E':'HEALTH INSURANCE COVERAGE'})
df['fips']=df.state+df.county
df.set_index('fips',inplace=True)
df.drop(columns=['state','county'],inplace=True)

#df.to_csv('realestate_variables.csv', sep='\t', encoding='utf-8')
df.to_csv('realestate_variables.csv', encoding='utf-8', index=False)
df
#df = pd.DataFrame(scaler.fit_transform(df.values), columns=df.columns, index=df.index)



# In[14]:


scaler = MinMaxScaler()
df[['Median Gross Rent(month)','Total Household Income(year)','Total population', 'Transportation To Work','WAGE OR SALARY INCOME','HEALTH INSURANCE COVERAGE']] = scaler.fit_transform(df[['Median Gross Rent(month)', 'Total Household Income(year)',
'Total population','Transportation To Work','WAGE OR SALARY INCOME','HEALTH INSURANCE COVERAGE']])

#df=df.astype(dtype={'Median Gross Rent':'int64','Household':'int64','Total population':'int64'},inplace=True)
df


# In[ ]:





# In[ ]:




