#! python3
'''

'''
print('Hey!')

''' imports '''
import pandas as pd
import numpy as np
from variablez import Variablez
miVarz = Variablez()

''' import csv '''
df = pd.read_csv(miVarz.inFileString,
	dtype='object')

''' print some stats to check that everything is working '''
print(df.head(5))
print(df.describe())
print(df.columns.to_series().groupby(df.dtypes).groups)


''' convert columns to integers and categories ''' 
df[miVarz.inDFCatCols] = df[miVarz.inDFCatCols].apply(pd.astype('category'))
df[miVarz.inDFIntCols] = df[miVarz.inDFIntCols].apply(pd.to_numeric)

print(df.columns.to_series().groupby(df.dtypes).groups)
