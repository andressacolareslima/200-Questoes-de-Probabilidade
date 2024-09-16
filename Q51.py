# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def subsets_containing_a1(n, p):
    return comb(n-1, p-1)

def subsets_not_containing_a1(n, p):
    return comb(n-1, p)
def subsets_containing_a1_and_a2(n, p):
    return comb(n-2, p-2)
def subsets_containing_at_least_one_a1_or_a2(n, p):
    return comb(n, p) - comb(n-2, p)
def subsets_containing_exactly_one_a1_or_a2(n, p):
    return 2 * comb(n-2, p-1)
n = 10  # Total de elementos no conjunto
p = 4   # Tamanho dos subconjuntos

print("Subconjuntos que contêm a1:", subsets_containing_a1(n, p))
print("Subconjuntos que não contêm a1:", subsets_not_containing_a1(n, p))
print("Subconjuntos que contêm a1 e a2:", subsets_containing_a1_and_a2(n, p))
print("Subconjuntos que contêm pelo menos um dos elementos a1 ou a2:", subsets_containing_at_least_one_a1_or_a2(n, p))
print("Subconjuntos que contêm exatamente um dos elementos a1 ou a2:", subsets_containing_exactly_one_a1_or_a2(n, p))
