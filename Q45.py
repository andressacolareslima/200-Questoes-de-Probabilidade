# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def calcular_quadrilateros_convexos():
    # Número de maneiras de escolher 2 pontos dos 5 pontos na reta R
    combinacoes_R = comb(5, 2)
    
    # Número de maneiras de escolher 2 pontos dos 8 pontos na reta R'
    combinacoes_R_prime = comb(8, 2)
    
    # Número total de quadriláteros convexos
    total_quadrilateros = combinacoes_R * combinacoes_R_prime
    return total_quadrilateros

resultado_quadrilateros = calcular_quadrilateros_convexos()
print(f'O número de quadriláteros convexos é: {resultado_quadrilateros}')
