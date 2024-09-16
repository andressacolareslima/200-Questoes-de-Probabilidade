# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


def diagonais_octaedro():
    V = 6
    diagonais = (V * (V - 3)) // 2
    return diagonais

resultado_octaedro = diagonais_octaedro()
print(f'O número de diagonais em um octaedro regular é: {resultado_octaedro}')

def diagonais_icosaedro():
    V = 12
    diagonais = (V * (V - 3)) // 2
    return diagonais

resultado_icosaedro = diagonais_icosaedro()
print(f'O número de diagonais em um icosaedro regular é: {resultado_icosaedro}')

def diagonais_dodecaedro():
    V = 20
    diagonais = (V * (V - 3)) // 2
    return diagonais

resultado_dodecaedro = diagonais_dodecaedro()
print(f'O número de diagonais em um dodecaedro regular é: {resultado_dodecaedro}')

def diagonais_cubo():
    V = 8
    diagonais = (V * (V - 3)) // 2
    return diagonais

resultado_cubo = diagonais_cubo()
print(f'O número de diagonais em um cubo é: {resultado_cubo}')

def diagonais_prisma_hexagonal():
    V = 12
    diagonais = (V * (V - 3)) // 2
    return diagonais

resultado_prisma_hexagonal = diagonais_prisma_hexagonal()
print(f'O número de diagonais em um prisma hexagonal regular é: {resultado_prisma_hexagonal}')
