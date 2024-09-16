# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

total_pecas = 28

total_combinacoes = comb(total_pecas, 2)

combinacoes_com_numero_comum = 7 * comb(7, 2)

probabilidade = combinacoes_com_numero_comum / total_combinacoes

print(f"Probabilidade de duas peças de dominó terem um número comum: {probabilidade:.4f}")