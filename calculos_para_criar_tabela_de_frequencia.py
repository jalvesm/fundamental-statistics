import numpy as np
import math
import matplotlib.pyplot as plt

print("\n## CÁLCULOS NECESSÁRIOS PARA A CONSTRUÇÃO DA TABELA DE FREQUÊNCIA ## \n")

print("Vetor original: ")
data = [6.8, 6.8, 5.9, 7.5, 6.2, 6.9, 7.2, 8, 6.6]
print(data)

print("\nVetor ordenado: ")
data.sort()
print(data)

def calcula_numero_de_classes(arr):
     n = len(arr) # seja n o tamanho do vetor!
     print("\nTamanho do vetor = ", n)
     k = math.sqrt(n)
     numero_de_classes_arredondado = round(k)
     return numero_de_classes_arredondado

def encontra_maior_valor(arr):
     maior_valor = max(arr)
     return maior_valor

def encontra_menor_valor(arr):
     menor_valor = min(arr)
     return menor_valor

def calcula_amplitude_total_dos_dados_coletados(arr):
     amplitude = max(arr) - min(arr)
     return amplitude

numero_de_classes = calcula_numero_de_classes(data)
print("Número de classes arredondado (raíz quadrada da quantidade de elementos do vetor) = ", numero_de_classes)

maior_valor = encontra_maior_valor(data)
print("\nMaior valor do vetor = ", maior_valor)

menor_valor = encontra_menor_valor(data)
print("\nMenor valor do vetor = ", menor_valor)

amplitude_dos_dados_coletados = calcula_amplitude_total_dos_dados_coletados(data)
print("\nAmplitude dos dados coletados = ", amplitude_dos_dados_coletados)

#amplitude_das_classes:
h =  amplitude_dos_dados_coletados / numero_de_classes
print("\nAmplitude das classes = ", h)
print("Obs: Arredonde o valor de ℎ conforme as regras de arredondamento. Este número deve ter a mesma quantidade de casas decimais dos dados da amostra")
print()

plt.boxplot(data)

# Adicione um título e rótulo do eixo y
plt.title("Boxplot dos dados")
plt.ylabel("Valores")

# Mostre o gráfico
plt.show()

#ATENÇÃO: O código abaixo funciona, mas ficar atentx aos p/ arredondamentos

plt.hist(data, bins=numero_de_classes) # número de classes arredondado p/ construção do histograma
plt.title("Histograma")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()

'''
# REGRAS DE TRÊS

total --- 100
n da amostra que me interessa --- x (n em porcentagem)



total = 34586
n_da_amostra = 346

porcentagem_de_n = (n_da_amostra * 100) / total
minha_string = str(porcentagem_de_n) + "%"
print(minha_string)

frequencia = [23908, 8192, 1693, 447, 346]
soma = 0

for n in frequencia:
     soma += n
     print(soma)


'''