# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import expand

x = int (input())

expr = (x + 2)**20 * (x**2 - 1)**5
expanded_expr = expand(expr)
coef_x28 = expanded_expr.coeff(x, 28)
print(coef_x28)
