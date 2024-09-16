# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"16 - Há duas entradas principais da cidade A até a cidade B, ligadas por 10 estradas secundárias, como na figura 2.2"
"Quantas rotas livres de autoinserções há de A até B?"

"Para chegar até a cidade B, o motorista poderá optar por 11 caminhos"

"Partindo da cidade A para a primeira estrada só terá um caminho, porém, as direções são duas, por isso"
"a expressão ficará = 2¹"

"Chegando da estrada secundária, S1 à S10 ele poderá continuar na secundária ou optar por outra, obtendo a seguinte expressão = 2^10"

"Dessa forma, para chegarmos o número de possibilidades teremos 2¹+2^10 = 2^11"

import math 

def estradas (s1):
    estradas = s1
    return estradas

s1 = int(math.pow (2,11))

print(f"O número de autoinserções entre as duas estradas é {s1}")


    