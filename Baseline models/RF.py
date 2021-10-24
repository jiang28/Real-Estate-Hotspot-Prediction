import sklearn.gaussian_process as gp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn import metrics 
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, DotProduct
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


#col_names = ['Median Gross Rent(monthly)','Total Household Income(yearly)','Total population', 'Transportation To Work','Wage','Health Insurance Coverage',  'Employment Status', 'Bedrooms', 'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 'Monthly Housing Cost', 'Value Increase Index(17-18)']


# load dataset
#df = pd.read_csv("realestate_data_all_tracts_2017_update_minmax.csv", header=None, names=col_names)
#df = pd.read_csv("realestate_data_all_county_minmax_2017.csv", header=None, names=col_names)
df = pd.read_csv('data_census_hotspot_1.csv')
#for col in df.columns:
    #print(col)


#df = df.astype(str)

df = df.apply(LabelEncoder().fit_transform)

#feature_cols = ['Median Gross Rent(monthly)','Total Household Income(yearly)','Total population', 'Transportation To Work','Wage','Health Insurance Coverage',  'Employment Status', 'Bedrooms', 'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 'Monthly Housing Cost']
#X = df[feature_cols]      # Features
X = df.loc[:, df.columns != 'hotspot Index']
y = df["hotspot Index"]           # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

clf = RandomForestClassifier(n_jobs=2, random_state=0)

clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
#print(roc_auc_score(y_test, clf.predict(X_test)))