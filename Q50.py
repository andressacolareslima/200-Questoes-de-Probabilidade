# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def calcular_numeros():
    # Caso 1
    caso1 = comb(7, 3) * comb(4, 2) * 8**2
    
    # Caso 2
    caso2 = comb(7, 4) * comb(3, 2) * 8
    
    # Caso 3
    caso3 = comb(7, 3) * comb(4, 3) * 8
    
    # Caso 4
    caso4 = comb(7, 5) * comb(2, 2) * 1
    
    # Caso 5
    caso5 = comb(7, 4) * comb(3, 3) * 1
    
    # Caso 6
    caso6 = comb(7, 6) * comb(1, 1) * 1
    
    # Caso 7
    caso7 = comb(7, 5) * comb(2, 2) * 1
    
    # Total
    total_numeros = caso1 + caso2 + caso3 + caso4 + caso5 + caso6 + caso7
    return total_numeros

resultado_numeros = calcular_numeros()
print(f'O número total de números naturais de 7 dígitos é: {resultado_numeros}')
