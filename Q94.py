# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

def combinacao(n, k):
    return math.comb(n, k)

n = 20
k = 4

numero_de_termos = combinacao(n + k - 1, k - 1)

print(f"O número de termos distintos no desenvolvimento é: {numero_de_termos}")