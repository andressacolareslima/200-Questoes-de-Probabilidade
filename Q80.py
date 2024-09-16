
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import Sum
from sympy import symbols

k = int (input())

n = symbols('n')
sum_expr = Sum(k**2, (k, 0, n))
sum_expr_d = sum_expr.doit()
print (sum_expr_d)
