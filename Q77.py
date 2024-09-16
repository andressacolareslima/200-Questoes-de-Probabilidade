
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from sympy import expand

x = int (input())

expr = (1 + x)**4
expanded_expr = expand(expr)
soma_coef_par = sum(expanded_expr.coeff(x, i) for i in range(0, 5, 2))
print(soma_coef_par)
