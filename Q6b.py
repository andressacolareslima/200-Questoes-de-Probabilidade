# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 6 - Quantos números de quatro dígitos são maiores que 2400 e:
#b) Não tem digitos iguais a 3, 5 ou 6

import math 

#numeros iniciados por 2:

def num_distintos (num_dif):
    num_distintos = math.prod(num_dif)
    total_dif = num_distintos
    return total_dif

num_dif = [1,4,7,7]
total_dif = num_distintos(num_dif) - 1

# As outras possibilidades
def num_distintos2 (num_dif2):
    num_distintos2 = math.prod (num_dif2)
    total_dif2 = num_distintos2
    return total_dif2

num_dif2 = [4,7,7,7]
total_dif2 = num_distintos2(num_dif2)

resultado = total_dif + total_dif2

print ("Os números de possibilidades para numeros é:",int (resultado))

