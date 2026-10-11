
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/jyoti./Downloads/breast cancer.csv')

features = ['radius_mean', 'texture_mean',
            'perimeter_mean', 'area_mean']

sns.pairplot(data, vars=features, hue='diagnosis')

plt.savefig('pair_plot.png')
plt.show()
