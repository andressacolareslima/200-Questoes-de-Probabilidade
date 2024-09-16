# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import comb

def calcular_numeros():
    # Número de maneiras de escolher 3 posições para o dígito 4
    maneiras_4 = comb(7, 3)
    
    # Número de maneiras de escolher 2 posições para o dígito 8
    maneiras_8 = comb(4, 2)
    
    # Número de maneiras de preencher as 2 posições restantes
    maneiras_restantes = 8**2
    
    # Número total de números
    total_numeros = maneiras_4 * maneiras_8 * maneiras_restantes
    return total_numeros

resultado_numeros = calcular_numeros()
print(f'O número total de números naturais de 7 dígitos é: {resultado_numeros}')
