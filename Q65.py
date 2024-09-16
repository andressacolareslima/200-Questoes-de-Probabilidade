# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def count_ordered_arrangements(h, m):
    # Número de maneiras de escolher h posições para os homens de h + m total posições
    return comb(h + m, h)

# Exemplo com h homens e m mulheres
h = 4  # Exemplo para 4 homens
m = 3  # Exemplo para 3 mulheres
print("Número de maneiras de colocar", h, "homens e", m, "mulheres em fila ordenada por altura:", count_ordered_arrangements(h, m))
