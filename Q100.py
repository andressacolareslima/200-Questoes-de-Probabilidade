# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

total_combinacoes = comb(10, 4)

combinacoes_favoraveis = comb(9, 3)

probabilidade = combinacoes_favoraveis / total_combinacoes

print(f"Probabilidade de uma pessoa específica ser sorteada: {probabilidade:.2f}")