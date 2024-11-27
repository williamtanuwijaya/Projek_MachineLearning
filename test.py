import pandas as pd
import numpy as np
from scipy.stats import entropy
df = pd.read_csv('weather_classification_data_clear.csv')
print(df.head())

y = df['Weather Type']

print(y.head())

values, counts = np.unique(y, return_counts=True)

probabilities = counts / len(y)

entropy_value = entropy(probabilities, base=2)
print('Entropi H(Y): ', entropy_value)