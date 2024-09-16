# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import comb

def number_of_lines(n):
    if n < 2:
        return 0
    return comb(n, 2)

# Exemplo para n = 5
print("Número de retas com 5 pontos:", number_of_lines(5))

def max_intersections(n):
    if n < 4:
        return 0
    num_lines = comb(n, 2)
    return comb(num_lines, 2)

# Exemplo para n = 5
print("Número máximo de interseções com 5 pontos:", max_intersections(5))
