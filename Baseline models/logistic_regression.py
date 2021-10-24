from sklearn.linear_model import LogisticRegression
from sklearn import metrics
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
from sklearn.metrics import roc_curve


col_names = ['Median Gross Rent(monthly)','Total Household Income(yearly)','Total population', 'Transportation To Work','Wage','Health Insurance Coverage',  'Employment Status', 'Bedrooms', 'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 'Monthly Housing Cost', 'Value Increase Index(17-18)']


# load dataset
# df = pd.read_csv("realestate_data_all_tracts_2017_update_minmax.csv", header=None, names=col_names)
# df = pd.read_csv("realestate_data_all_county_minmax_2017.csv", header=None, names=col_names)
df = pd.read_csv('data_census_hotspot_1.csv')


#df = df.astype(str)

df = df.apply(LabelEncoder().fit_transform)

#feature_cols = ['Median Gross Rent(monthly)','Total Household Income(yearly)', 'Transportation To Work','Wage',  'Total Contract Rent', 'Total Rent Asked', 'Total Gross Rent', 'Aggregate Gross Rent', 'Median Value',  'Total Price Asked', 'Selected Monthly Owner Costs', 'Monthly Housing Cost']
X = df.loc[:, df.columns != 'hotspot Index']
y = df["hotspot Index"]           # Target variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)


y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
print(classification_report(y_test, y_pred))
print(roc_auc_score(y_test, logreg.predict(X_test)))


""" #draw graph
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()  """