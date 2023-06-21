import numpy as np
from statsmodels.base.model import Model

vetor = np.array([11, 9, 8, 10, 10, 9, 7, 11, 11, 7, 6, 9, 10, 8, 10])


desvio_padrao_amostral = np.std(vetor, ddof=1)

print("Desvio padrão amostral:", desvio_padrao_amostral)

# 
# vetor1 = np.array([1.55, 1.53, 1.37, 1.33, 1.32, 1.06, 1.03, 0.94, 0.90, 0.89, 0.38, 0.34])
# 
# desvio_padrao_populacional = np.std(vetor1)
# 
# print("Desvio padrão populacional:", desvio_padrao_populacional)
# 
# 
# # Dados da tabela de frequência
# classes = np.array([130, 150, 170, 190, 210,230])  # Classes
# frequencias = np.array([2,4,6,8,6,4])  # Frequências
# media = 180  # Média dos dados
# 
# # Cálculo do desvio padrão
# variancia = np.sum(frequencias * (classes - media) ** 2) / np.sum(frequencias)
# desvio_padrao = np.sqrt(variancia)
# 
# print("Desvio padrão:", desvio_padrao)
# 
# 
# # Dados do histograma (exemplo)
# frequencias = [5, 10, 15, 10, 5]  # Frequências
# pontos_medios = [2.5, 7.5, 12.5, 17.5, 22.5]  # Pontos médios das classes
# 
# # Cálculo do desvio padrão amostral
# media = np.sum(np.array(frequencias) * np.array(pontos_medios)) / np.sum(frequencias)
# desvios = np.array(pontos_medios) - media
# desvio_padrao_amostral = np.sqrt(np.sum(np.array(frequencias) * desvios**2) / (np.sum(frequencias) - 1))
# 
# print("Desvio padrão amostral:", desvio_padrao_amostral)
# 


import numpy as np
 
data = [20, 31, 32, 36, 36, 36, 38, 41, 41, 42, 42, 42, 44, 45, 47, 47, 48, 48, 48, 49, 49, 49, 50, 50, 51, 51, 51, 51, 54, 54, 54, 56, 57, 57, 60, 61, 61, 61, 64]
sorted_data = np.sort(data)

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
print(q1)
print(q3)

iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

print(lower_fence)
print(upper_fence)

lower_values = []
upper_values = []

for x in data:
    if x < lower_fence:
        lower_values.append(x)
    elif (x > upper_fence):
        upper_values.append(x)

print(lower_values)
print(upper_values)

amostra = [1.55,1.53,1.37,1.33,1.32,1.06,1.03,0.94,0.90,0.89,0.38,0.34]

desvio_padrao_amostral = np.std(amostra, ddof=1)

print("desvio_padrao_amostral: ", desvio_padrao_amostral)

vetor = [11, 9, 8, 10, 10, 9, 7, 11, 11, 7, 6, 9, 10, 8, 10]
media = np.mean(vetor)
print("media do vetor: ", media)


import math

print("#####################")
print("pergunta 3")
proporcao_amostra = 0.1
tamanho_amostra = 290
nivel_confianca = 0.95

valor_critico = 1.96
erro_padrao = math.sqrt((proporcao_amostra * (1 - proporcao_amostra)) / tamanho_amostra)

intervalo_confianca = (proporcao_amostra - valor_critico * erro_padrao, proporcao_amostra + valor_critico * erro_padrao)

print(f"Intervalo de 95% de confiança: {intervalo_confianca}")

print("#####################")
print("pergunta 2")


import math

desvio_padrao = 2.10
tamanho_amostra = 16
media_amostra = 12.53
nivel_confianca = 0.90

valor_critico = 1.753
erro_padrao = desvio_padrao / math.sqrt(tamanho_amostra)

intervalo_confianca = (media_amostra - valor_critico * erro_padrao, media_amostra + valor_critico * erro_padrao)

print(f"Intervalo de 95% de confiança: {intervalo_confianca}")

import math

proporcao_estimada = 0.2
erro_maximo = 0.025
nivel_confianca = 0.99

valor_critico = 2.576  # Valor crítico para um nível de confiança de 99%

tamanho_amostra = math.ceil((valor_critico**2 * proporcao_estimada * (1 - proporcao_estimada)) / erro_maximo**2)

print("Tamanho da amostra necessário:", tamanho_amostra)




print("\n\n\n#############")


import numpy as np
from scipy.stats import pearsonr, linregress
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# Dados
x = np.array([2, 3, 4, 5, 4, 6, 7, 8, 8, 10])
y = np.array([48, 50, 56, 52, 43, 60, 62, 58, 64, 72])

# Coeficiente de Pearson
correlation_coef, _ = pearsonr(x, y)
print("Coeficiente de Pearson:", correlation_coef)

# Equação de regressão linear
slope, intercept, _, _, _ = linregress(x, y)
regression_equation = f"y = {slope:.2f}x + {intercept:.2f}"
print("Equação de regressão linear:", regression_equation)

# Coeficiente de determinação (R²)
r_squared = correlation_coef ** 2
print("Coeficiente de determinação (R²):", r_squared)

print("### à partir daqui melhorar o código")

n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(x * y)
x_squared_mean = np.mean(x**2)

# Cálculo dos coeficientes da regressão linear
b1 = (xy_mean - x_mean * y_mean) / (x_squared_mean - x_mean**2)
b0 = y_mean - b1 * x_mean

# Cálculo dos resíduos
y_pred = b0 + b1 * x
residuals = y - y_pred

rounded_arr = []
for item in residuals:
    rounded_item = round(item, 2)
    rounded_arr.append(rounded_item)

rounded_arr = np.array(rounded_arr)

print("residuals: ", rounded_arr)

squared_residuals = np.square(rounded_arr)

print("Itens ao quadrado:")
print(squared_residuals)

rounded_squared_residuals = np.round(squared_residuals,2)
print(rounded_squared_residuals)

soma = np.sum(rounded_squared_residuals)
print("soma: ", soma)


tamanho = x.shape[0]
print(tamanho)
denominador = tamanho - 2
se = math.sqrt(soma / denominador)
print("se: ", se)
