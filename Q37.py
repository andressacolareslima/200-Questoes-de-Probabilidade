# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import factorial

def calcular_dados_diferentes(n_faces, simetrias):
    """Calcula o número de dados diferentes que podem ser formados com n_faces, considerando as simetrias."""
    total_arranjos = factorial(n_faces)  # Total de arranjos possíveis
    dados_diferentes = total_arranjos // simetrias  # Dividido pelo número de simetrias
    return dados_diferentes

# Tetraedro Regular (4 faces, 12 simetrias)
n_faces_tetraedro = 4
simetrias_tetraedro = 12
resultado_tetraedro = calcular_dados_diferentes(n_faces_tetraedro, simetrias_tetraedro)

# Octaedro Regular (8 faces, 24 simetrias)
n_faces_octaedro = 8
simetrias_octaedro = 24
resultado_octaedro = calcular_dados_diferentes(n_faces_octaedro, simetrias_octaedro)

# Dodecaedro Regular (12 faces, 60 simetrias)
n_faces_dodecaedro = 12
simetrias_dodecaedro = 60
resultado_dodecaedro = calcular_dados_diferentes(n_faces_dodecaedro, simetrias_dodecaedro)

# Icosaedro Regular (20 faces, 60 simetrias)
n_faces_icodsaedro = 20
simetrias_icodsaedro = 60
resultado_icodsaedro = calcular_dados_diferentes(n_faces_icodsaedro, simetrias_icodsaedro)

# Prisma Hexagonal Regular (8 faces, 24 simetrias)
n_faces_prisma_hexagonal = 8
simetrias_prisma_hexagonal = 24
resultado_prisma_hexagonal = calcular_dados_diferentes(n_faces_prisma_hexagonal, simetrias_prisma_hexagonal)

# Pirâmide Quadrangular Regular (5 faces, 20 simetrias)
n_faces_piramide = 5
simetrias_piramide = 20
resultado_piramide = calcular_dados_diferentes(n_faces_piramide, simetrias_piramide)

print(f'a) Número de dados diferentes para um tetraedro com números de 1 a 4: {resultado_tetraedro}')
print(f'b) Número de dados diferentes para um octaedro com números de 1 a 8: {resultado_octaedro}')
print(f'c) Número de dados diferentes para um dodecaedro com números de 1 a 12: {resultado_dodecaedro}')
print(f'd) Número de dados diferentes para um icosaedro com números de 1 a 20: {resultado_icodsaedro}')
print(f'e) Número de dados diferentes para um prisma hexagonal com números de 1 a 8: {resultado_prisma_hexagonal}')
print(f'f) Número de dados diferentes para uma pirâmide quadrangular com números de 1 a 5: {resultado_piramide}')
