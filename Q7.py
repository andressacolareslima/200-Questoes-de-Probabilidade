# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 7 - O conjunto A possui 4 elementos e o conjunto B possui 7 elementos. Quais são as funções f: A -> B?
# Quantas são as funções injetoras f: A -> B?

#Funções de A -> B

import math

def conjunto(func):
  conjunto = math.prod(func)
  return conjunto

func = [4, 7]
total_funcoes = conjunto(func)

#Funções injetoras de A->B

injetora = 4
fatorial = math.factorial (injetora)

print("Quantidade de funções A->B:", int(total_funcoes), "\nQuantidades de funções injetoras A->B:",(fatorial))
