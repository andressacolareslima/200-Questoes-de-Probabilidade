# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 9 - Quantos sao os números naturais de 4 digitos que possuem pelo menos doios digitos iguais?

"Pelo menos dois numeros iguais"
import math

def dois_iguais (numeros_iguais) :
    dois_iguais = math.prod(numeros_iguais)
    return dois_iguais

numeros_iguais = [9, 9, 8, 7]
total_igual = dois_iguais (numeros_iguais)

"Pelo menos três números iguais"

def tres_iguais (numeros_iguais1) :
    tres_iguais = math.prod(numeros_iguais1)
    return tres_iguais

numeros_iguais1 = [9, 9, 9, 8]
total_igual1 = tres_iguais(numeros_iguais1)

"Pelo menos 4 numeros iguais"

def quatro_iguais (numeros_iguais2) :
    quatro_iguais = math.prod(numeros_iguais2)
    return quatro_iguais
numeros_iguais2 = [9, 9, 9, 9]
total_igual2 = quatro_iguais(numeros_iguais2)
resultado_final = total_igual + total_igual1 + total_igual2

print ("O número de possibilidades possiveis para essa problematica é: ",int(resultado_final))
