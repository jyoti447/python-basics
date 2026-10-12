
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/jyoti./Downloads/breast_cancer_cleaned.csv')

data = data.drop(columns=['id'], errors='ignore')
numeric = data.select_dtypes(include='number')

if 'diagnosis' in data.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=data, x='diagnosis')
    plt.title('Class Distribution')
    plt.savefig('class_distribution.png')

numeric.hist(figsize=(15, 12), bins=20)
plt.suptitle('Feature Histograms')
plt.tight_layout()
plt.savefig('feature_histograms.png')

plt.figure(figsize=(10, 8))
sns.heatmap(numeric.corr(), cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_matrix.png')

features = [
    col for col in
    ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean']
    if col in numeric.columns
]

if features:
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=numeric[features], orient='h')
    plt.title('Box Plot')
    plt.tight_layout()
    plt.savefig('box_plot.png')

if len(features) >= 2:
    pair_data = data[features].copy()

    if 'diagnosis' in data.columns:
        pair_data['diagnosis'] = data['diagnosis'].astype(str)
        g = sns.pairplot(pair_data, vars=features, hue='diagnosis')
    else:
        g = sns.pairplot(pair_data, vars=features)

    g.figure.suptitle('Pair Plot', y=1.02)
    g.savefig('pair_plot.png')

plt.show()

print("All visualizations generated successfully!")
