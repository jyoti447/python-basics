
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')


numeric_data = data.select_dtypes(include='number')


corr = numeric_data.corr()


print(corr)


plt.figure(figsize=(10, 8))
sns.heatmap(corr, cmap='coolwarm', annot=True, fmt='.2f')

plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
