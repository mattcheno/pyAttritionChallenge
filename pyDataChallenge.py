#! python3
'''

'''

''' imports '''
import pandas as pd #Pandas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sys
from variablez import Variablez
miVarz = Variablez()

''' read csv '''
df = pd.read_csv(miVarz.inFileString,
	dtype='object')

''' convert columns to integers and categories ''' 
df['Attrition'] = df['Attrition'].map(miVarz.inYesNoBoo)
df[miVarz.inDFCatCols] = df[miVarz.inDFCatCols].apply(pd.Categorical)
df[miVarz.inDFIntCols] = df[miVarz.inDFIntCols].apply(pd.to_numeric)

''' print some stats to check that everything is working '''
print(df.head(5))
print(df.describe())
#print(df.columns.to_series().groupby(df.dtypes).groups)

''' ===== Playing around ===== 
y = df['Attrition']
X = df[['MonthlyIncome', 'TotalWorkingYears']]

X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

print(est.summary())
'''
