# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

def combinacao(n, k):
    return math.comb(n, k)

total_pecas = 35
pecas_boas = 20
amostra_tamanho = 10

total_maneiras = combinacao(total_pecas, amostra_tamanho)

maneiras_boas = combinacao(pecas_boas, amostra_tamanho)

probabilidade_todas_boas = maneiras_boas / total_maneiras

probabilidade_ao_menos_uma_defeito = 1 - probabilidade_todas_boas

print(f"A probabilidade de que ao menos uma peça na amostra seja defeituosa é: {probabilidade_ao_menos_uma_defeito:.4f}")