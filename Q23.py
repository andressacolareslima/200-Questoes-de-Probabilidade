# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"23 - Escrevem-se números de cinco dígitos (inclusive os começados por"
"zero) em cartões. Como 0,1 e 8 não se alteram de cabeça para baixo e como"
"6 de cabeça para baixo se transforma em 9, um só cartão pode representar"
"dois números (por exemplo, 06198 e 86190). Qual é o número mínimo de"
"cartões para representar todos os números de cinco dígitos?"

"O número total de cartões é 10^5 = 100000"
"Como a questão exige o mínimo de cartões possivéis, há duas possibilidades:"
"Os que virados de cabeça para baixo representam o mesmo número e os que virados de cabeça para baixo representam outro número"

"Para a primeira situação temos 5 algarismos, 0,1,6,8,9 na qual os números 0,1 e 8 estão inclusos. Para isso eles precisam ser 0 e 0 no primeiro e ultimo digito. "
"ou 1 e 1 no primeiro e ultimo digito, ou 6 e 9  no primeiro e ultimo digito, os algarismos do meio so podem ser ocupados, por 0,1 ou 8, e as demais possições por um dos cinco números citadosm, ficando com o seguinte cálculo = 1x5x5x3x1"
"A segunda situação podemos usar os cinco algarismos, 0,1,6,8,9 ficando com o seguinte calculo 5x5x5x5x5 "
"Com isso, temos o produto da segunda situação, subtraída com o produto da primeira situação o resultado dessa conta, iremos subtratir do número total de cartões, obtendo o número mínimo de cartões"

import math 

def min_cartoes (max_cartoes, p1, p2):
    min_cartoes = max_cartoes - ((p1-p2)/2)
    return min_cartoes

max_cartoes = math.pow (10,5)
p1 = math.pow (5,5)
p2 = 3*math.pow (5,2)

total = int (min_cartoes(max_cartoes,p1,p2))

print (f"O minímo de cartões possíveis é {total}")