import numpy as np 
import pandas as pd
data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')

#print("shape of data",data.shape)

#print("information of data",data.info())

print("dataset summary",data.describe())