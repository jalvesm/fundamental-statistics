import scipy.stats as stats

confianca = 0.98  # Confiança desejada
margem_erro = 0.36  # Margem de erro desejada
desvio_padrao = 1.1  # Desvio-padrão populacional

#Encontrar o valor crítico da distribuição normal padrão
z = stats.norm.ppf((1 + confianca) / 2)

#Calcular o tamanho mínimo da amostra
tamanho_amostra = ((z * desvio_padrao) / margem_erro) ** 2
tamanho_amostra = round(tamanho_amostra)

print(f"O tamanho mínimo da amostra necessário é de {tamanho_amostra} elementos.")