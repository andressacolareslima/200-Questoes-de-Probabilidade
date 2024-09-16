# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

# Número total de permutações das 7 pessoas
total_permutacoes = math.factorial(7)

# Número de permutações em que duas pessoas específicas estão juntas
# Podemos tratar as duas pessoas como um "bloco", o que deixa 6 "pessoas" para organizar
# E dentro do "bloco", as duas pessoas podem trocar de lugar (2! maneiras)
permutacoes_juntas = math.factorial(6) * 2

# Número de permutações em que as duas pessoas NÃO ficam juntas
permutacoes_nao_juntas = total_permutacoes - permutacoes_juntas

permutacoes_nao_juntas
