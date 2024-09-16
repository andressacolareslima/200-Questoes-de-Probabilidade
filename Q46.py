# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

def calcular_participantes(total_partidas):
    # Resolva a equação n(n - 1) / 2 = total_partidas
    a = 1
    b = -1
    c = -2 * total_partidas
    
    # Calcular o discriminante
    discriminante = b**2 - 4 * a * c
    raiz_discriminante = math.sqrt(discriminante)
    
    # Calcular as soluções
    n1 = (-b + raiz_discriminante) / (2 * a)
    n2 = (-b - raiz_discriminante) / (2 * a)
    
    # A solução positiva
    n = int(n1)
    
    return n

# Número total de partidas
total_partidas = 780
resultado_participantes = calcular_participantes(total_partidas)
print(f'O número de participantes é: {resultado_participantes}')
