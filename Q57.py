# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

def count_anagrams(word):
    from collections import Counter
    counts = Counter(word)
    denom = 1
    for count in counts.values():
        denom *= factorial(count)
    return factorial(len(word)) // denom

# Para a palavra "CARAGUATATUBA"
word = "CARAGUATATUBA"
print("Número de anagramas da palavra 'CARAGUATATUBA':", count_anagrams(word))
