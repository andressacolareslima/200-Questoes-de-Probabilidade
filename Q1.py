# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 1 - Quantas palavras contendo 3 letras podem ser formadas em um alfabeto de 26 letras?
import math

def possibilidades (qnt_palavras):
    qnt_palavras = [26]
    return qnt_palavras
qnt_palavras = math.pow (26,3)
possibilidades = qnt_palavras

print ("Quantidade de palavras para essa problematica é:", int (possibilidades))

#Explicação do código: Esta questão exige um conhecimento básico de combinações. Como enunciado não especifica se as letras necessitam ser diferentes
# o cálculo utilizado foi 26x26x26 (ou 26³ para este caso em especifico). A biblioteca math.pow foi utilizado para o calculo da pontenciação de expoente 3, para chegar no resultado 17576.
