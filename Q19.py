# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"19 - Quantos são os números de 5 algarismos, base 10:"

"a) nos quais o algarismo 2 figura?"
"b) nos quais o algarismo 2 não figura?"

"Para resolver essa questão, foi calculado a quantidade de numeros que possuem 5 algarismo e a quantidade deles que não possuem o numeral 2,"
"com isso, foi realizada uma subtração entre o primeiro e o segundo resultado e obtevesse a resposta do item a"

import math

def numeros (primeiro_digito, demais_digitos) :
    numeros = (primeiro_digito-demais_digitos)
    return numeros

primeiro_digito = int(9* (math.pow(10,4)))
demais_digitos = int(8* (math.pow(9,4)))
total = numeros(primeiro_digito, demais_digitos)

print (f"Resposta item a): O 2 figura em {total} algarismos")
print (f"Resposta item b): O 2 não figura em {demais_digitos} algarismos")

