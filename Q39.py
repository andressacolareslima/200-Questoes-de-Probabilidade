# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from itertools import permutations

def permutacoes_restritas(n):
    count = 0
    # Gerar todas as permutações de 1 a n
    for perm in permutations(range(1, n + 1)):
        valid = True
        for k in range(n):
            if perm[k] >= (k + 1) + 4:
                valid = False
                break
        if valid:
            count += 1
    return count

n = 5  # Defina o valor de n conforme necessário
resultado_permutacoes = permutacoes_restritas(n)
print(f'O número de permutações com a condição dada para n = {n} é: {resultado_permutacoes}')
