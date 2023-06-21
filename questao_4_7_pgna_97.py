'''

Depois de terem sido pesadas várias embalagens de 1 kg de café da marca “Apetitoso”, chegou-se à
conclusão de que, embora a embalagem indique 1 kg, o verdadeiro peso é uma variável aleatória
uniformemente distribuída no intervalo [0,85 kg ; 1,05 kg], isto é, a f.d.p. tem a seguinte forma:

𝑓(𝑥) =   { 𝑘, 0.85 ≤ 𝑥 ≤ 1.05
        { 0, 𝑐.𝑐.
        
(a) Calcule 𝑘 e represente graficamente 𝑓(𝑥).
(b) Determine a média e a variância do peso das embalagens.
(c) Qual a probabilidade de uma embalagem de café da marca “Apetitoso” pesar menos de 1 kg?
(d) Em 200 embalagens, quantas você esperaria que tivessem o peso superior ao indicado no rótulo?

'''

def calcula_k_da_funcao_densidade_uniforme_de_probabilidade(limite_inferior, limite_superior):
    k = 1 / (limite_superior - limite_inferior)
    k_arredondado = round(k)
    return k_arredondado

def calcula_media_aritmetica(limite_inferior, limite_superior):
    media = (limite_inferior + limite_superior) / 2
    return media

def cacula_var(limite_inferior, limite_superior):
    variancia = ((limite_superior - limite_inferior) ** 2)/12
    return variancia

def area_do_grafico(k, limite_inferior, limite_superior):
    variacao_no_eixo_x = (limite_superior - limite_inferior)
    area_do_retangulo = variacao_no_eixo_x * k
    return area_do_retangulo

def calcula_probabilidade_para_n_embalagens(nrm_pacotes, prob_1_embalagem):
    probabilidade_n_embalagens = nrm_pacotes * prob_1_embalagem
    return probabilidade_n_embalagens


print("(a) O valor da probabilidade é:")
constante = calcula_k_da_funcao_densidade_uniforme_de_probabilidade(0.85, 1.05)
print("K = ", constante)
print()

print("(b) Determine a média e a variância do peso das embalagens:")
media = calcula_media_aritmetica(0.85, 1.05)
var = cacula_var(0.85, 1.05)
variancia = format(var, ".3f")
print("Média: ", media)
print("Variância: ", variancia)
print()

print("(c) Qual a probabilidade de uma embalagem de café da marca “Apetitoso” pesar menos de 1 kg?")
prob = area_do_grafico(constante, 0.85, 1)
probabilidade = format(prob, ".2f")
print("Probabilidade = ", probabilidade)
print()

print("(d) Em 200 embalagens, quantas você esperaria que tivessem o peso superior ao indicado no rótulo?")
probabilidade_1_embalagem = 0.05 * (1/0.2)
probabilidae_200_embalagens = calcula_probabilidade_para_n_embalagens(200, probabilidade_1_embalagem)
print("Número de embalgens: ", round(probabilidae_200_embalagens))


