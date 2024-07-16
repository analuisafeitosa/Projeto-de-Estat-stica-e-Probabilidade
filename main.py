import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from acessoaobd import acessoaobd

data = acessoaobd()

df = pd.DataFrame(data, columns=['Latência'])

print(df.head())

media = df['Latência'].mean()
mediana = df['Latência'].median()
moda = df['Latência'].mode()[0]

variancia = df['Latência'].var()
desvio_padrao = df['Latência'].std()
quartis = df['Latência'].quantile([0.25, 0.5, 0.75])

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Quartis: \n{quartis}")

plt.figure(figsize=(10, 6))
sns.histplot(df['Latência'], bins=30, kde=True)
plt.title('Histograma da Latência')
plt.xlabel('Latência (ms)')
plt.ylabel('Frequência')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(df['Latência'])
plt.title('Boxplot da Latência')
plt.xlabel('Latência (ms)')
plt.show()