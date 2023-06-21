import matplotlib.pyplot as plt

# Dados de exemplo
consumo_cigarros = [240, 255, 340, 375, 510, 490, 490, 180, 1.125, 1.150, 1.275]
mortes_por_hab = [63, 100, 140, 175, 160, 180, 250, 180, 360, 470, 200]

# Cria o gráfico de dispersão
plt.scatter(consumo_cigarros, mortes_por_hab)

# Adiciona um título e rótulos aos eixos
plt.title('Diagrama de Dispersão Linear')
plt.xlabel('Consumo de cigarros')
plt.ylabel('Mortes (por 10⁶ hab)')

# Exibe o gráfico
plt.show()
