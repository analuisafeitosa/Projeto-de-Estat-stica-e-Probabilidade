import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from scipy.stats import norm 

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

# Parâmetros do teste
latencia_media = 10  # latência média hipotética
media = np.mean(df['Latência'])  # média da amostra
desvio_padrao = np.std(df['Latência'], ddof=1)  # desvio padrão da amostra
n = len(df['Latência'])  # tamanho da amostra


# Estatística do teste Z
z = (media - latencia_media) / (desvio_padrao / np.sqrt(n))

# z crítico para um teste unilateral à esquerda com α = 0.05
z_critical = norm.ppf(0.05)

# Verifica se rejeitamos a hipótese nula
reject_null = z < z_critical

print(f"Estatística z: {z}")
print(f"Rejeitar H0: {reject_null}")

# Plot
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuição Normal Padrão')
plt.fill_between(x, y, where=(x <= z_critical), color='red', alpha=0.5, label='Região de Rejeição')
plt.axvline(z, color='blue', linestyle='--', label=f'Estatística Z = {z:.2f}')
plt.title('Gráfico do Teste de Hipótese Z Unilateral à Esquerda')
plt.xlabel('Valores Z')
plt.ylabel('Densidade')
plt.legend()
plt.show()