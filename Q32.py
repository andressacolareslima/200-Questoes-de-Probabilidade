# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import factorial

def combinacao(n, k):
    """Calcula o número de combinações de n elementos tomados k a k."""
    return factorial(n) // (factorial(k) * factorial(n - k))

def dividir_em_grupos(total_pessoas, tamanhos_grupos):
    """Calcula o número de maneiras de dividir total_pessoas em grupos de tamanhos especificados."""
    resultado = factorial(total_pessoas)
    for tamanho in tamanhos_grupos:
        resultado //= factorial(tamanho)
    # Dividido pelo número de permutações dos grupos, pois a ordem dos grupos não importa
    resultado //= factorial(len(tamanhos_grupos))
    return resultado

# a) Em dois grupos de 6
grupos_a = dividir_em_grupos(12, [6, 6])
print(f'a) Número de maneiras de dividir em dois grupos de 6: {grupos_a}')

# b) Em três grupos de 4
grupos_b = dividir_em_grupos(12, [4, 4, 4])
print(f'b) Número de maneiras de dividir em três grupos de 4: {grupos_b}')

# c) Em um grupo de 5 e um grupo de 7
# Não precisamos dividir por permutações dos grupos, pois há apenas dois grupos e sua ordem não importa
grupos_c = combinacao(12, 5) * combinacao(7, 7)
print(f'c) Número de maneiras de dividir em um grupo de 5 e um grupo de 7: {grupos_c}')

# d) Em seis grupos de 2
grupos_d = dividir_em_grupos(12, [2, 2, 2, 2, 2, 2])
print(f'd) Número de maneiras de dividir em seis grupos de 2: {grupos_d}')

# e) Em dois grupos de 4 e dois grupos de 2
grupos_e = dividir_em_grupos(12, [4, 4, 2, 2])
print(f'e) Número de maneiras de dividir em dois grupos de 4 e dois grupos de 2: {grupos_e}')
