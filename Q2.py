# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 2 - Quantos são os gabaritos possíveis de um teste de 10 questões de multipla escolha, com cinco alternativas por questão?
import math

def possibilidades (qnt_respostas):
    qnt_respostas = [0]
qnt_respostas = math.pow (5,10)
possibilidades = qnt_respostas

print ("Quantidade de respostas diferentes para essa problematica é:", int (possibilidades))

#Explicação do código: Esta questão exige um conhecimento básico de combinações. Como enunciado não especifica se as letras necessitam ser diferentes
# o cálculo utilizado foi 5x5x5x5x5x5x5x5x5x5 (ou 5^10 para este caso em especifico). A biblioteca math.pow foi utilizado para o calculo da pontenciação de expoente 10, para chegar no resultado 9765625.
