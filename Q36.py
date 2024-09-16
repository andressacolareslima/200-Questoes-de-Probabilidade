# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

def calcular_dados_diferentes():
    total_arranjos = factorial(6)  # Total de arranjos sem considerar simetria
    simetrias_cubo = 24            # Número de simetrias do cubo

    # Número de arranjos distintos considerando as simetrias do cubo
    dados_diferentes = total_arranjos // simetrias_cubo
    return dados_diferentes

resultado = calcular_dados_diferentes()
print(f'O número de dados diferentes que podemos formar é: {resultado}')
