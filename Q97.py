# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from itertools import product

total_favoráveis = 0
for dado1, dado2 in product(range(1, 7), repeat=2):
    if dado1 + dado2 == 7:
        total_favoráveis += 1

total_resultados = 6 ** 2
probabilidade = total_favoráveis / total_resultados

print(f"O número total de combinações favoráveis é: {total_favoráveis}")
print(f"A probabilidade de obter uma soma de 7 é: {probabilidade:.4f}")