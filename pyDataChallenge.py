#! python3
'''

'''

''' imports '''
import pandas as pd #Pandas
import numpy as np #Numpy
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sys
import pprint
from variablez import Variablez
miVarz = Variablez()

''' read csv '''
df = pd.read_csv(miVarz.inFileString,
	dtype='object')

''' convert columns to integers and categories ''' 
df['Attrition'] = df['Attrition'].map(miVarz.inYesNoBoo)
df[miVarz.inDFCatCols] = df[miVarz.inDFCatCols].apply(pd.Categorical)
df[miVarz.inDFIntCols] = df[miVarz.inDFIntCols].apply(pd.to_numeric)

''' print some stats to check that everything is working 
print(df.head(5))
print(df.describe())
print(df.columns.to_series().groupby(df.dtypes).groups) '''

''' ===== Trying some dummy variables ===== 
print(df.columns)
dummy = pd.get_dummies(df['BusinessTravel'], prefix='Bt')
print(dummy)
'''

''' ===== Begin Building Model ===== '''
data = df[miVarz.inDFIntCols]
pprint.pprint(miVarz.inDFIntCols)

''' ===== Loop through Categoricals, make dummy variables, and add 
          to the model                                                ===== '''
for col in miVarz.inDFCatCols:
	dummy = pd.get_dummies(df[col], prefix=col)
	dName = col + '_2'
	data = data.join(dummy.ix[:, dName:])
	print(col)

print(data.describe())
