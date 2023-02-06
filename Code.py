import pandas as pd
df = pd.read_csv (r'penguins.csv')
print (df)
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

plt.show()
