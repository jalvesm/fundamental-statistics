import scipy.stats as stats
import numpy as np
from icecream import ic

def intervalo_confianca_z(amostra, nivel_confianca):
    # Calcula a média e o desvio padrão da amostra
    media_amostra = np.mean(amostra)
    desvio_padrao_amostra = np.std(amostra, ddof=1)

    # Calcula o valor crítico da distribuição normal padrão (tabela Z)
    z = stats.norm.ppf(1 - (1 - nivel_confianca) / 2)

    # Calcula o erro padrão
    erro_padrao = desvio_padrao_amostra / (len(amostra) ** 0.5)

    # Calcula o limite inferior do intervalo de confiança
    limite_inferior = media_amostra - z * erro_padrao

    # Calcula o limite superior do intervalo de confiança
    limite_superior = media_amostra + z * erro_padrao

    return limite_inferior, limite_superior

# Exemplo de uso
amostra = [22, 25, 28, 30, 24, 27, 26, 23, 29, 28]
nivel_confianca = 0.95

limite_inferior, limite_superior = intervalo_confianca_z(amostra, nivel_confianca)

print("Intervalo de Confiança:", limite_inferior, "-", limite_superior)
