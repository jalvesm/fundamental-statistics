import statistics
import numpy as np
import math
from itertools import filterfalse

#define array of data
data = np.array([28,31,32,36,36,36,38,41,41,42,42,42,44,45,47,47,48,48,48,49,49,49,50,50,51,51,51,51,54,54,54,56,57,57,60,61,61,61,64])

#calculate interquartile range 
q3, q1 = np.percentile(data, [75 ,25])
iqr = q3 - q1
print("Amplitude interquartil:", iqr)
print("\n")
dp = statistics.stdev([11,14.50,9.60,9.60,6.00,6.00,6.00,4.50,4.50,4.50])
print("dp do salário = ", dp)

print("\n")
dp = statistics.stdev([5,8,6,8,3,2,5,2,3,3])
print("dp dos anos de empresa = ", dp)


from scipy.special import comb

N1 = 10  # Número de elementos que não passam no teste
N2 = 12  # Número de elementos que passam no teste
n = 5  # Tamanho da amostra
N = 22  # Tamanho da população

probabilidade = (comb(N1, 4) * comb(N2, n - 4)) / comb(N, n)

print("Probabilidade de 4 lampadas ñ passarem no teste:", probabilidade)



taxa = 5  # Taxa de desembarque de brasileiros por hora
k = 2  # Número máximo de brasileiros desembarcando

probabilidade = 0

for i in range(k + 1):
    probabilidade += math.exp(-taxa) * (taxa ** i) / math.factorial(i)

print("Probabilidade de q cheguem nos eua no maximo 2 br:", probabilidade)


import scipy.stats as stats

media = 20  # Média em minutos
desvio_padrao = 4  # Desvio padrão em minutos
probabilidade_cancelamento = 0.07  # Probabilidade de cancelamento por atraso

probabilidade_nao_cancelamento = 1 - probabilidade_cancelamento

# Encontrar o valor da distribuição normal correspondente aos 93% superiores
limite_superior = stats.norm.ppf(probabilidade_nao_cancelamento, loc=media, scale=desvio_padrao)

print("Tempo máximo de espera para evitar cancelamento:", limite_superior, "minutos")
