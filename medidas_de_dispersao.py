## CÁLCULOS NECESSÁRIOS PARA AS MEDIDAS DE DISPERSÃO

import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt

data = [14,19,24,19,16,20,24,20,21,22,24,18,17,23,26,22,23,25,25,19,18,16,15,24,21,16,19,21,23,20,22,22,16,16,16,12,25,19,24,20]
data.sort()
print(data)

desvio_padrao = np.std(data)
print("\nDesvio padrão = ", desvio_padrao)

variancia = math.sqrt(desvio_padrao)
print("\nVariancia = ", variancia)

amplitude = max(data) - min(data)
print("\nAmplitude = ", amplitude)

def calcula_numero_de_classes(arr):
    n = len(arr) # seja n o tamanho do vetor!
    print("\nTamanho do vetor = ", n)
    k = math.sqrt(n)
    numero_de_classes_arredondado = round(k)
    return numero_de_classes_arredondado
 
num_classes = calcula_numero_de_classes(data)
print(num_classes)

# Gerar o histograma detalhado
sns.histplot(data, kde=True, bins=num_classes, color='blue', edgecolor='black')

# Configurar os rótulos do eixo x e y
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma Detalhado dos Dados')

# Exibir o histograma
plt.show()
