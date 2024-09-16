# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 11 - De quantos modos podemos arrumar 8 torres iguais em um tabuleiro de xadrez (8x8) de modo que não haja
# duas torres na mesma linha nem na mesma coluna?

import math 

def linhas (num_linhas, num_colunas):
    linhas = math.factorial(num_linhas) * math.factorial(num_colunas)
    return linhas

num_linhas = 8
num_colunas = 8
total_linhas = linhas(num_linhas,num_colunas)

print (f"O número de modos diferentes que podemos arrumar as torres é {total_linhas}")