
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import symbols
from sympy import floor, sqrt

n = symbols('n')
value = floor((2 + sqrt(3))**n)
is_odd = value % 2 != 0
print(is_odd)
