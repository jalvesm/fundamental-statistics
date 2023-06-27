
import numpy as np
from scipy.stats import pearsonr, linregress
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# Dados
x = np.array([62, 74, 70, 98, 88, 80, 78, 67, 75, 86, 83, 78])
y = np.array([515, 430, 475, 565, 620, 510, 495, 480, 555, 535, 470, 445])

# Coeficiente de Pearson
correlation_coef, _ = pearsonr(x, y)
print("Coeficiente de Pearson:", correlation_coef)

# Equação de regressão linear
slope, intercept, _, _, _ = linregress(x, y)
regression_equation = f"y = {slope:.5f}x + {intercept:.5f}"
print("Equação de regressão linear:", regression_equation)
