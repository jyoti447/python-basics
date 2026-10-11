
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')

features = data.select_dtypes(include='number')
features = features.drop(columns=['id'], errors='ignore')

plt.figure(figsize=(12, 6))
sns.boxplot(data=features, orient='v')

plt.title('Box Plot of Numerical Features')
plt.tight_layout()
plt.savefig('box_plot.png')
plt.show()
