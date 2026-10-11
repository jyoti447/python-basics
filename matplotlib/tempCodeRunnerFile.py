
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')


features = data.select_dtypes(include='number').drop(
    columns=['id'], errors='ignore'
)


features.hist(figsize=(15, 12), bins=20)

plt.suptitle('Feature Histograms')
plt.tight_layout()
plt.show()
