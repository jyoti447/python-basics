import pandas as pd

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')

data = data.drop_duplicates()

for col in data.select_dtypes(include='number').columns:
    data[col] = data[col].fillna(data[col].median())

data.to_csv('/Users/jyoti./Downloads/processed_data.csv', index=False)

print("Processed data saved successfully!")
