# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import expand

x = int (input())

expr = (1 + x)**3 * (1 - x)**7
expanded_expr = expand(expr)
term_independent = expanded_expr.coeff(x, 0)
print(term_independent)
