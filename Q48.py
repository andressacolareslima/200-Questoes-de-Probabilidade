# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def combinacoes(h, a, n):
    total_combinacoes = 0
    for k in range(max(0, n - a), min(h, n) + 1):
        total_combinacoes += comb(h, k) * comb(a, n - k)
    return total_combinacoes

def calcular_combinacoes():
    # Para o homem
    amigas_homem = 5
    amigos_homem = 7
    total_homem = combinacoes(amigas_homem, amigos_homem, 6)
    
    # Para a esposa
    amigas_esposa = 7
    amigos_esposa = 5
    total_esposa = combinacoes(amigas_esposa, amigos_esposa, 6)
    
    # Número total de combinações
    total_combinacoes = total_homem * total_esposa
    return total_combinacoes

resultado_combinacoes = calcular_combinacoes()
print(f'O número total de modos que o homem e a esposa podem convidar 6 pessoas cada um é: {resultado_combinacoes}')
