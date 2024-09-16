# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

# Valores
a = 17
b = 2
c = 1

# Calculando o coeficiente
coeficiente = factorial(20) // (factorial(a) * factorial(b) * factorial(c))

# Exibindo o resultado
print("O coeficiente de x^17 é:", coeficiente)