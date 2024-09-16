# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def calcular_selecao():
    # Número de maneiras de escolher 1 goleiro de 2
    goleiros = comb(2, 1)
    
    # Número de maneiras de escolher 4 zagueiros de 6
    zagueiros = comb(6, 4)
    
    # Número de maneiras de escolher 4 meios de campo de 7
    meios_de_campo = comb(7, 4)
    
    # Número de maneiras de escolher 2 atacantes de 4
    atacantes = comb(4, 2)
    
    # Número total de maneiras de escalar a seleção
    total_maneiras = goleiros * zagueiros * meios_de_campo * atacantes
    return total_maneiras

resultado_selecao = calcular_selecao()
print(f'O número de maneiras de escalar a seleção é: {resultado_selecao}')
