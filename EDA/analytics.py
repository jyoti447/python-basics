import pandas as pd
data = pd.read_csv('/Users/jyoti./Downloads/breast_cancer_cleaned.csv')
print("Dataset Shape:")
print(data.shape)

print("\nStatistical Summary:")
print(data.describe())

print("\nMean:")
print(data.mean(numeric_only=True))

print("\nMedian:")
print(data.median(numeric_only=True))

print("\nStandard Deviation:")
print(data.std(numeric_only=True))

print("\nMinimum Values:")
print(data.min(numeric_only=True))

print("\nMaximum Values:")
print(data.max(numeric_only=True))

if 'diagnosis' in data.columns:
    print("\nClass Distribution:")
    print(data['diagnosis'].value_counts())
