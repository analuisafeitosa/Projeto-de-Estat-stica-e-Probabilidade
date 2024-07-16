import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from acessoaobd import acessoaobd

data = acessoaobd()

sns.histplot(data, kde=True)
plt.title('Histograma dos dados de latência')
plt.xlabel('Latência')
plt.ylabel('Frequência')
plt.show()

stats.probplot(data, dist="norm", plot=plt)
plt.title('Gráfico Q-Q dos dados de latência')
plt.xlabel('Quantis teóricos')
plt.ylabel('Valores observados')
plt.show()

shapiro_test = stats.shapiro(data)
print(f"Shapiro-Wilk Test: Estatística={shapiro_test.statistic}, p-valor={shapiro_test.pvalue}")

ks_test = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))
print(f"Kolmogorov-Smirnov Test: Estatística={ks_test.statistic}, p-valor={ks_test.pvalue}")

ad_test = stats.anderson(data, dist='norm')
print(f"Anderson-Darling Test: Estatística={ad_test.statistic}, Valores Críticos={ad_test.critical_values}, Significância={ad_test.significance_level}")

jb_test = stats.jarque_bera(data)
print(f"Jarque-Bera Test: Estatística={jb_test.statistic}, p-valor={jb_test.pvalue}")