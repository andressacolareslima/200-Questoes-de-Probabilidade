# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

def calcular_arranjos():
    # Total de arranjos sem restrições
    total_arranjos = factorial(10)
    
    # Arranjos com Brasil e Portugal juntos
    arranjos_brasil_portugal = factorial(9) * factorial(2)
    
    # Arranjos com Iraque e EUA juntos
    arranjos_iraque_eua = factorial(9) * factorial(2)
    
    # Arranjos com Brasil-Portugal e Iraque-EUA juntos
    arranjos_brasil_portugal_e_iraque_eua = factorial(8) * (factorial(2) ** 2)
    
    # Arranjos onde Brasil e Portugal estão juntos, e Iraque e EUA não estão juntos
    arranjos_com_restricao = arranjos_brasil_portugal - arranjos_brasil_portugal_e_iraque_eua
    
    return arranjos_com_restricao

resultado = calcular_arranjos()
print(f'O número de modos para os delegados se sentarem, com Brasil e Portugal juntos e Iraque e EUA não juntos, é: {resultado}')
