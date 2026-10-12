
import pandas as pd

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')

data.columns = data.columns.str.strip()

data = data.loc[:, ~data.columns.str.contains('^Unnamed', case=False)]

data = data.dropna(axis=1, how='all')

data = data.drop_duplicates()

for col in data.select_dtypes(include='number').columns:
    data[col] = data[col].fillna(data[col].median())

for col in data.select_dtypes(exclude='number').columns:
    if data[col].isnull().any():
        mode = data[col].mode()
        if not mode.empty:
            data[col] = data[col].fillna(mode[0])

print("Cleaned Dataset:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDataset Shape:")
print(data.shape)

data.to_csv('/Users/jyoti./Downloads/breast_cancer_cleaned.csv',
            index=False)

print("\nCleaned data saved successfully!")
