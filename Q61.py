# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def min_padlocks(n_scientists, min_present):
    from math import comb
    # Total de cadeados deve ser o número de combinações de (n_scientists - min_present + 1)
    return comb(n_scientists, min_present) - 1

# Exemplo para 9 cientistas e pelo menos 5 presentes
n_scientists = 9
min_present = 5
print("Número mínimo possível de cadeados:", min_padlocks(n_scientists, min_present))
