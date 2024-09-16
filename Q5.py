# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 5 - De quantos modos 3 pessoas podem sentar-se em 5 cadeiras em fila?

import math

def cadeiras_restantes (qtd_pessoas):
    cadeiras_restantes= math.prod(qtd_pessoas)
    total_cadeiras = cadeiras_restantes
    return total_cadeiras

qtd_pessoas = [5, 4, 3]
total_cadeiras = cadeiras_restantes (qtd_pessoas)

print("Os modos diferentes que as pessoas podem sentar na cadeira é:", int(total_cadeiras))

# Cada pessoa tem, inicialmente, 5 possibilidades para sentar-se. A primeira pessoa tem 5 cadeiras, a segunda possui 4 cadeiras e a terceira possui 3 cadeiras
#Logo, teremos o seguinte calculo 5x4x3, resultando em 60. 