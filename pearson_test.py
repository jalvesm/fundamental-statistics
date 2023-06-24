# Import the packages and classes needed in this example:
import numpy as np
# from sklearn.linear_model import LinearRegression

# Create a numpy array of data:
x = np.array([28, 25, 25, 23, 30, 32, 21, 35, 26, 25]).reshape((-1, 1))
y = np.array([30, 50, 40, 55, 30, 25, 60, 25, 50, 55])
# 
# # Create an instance of a linear regression model and fit it to the data with the fit() function:
# model = LinearRegression().fit(x, y) 
# 
# # The following section will get results by interpreting the created instance: 
# 
# # Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
# r_sq = model.score(x, y)
# print('coefficient of determination:', r_sq)
# 
# # Print the Intercept:
# print('intercept:', model.intercept_)
# 
# # Print the Slope:
# print('slope:', model.coef_) 
# 
# # Predict a Response and print it:
# y_pred = model.predict(x)
# print('Predicted response:', y_pred, sep='\n')

# from scipy import stats
# res = stats.pearsonr(y, x)
# print(res)
# 
# import statistics
# 
# data = [30, 50, 40, 55, 30, 25, 60, 25, 50, 55]
# 
# desvio_padrao_amostral = statistics.stdev(data)
# 
# print(desvio_padrao_amostral)
# 

import math

def calcular_correlacao_amostral(vetor_x, vetor_y):
    n = len(vetor_x)

    # Cálculo da média
    media_x = sum(vetor_x) / n
    media_y = sum(vetor_y) / n

    # Cálculo dos numeradores
    numerador_xy = sum((x - media_x) * (y - media_y) for x, y in zip(vetor_x, vetor_y))
    numerador_xx = sum((x - media_x) ** 2 for x in vetor_x)
    numerador_yy = sum((y - media_y) ** 2 for y in vetor_y)

    # Cálculo das variâncias amostrais
    sxx = numerador_xx * (n)
    syy = numerador_yy * (n)

    # Cálculo da correlação amostral
    correlacao = numerador_xy / math.sqrt(sxx * syy)

    return correlacao, sxx, syy

# vetor_x = [28, 25, 25, 23, 30, 32, 21, 35, 26, 25] # Consumo
# vetor_y = [30, 50, 40, 55, 30, 25, 60, 25, 50, 55] # Velocidade

vetor_x = [2,3,4,5,4,6,7,8,8,10] # Consumo
vetor_y = [48,50,56,52,43,60,62,58,64,72] # Velocidade

correlacao, sxx, syy = calcular_correlacao_amostral(vetor_x, vetor_y)

resultado_final = (sxx*syy)

print("Correlação amostral:", correlacao)
print("Sxx:", sxx)
print("Syy:", syy)


beta_1 = correlacao / sxx
print("coeficiente a: ", beta_1)

import math


import numpy as np

valores = [28, 25, 25, 23, 30, 32, 21, 35, 26, 25]

media = np.mean(valores)

print(media)

ICminus = media - (1.96 * (4.269/3.16))
ICm = media + (1.96 * (4.269/3.16))
print(ICminus)
print(ICm)


import numpy as np
from sklearn.linear_model import LinearRegression

# Dados de exemplo
x = np.array([28, 25, 25, 23, 30, 32, 21, 35, 26, 25])
y = np.array( [30, 50, 40, 55, 30, 25, 60, 25, 50, 55])

# Ajustar o modelo de regressão linear
regressor = LinearRegression()
regressor.fit(x.reshape(-1, 1), y)

# Previsões do modelo
y_pred = regressor.predict(x.reshape(-1, 1))

# Resíduos
residuos = y - y_pred

# Cálculo do erro padrão da estimativa
erro_padrao_estimativa = np.sqrt(np.sum(residuos**2) / (len(y) - 2))

print(erro_padrao_estimativa)


print("lalala")