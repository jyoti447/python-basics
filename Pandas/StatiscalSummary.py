import numpy as np
import pandas as pd

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')

print("Mean:")
print(data.mean(numeric_only=True))

print("\nMedian:")
print(data.median(numeric_only=True))

print("\nStandard Deviation:")
print(data.std(numeric_only=True))

print("\nStatistical Summary:")
print(data.describe())