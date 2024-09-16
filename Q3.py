# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 3 - Quantos inteiros há entre 1000 e 9999 cujos algarismos são distintos? 

import math

def algarismo_distintos(number):
  algarismo_distintos = math.prod(number)
  total_numeros_distintos = algarismo_distintos

  return total_numeros_distintos

number = [9, 9, 8, 7]
total_numeros_distintos = algarismo_distintos(number)

print("As possibilidades de criar números distintos é:", int(total_numeros_distintos))

#Explicação do código: Para realizar o cálculo dessa questão, cada número precisa ser distinto,
#com isso, o primeiro algarismo tem 9 possibilidades de escolha (considerando os numerais de 0 a 9),
# uma vez que o 0 deve ser excluido, pois a questão expecifica que o primeiro numeral necessita ser maior que 
# 0. Tendo em vista essa abordagem, o segundo algarismo também possui 9 possibilidades de escolha, pois 
# excluimos o número utilizado na primeira posição. Seguindo a logica anterior, o terceiro terá 8 possibilidades, 
#e o quarto e último terá 7 possibilidades. Assim o calculo será apresentado da seguinte maneira 9x9x8x7,
#obtendo como resultado o valor de 4536.