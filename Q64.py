# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def count_combinations_fixed_position(total_elements, combination_size, fixed_position_element):
    # Restante dos elementos após fixar o elemento na posição fixa
    remaining_elements = total_elements - 1  # Exclui o elemento fixo
    # Número de combinações dos elementos restantes
    return comb(remaining_elements, combination_size - 1)

# Total de elementos é 12, combinação de tamanho 5, e o elemento a8 está fixo na 3ª posição
total_elements = 12
combination_size = 5
fixed_position_element = 8

print("Número de combinações com o elemento a8 na 3ª posição:", count_combinations_fixed_position(total_elements, combination_size, fixed_position_element))
