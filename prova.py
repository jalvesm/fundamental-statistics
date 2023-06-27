
import numpy as np

# Crie um conjunto de dados como uma matriz NumPy
dados = [6.8, 6.8, 5.9, 7.5, 6.2, 6.9, 7.2, 8, 6.6]

# Calcule a média e o desvio padrão dos dados
media = np.mean(dados)
desvio_padrao = np.std(dados)

# Calcule o coeficiente de variação estatística
cv = (desvio_padrao / media) * 100

# Imprima o resultado
print("Coeficiente de variação: {:.3f}%".format(cv))


