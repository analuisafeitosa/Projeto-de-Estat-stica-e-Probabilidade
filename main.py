import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

def acessoaobd():
    conn = sqlite3.connect('./db/IoT.db')
    cursor = conn.cursor()

    cursor.execute('SELECT value FROM data_values')
    data = cursor.fetchall()

    conn.close()

    return data

data = acessoaobd()

df = pd.DataFrame(data, columns=['Latência'])

print(df.head())

# verifica se é um número, oq não for recebe o nome de NaN
df['Latência'] = pd.to_numeric(df['Latência'], errors='coerce')

# remove os NaN
df = df.dropna(subset=['Latência'])

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
sns.boxplot(x=df['Latência'])
plt.title('Boxplot da Latência')
plt.xlabel('Latência (ms)')
plt.show()

# teste de hipótese Z
latencia_media = 10  # latencia média hipotetica
n = len(df['Latência']) # tamanho da amostra
z = (media - latencia_media) / (desvio_padrao / np.sqrt(n)) 

# z crítico para um teste bilateral com α = 0.05
z_critical = 1.96

# verifica se rejeitamos a hipótese nula
reject_null = abs(z) > z_critical

print(f"Estatística z: {z}")
print(f"Rejeitar H0: {reject_null}")