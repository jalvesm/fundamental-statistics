import math

media = 7  # Média em milissegundos
λ = 1 / media  # Parâmetro de taxa da distribuição exponencial

x1 = 6  # Tempo inicial em milissegundos
x2 = 13  # Tempo final em milissegundos

F_x1 = 1 - math.exp(-λ * x1)  # Função de distribuição acumulada em x1
F_x2 = 1 - math.exp(-λ * x2)  # Função de distribuição acumulada em x2

probabilidade = F_x2 - F_x1

print("Probabilidade de o tempo de resposta estar entre 6 e 13 milissegundos:", probabilidade)
