
import numpy as np
from scipy.stats import pearsonr, linregress
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import icecream as ic
# Dados
x = np.array([12, 16, 18, 20, 28, 30, 40, 48, 50, 54])
y = np.array([7.2, 7.4, 7, 7.5, 6.6, 6.7, 6, 5.6, 6, 5.5])

# Coeficiente de Pearson
correlation_coef, _ = pearsonr(x, y)
print("Coeficiente de Pearson:", correlation_coef)

# Equação de regressão linear
slope, intercept, _, _, _ = linregress(x, y)
regression_equation = f"y = {slope:.5f}x + {intercept:.5f}"
print("Equação de regressão linear:", regression_equation)

# Coeficiente de determinação (R²)
r_squared = correlation_coef ** 2
print("Coeficiente de determinação (R²):", r_squared)
