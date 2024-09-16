# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def selecionar_jogos():
    # Número total de clubes
    total_clubes = 12
    # Número de clubes em cada jogo (6 clubes por rodada)
    clubes_por_rodada = 6
    # Calcular o número de combinações
    numero_combinacoes = comb(total_clubes, clubes_por_rodada)
    return numero_combinacoes

resultado_jogos = selecionar_jogos()
print(f'O número de modos de selecionar os jogos da primeira rodada é: {resultado_jogos}')
