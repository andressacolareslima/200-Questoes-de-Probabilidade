# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

# Número de livros de cada assunto
livros_matematica = 5
livros_fisica = 3
livros_estatistica = 2

# Primeiramente, tratamos cada grupo de livros como um único "bloco"
# Há 3 blocos (Matemática, Física, Estatística)
# O número de maneiras de organizar esses blocos na prateleira
organizacao_blocos = math.factorial(3)

# Dentro de cada "bloco", podemos organizar os livros de diversas maneiras
# Número de maneiras de organizar os livros de Matemática
organizacao_matematica = math.factorial(livros_matematica)

# Número de maneiras de organizar os livros de Física
organizacao_fisica = math.factorial(livros_fisica)

# Número de maneiras de organizar os livros de Estatística
organizacao_estatistica = math.factorial(livros_estatistica)

# Número total de modos de organizar os livros
total_modos = organizacao_blocos * organizacao_matematica * organizacao_fisica * organizacao_estatistica

total_modos
