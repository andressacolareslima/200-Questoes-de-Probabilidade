# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

# Total de permutações
total_permutacoes = factorial(10)

# Para cada permutação onde 5 está à direita de 2 e à esquerda de 3
# Vamos calcular usando combinatória
# 10! permutações no total

# Há 3! maneiras de permutar os números 1, 2, 3, ..., 10
# Para satisfazer a condição 5 à direita de 2 e à esquerda de 3,
# O número total de permutações válidas é dado por:
# Total de permutações / 3! = Total de permutações / (3!)

total_permutacoes_validas = total_permutacoes / 6  # 6 é o fatorial de 3

print(f'O número de permutações onde 5 está à direita de 2 e à esquerda de 3 é: {int(total_permutacoes_validas)}')
