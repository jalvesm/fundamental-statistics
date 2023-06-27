import seaborn as sns
import matplotlib.pyplot as plt

# Dados
dados = [12, 14, 15, 16, 16, 16, 16, 16, 16, 17, 18, 18, 19, 19, 19, 19, 19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24, 24, 24, 25, 25, 25, 26]

# Gerar o histograma detalhado
sns.histplot(dados, kde=True, bins=6, color='blue', edgecolor='black')

# Configurar os rótulos do eixo x e y
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma Detalhado dos Dados')
plt.xticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]) # mudar escala do eixo X
# Exibir o histograma
plt.show()
