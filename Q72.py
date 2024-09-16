# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import expand
from sympy import symbols

x = int (input())

n = symbols('n')
expr = (1 - x)**2 * (1 + x)**n
expanded_expr = expand(expr)
coef_x_n = expanded_expr.coeff(x, n)
print(coef_x_n)
