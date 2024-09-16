
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import symbols

x = int (input())
y = int (input())

n = symbols('n')
expr = (2*x**2 - 3*y)**n
soma_coef = expr.subs(x, 1).subs(y, 1)
soma_coef

