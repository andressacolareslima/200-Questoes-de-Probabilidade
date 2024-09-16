# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

def seat_couples(n_couples, n_seats):
    if n_couples * 2 > n_seats:
        return 0
    # Número de maneiras de organizar 6 casais em 20 poltronas, com cada casal junto
    return factorial(n_seats // 2) * factorial(n_couples)

# Para 6 casais e 20 poltronas
n_couples = 6
n_seats = 20
print("Número de maneiras de sentar 6 casais em 20 poltronas:", seat_couples(n_couples, n_seats))
