
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import symbols
from sympy import binomial, Sum

k = int (input())
x = int (input())

n = symbols('n')
sum_expr = Sum(binomial(n, k) * x**k, (k, 0, n))
sum_expr_d = sum_expr.doit()
print(sum_expr_d)
