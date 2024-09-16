# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def intersection_points(n):
    if n < 4:
        return 0
    return comb(n, 4)

# Exemplo para um polígono de 6 lados
print("Número de pontos de interseção das diagonais em um polígono de 6 lados:", intersection_points(6))

def interior_points(n):
    return intersection_points(n)

# Exemplo para um polígono de 6 lados
print("Número de pontos de interseção interiores ao polígono de 6 lados:", interior_points(6))

def exterior_points(n):
    return 0

# Exemplo para um polígono de 6 lados
print("Número de pontos de interseção exteriores ao polígono de 6 lados:", exterior_points(6))
