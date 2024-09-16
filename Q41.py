# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def calcular_comissoes():
    # Número de maneiras de escolher 3 homens de 8
    combinacoes_homens = comb(8, 3)
    # Número de maneiras de escolher 3 mulheres de 5
    combinacoes_mulheres = comb(5, 3)
    # Número total de comissões
    total_comissoes = combinacoes_homens * combinacoes_mulheres
    return total_comissoes

resultado_comissoes = calcular_comissoes()
print(f'O número total de comissões que podem ser formadas é: {resultado_comissoes}')

def calcular_comissoes_restritas():
    # Número total de comissões (sem restrições)
    total_comissoes = calcular_comissoes()
    
    # Número de maneiras de escolher 2 homens dos 7 restantes (excluindo o Homem A)
    combinacoes_homens_restantes = comb(7, 2)
    # Número de maneiras de escolher 2 mulheres dos 4 restantes (excluindo a Mulher B)
    combinacoes_mulheres_restantes = comb(4, 2)
    # Número de comissões com Homem A e Mulher B
    comissoes_com_HomemA_e_MulherB = combinacoes_homens_restantes * combinacoes_mulheres_restantes
    
    # Número de comissões válidas (onde Homem A e Mulher B não estão juntos)
    comissoes_validas = total_comissoes - comissoes_com_HomemA_e_MulherB
    return comissoes_validas

resultado_comissoes_restritas = calcular_comissoes_restritas()
print(f'O número de comissões onde o Homem A e a Mulher B não estão juntos é: {resultado_comissoes_restritas}')
