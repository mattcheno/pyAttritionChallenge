#! python3
'''

'''

# imports
import pandas as pd
import numpy as np
from variablez import Variablez

# declarations
miVarz = Variablez()

df = pd.read_csv(miVarz.inFileString,
                 dtype='category',
                 converters=miVarz.inDFIntCols)

print(df.head(5))
print(df.describe())
print(df.dtypes())
'''
g = df.columns.to_series().groupby(df.dtypes).groups
print(g)
'''
