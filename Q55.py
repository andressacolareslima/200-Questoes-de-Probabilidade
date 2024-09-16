# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def draw_5_cards():
    from math import comb
    return comb(52, 5)

print("Número de maneiras de sacar 5 cartas de um baralho de pôquer:", draw_5_cards())
