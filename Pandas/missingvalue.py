import numpy as np 
import pandas as pd
data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')
df = data.isnull().sum().head(5)
print(df)