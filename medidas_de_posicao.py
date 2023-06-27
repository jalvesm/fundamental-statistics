import statistics
import numpy as np
import math

#substituir o vetor a seguir pelos dados da prova  
data = [250, 194, 215, 259, 187, 187, 184]

print("\nVetor ordenado: ")
data.sort()
print(data)

media_aritmetica = statistics.mean(data)
print("\nMédia aritmética: ", media_aritmetica)

mediana = statistics.median(data)
print("\nMediana: ", mediana)

quantidade_de_funcionarios = mediana * 0.19
print(quantidade_de_funcionarios)

moda = statistics.mode(data)
print("\nModa:", moda)

# cálculo dos quartis

q1 = np.percentile(data, 25)
print("\nQuartil 1: ", q1)

q2 = np.median(data)
print("\nQuartil 2: ", q2)

q3 = np.percentile(data, 75)
print("\nQuartil 3: ", q3)


calculo = 0.007 * 0.1 + 0.022 * 0.15 + 0.002 * 0.15 + 0.025 * 0.4 + 0.061 * 0.2
print(calculo)


fat_6 = math.factorial(6)
fat_4 = math.factorial(4)
fat_2 = math.factorial(2)
fat_34 = math.factorial(34)
fat_40 = math.factorial(40)
fat_32 = math.factorial(32)

resposta = (fat_6 / (fat_4 * fat_2)) * (fat_34 / (fat_2 * fat_32)) / (fat_40 / (fat_6 * fat_34))
print(resposta)
