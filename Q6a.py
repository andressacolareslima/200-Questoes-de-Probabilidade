# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 6 - Quantos números de quatro dígitos são maiores que 2400 e:
# a) tem todos os digitos diferentes

#Numeros iniciados por 2
import math

def num_distintos (varia_num):
    num_distintos = math.prod(varia_num)
    total_variacoes = num_distintos
    return total_variacoes

varia_num = [1,6,8,7]
total_variacoes = num_distintos (varia_num) - 1


# Demais numeros 

def num_distintos2 (varia_num2):
    num_distintos2 = math.prod (varia_num2)
    total_variacoes2 = num_distintos2
    return total_variacoes2
varia_num2 = [7,9,8,7]
total_variacoes2 = num_distintos2(varia_num2)
resultado = total_variacoes + total_variacoes2

print ("As possibilidades para o item a são:", int (resultado))

