import scipy.stats as stats

media = 55
desvio_padrao = 24.2
percentil = 94

# Calculando o valor crítico correspondente ao percentil
valor_critico = stats.norm.ppf(percentil / 100, loc=media, scale=desvio_padrao)

print(f"O tempo máximo necessário para receber o certificado especial é de aproximadamente {valor_critico:.5f} minutos.")
