#   Para realizar um teste de hipótese com base na média de uma amostra, você pode seguir os seguintes passos:
#   
#   1) Formular as hipóteses nula (H0) e alternativa (H1):
#   
#   H0: A vida média dos bulbos é igual a um determinado valor (hipótese nula).
#   H1: A vida média dos bulbos é diferente desse valor (hipótese alternativa).
#   
#   2) Especificar o nível de significância desejado, que representa a probabilidade de rejeitar 
# erroneamente a hipótese nula.
#   
#   3) Calcular a estatística de teste apropriada. Neste caso, como a distribuição é aproximadamente normal e o 
# desvio-padrão populacional é conhecido, podemos usar um teste z.
#   
#   4) Determinar a região crítica ou valor crítico para o teste. Isso depende da hipótese 
# alternativa e do nível de significância.
#   
#   5) Comparar a estatística de teste com o valor crítico ou determinar se está dentro ou fora da região crítica.
#   
#   6) Concluir o teste e interpretar os resultados.

import numpy as np
from scipy.stats import t

def teste_hipotese(amostra, media_hipotese, nivel_significancia):
    tamanho_amostra = len(amostra)
    media_amostra = np.mean(amostra)
    desvio_padrao_amostra = np.std(amostra, ddof=1)

    # Calcula a estatística de teste t
    t_valor = (media_amostra - media_hipotese) / (desvio_padrao_amostra / np.sqrt(tamanho_amostra))

    # Calcula os graus de liberdade
    graus_liberdade = tamanho_amostra - 1

    # Calcula o valor crítico t para o nível de significância desejado
    valor_critico_t = t.ppf(1 - nivel_significancia/2, graus_liberdade)

    # Verifica se a estatística de teste está dentro ou fora da região crítica
    if abs(t_valor) > valor_critico_t:
        resultado = "Rejeita H0"
    else:
        resultado = "Aceita H0"

    return t_valor, resultado

# Exemplo de uso
amostra = [8.24, 8.23, 8.20, 8.21, 8.20, 8.28, 8.23, 8.26, 8.24, 8.25, 8.19, 8.25, 8.26, 8.23, 8.24]
media_hipotese = 8.22
nivel_significancia = 0.05

estatistica_t, resultado = teste_hipotese(amostra, media_hipotese, nivel_significancia)

print("Estatística de teste t:", estatistica_t)
print("Resultado do teste:", resultado)