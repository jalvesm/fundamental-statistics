import scipy.stats as stats
from icecream import ic


# USA TABELA Z 
def intervalo_confianca_z(media_amostra, desvio_padrao_populacao, tamanho_amostra, nivel_confianca):
    # Calcula o valor crítico da distribuição normal padrão (tabela Z)
    z = stats.norm.ppf(1 - (1 - nivel_confianca) / 2)

    # Calcula o erro padrão
    erro_padrao = desvio_padrao_populacao / (tamanho_amostra ** 0.5)

    # Calcula o limite inferior do intervalo de confiança
    limite_inferior = media_amostra - z * erro_padrao

    # Calcula o limite superior do intervalo de confiança
    limite_superior = media_amostra + z * erro_padrao

    return limite_inferior, limite_superior

# Exemplo de uso
media_amostra = 98
desvio_padrao_populacao = 2
tamanho_amostra = 9
nivel_confianca = 0.95

limite_inferior, limite_superior = intervalo_confianca_z(media_amostra, desvio_padrao_populacao, tamanho_amostra, nivel_confianca)

print("Intervalo de Confiança:", limite_inferior, "-", limite_superior)
