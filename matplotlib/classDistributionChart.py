import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')
sns.countplot(x='diagnosis', data=data)

plt.title('Class Distribution')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.show()