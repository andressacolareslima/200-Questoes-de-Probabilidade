# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"22- Fichas podem ser azuis, vermelhas ou amarelas; circulares, retangulares ou triangulares, finas ou grossas"
"Quantos tipos de ficha existem?"

"Existem 3 cores diferentes para cada ficha = 3"
"Também há três formatos diferentes = 3"
"E possue duas expessuras = 2"

"A quantidade de fichas é o produto dessas caracteristicas = 3x3x2"

import math

qtd_fichas = int (2*(math.pow(3,2)))

print (f"A quantidade de fichas é {qtd_fichas}")