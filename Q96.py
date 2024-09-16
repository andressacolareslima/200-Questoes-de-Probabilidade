# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from itertools import product

total_favoráveis = 0
for dado1, dado2, dado3 in product(range(1, 7), repeat=3):
    if dado1 + dado2 + dado3 == 12:
        total_favoráveis += 1

total_resultados = 6 ** 3
probabilidade = total_favoráveis / total_resultados

print(f"O número total de combinações favoráveis é: {total_favoráveis}")
print(f"A probabilidade de obter uma soma de 12 é: {probabilidade:.4f}")