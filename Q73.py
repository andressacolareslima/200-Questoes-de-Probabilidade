
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import symbols
from sympy import  solve

x = int (input())


n = symbols('n')
expr = (1 + x)**n
coeff_x0 = expr.coeff(x, 0)
values_n = solve(coeff_x0, n)
print(values_n)
