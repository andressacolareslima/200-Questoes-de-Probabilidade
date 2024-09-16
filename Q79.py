
# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from sympy import factorial
from sympy import symbols

n = symbols('n')
k = symbols('k')
total_subsets = 2**(n - k)
print(total_subsets)
