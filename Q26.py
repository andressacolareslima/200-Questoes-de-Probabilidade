# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import math

# Fatorial de um número
def fatorial(n):
    return math.factorial(n)

# Contagem de anagramas totais
def anagramas_totais(palavra):
    return fatorial(len(palavra))

# a) Anagramas que começam por consoante e terminam por vogal
def anagramas_consoante_vogal(palavra, consoantes, vogais):
    # Escolher uma consoante para o início e uma vogal para o fim
    return len(consoantes) * len(vogais) * fatorial(len(palavra) - 2)

# b) Anagramas com C, A, P juntos nessa ordem
def anagramas_cap_ordem(palavra):
    # Considerando CAP como uma única "letra"
    return fatorial(len(palavra) - 2)

# c) Anagramas com C, A, P juntos em qualquer ordem
def anagramas_cap_qualquer_ordem(palavra):
    return fatorial(len(palavra) - 2) * fatorial(3)

# d) Anagramas com vogais e consoantes intercaladas
def anagramas_intercaladas(vogais, consoantes):
    return fatorial(len(vogais)) * fatorial(len(consoantes))

# e) Anagramas com C no 1º lugar e A no 2º lugar
def anagramas_c1_a2(palavra):
    return fatorial(len(palavra) - 2)

# f) Anagramas com C no 1º lugar ou A no 2º lugar
def anagramas_c1_ou_a2(palavra):
    total_possibilidades = 2 * fatorial(len(palavra) - 2)  # C no 1º ou A no 2º
    c1_a2_juntos = fatorial(len(palavra) - 2)  # C no 1º E A no 2º
    return total_possibilidades - c1_a2_juntos

# Palavra e seus elementos
palavra = "CAPÍTULO"
consoantes = [c for c in palavra if c not in 'AEIOUÁÉÍÓÚ']
vogais = [v for v in palavra if v in 'AEIOUÁÉÍÓÚ']

# Cálculos
resultados = {
    'a': anagramas_consoante_vogal(palavra, consoantes, vogais),
    'b': anagramas_cap_ordem(palavra),
    'c': anagramas_cap_qualquer_ordem(palavra),
    'd': anagramas_intercaladas(vogais, consoantes),
    'e': anagramas_c1_a2(palavra),
    'f': anagramas_c1_ou_a2(palavra)
}

resultados
