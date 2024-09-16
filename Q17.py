# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"17 - Quantos números entre 100 e 999 são ímpares e possuem três digitos distintos?"

"Para o primeiro digito, temos 8 possibilidades (excluindo o número 0 e ele precisa ser diferente do último algarismo )"
"Para o segundo também temos 8 possibilidades (excluindo o primeiro digito e o ultimo e o zero, nesta situação pode ser escolhido)"
"Para o terceiro e último, dentre os 10 algarismo temos 5 possibilidades"

import math 

def distintos (quantidade):
    distintos = math.prod(quantidade)
    return distintos

quantidade = [5,8,8]
total = distintos(quantidade)
print (f"A quantidade de números que podemos escrever é {total}")