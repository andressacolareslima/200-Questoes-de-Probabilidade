# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

# Frequências das letras
frequencias = {'A': 5, 'C': 1, 'R': 1, 'G': 1, 'U': 2, 'T': 2, 'B': 1}

# Total de letras
n = 13

# Cálculo do número total de anagramas
anagramas_total = math.factorial(n) // (math.factorial(frequencias['A']) * 
                                        math.factorial(frequencias['C']) * 
                                        math.factorial(frequencias['R']) * 
                                        math.factorial(frequencias['G']) * 
                                        math.factorial(frequencias['U']) * 
                                        math.factorial(frequencias['T']) * 
                                        math.factorial(frequencias['B']))

print("Número total de anagramas:", anagramas_total)

# Número de vogais (A, U) no começo
vogais = ['A', 'U']
anagramas_com_vogal = 0

for vogal in vogais:
    frequencias_vogal = frequencias.copy()
    frequencias_vogal[vogal] -= 1  # Reduz uma ocorrência da vogal escolhida

    anagramas_com_vogal += math.factorial(n - 1) // (math.factorial(frequencias_vogal['A']) *
                                                     math.factorial(frequencias_vogal['C']) *
                                                     math.factorial(frequencias_vogal['R']) *
                                                     math.factorial(frequencias_vogal['G']) *
                                                     math.factorial(frequencias_vogal['U']) *
                                                     math.factorial(frequencias_vogal['T']) *
                                                     math.factorial(frequencias_vogal['B']))

print("Número de anagramas que começam com vogal:", anagramas_com_vogal)
