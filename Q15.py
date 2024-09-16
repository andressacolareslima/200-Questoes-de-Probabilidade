# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"15 - Um vagão de metrô tem 10 bancos individuais, sendo 5 na frente e 5 de costas. De 10 passageiros, 4 querem"
"sentar de frente, 3 preferem sentar-se de costas e os demais não tem preferencia. De quantas modos os passaageiros podem se sentar, respeitando as preferencias?"

import math 

"Primeiro arranjo com os passageiros que querem sentar-se na frente"
def distribuicao (forma1, forma2) :
    distribuicao = int ((math.factorial(forma1) / math.factorial(forma2) * ((math.factorial(forma1-forma2)))) * math.factorial(forma2))
    return distribuicao
forma1 = 5
forma2 = 4
total1 = distribuicao(forma1, forma2)

"Segundo arranjo com os passageiros que preferem sentar-se de costas"
def distribuicao2(forma1, forma2):
    distribuicao2 = int(math.factorial(forma1) / (math.factorial(forma2) * math.factorial(forma1 - forma2)) * math.factorial(forma2))
    return distribuicao2

forma1 = 5
forma2 = 3
total2 = distribuicao2(forma1, forma2)

"Terceiro e ultimo arranjo com os passageiros que não possuem preferencia ao sentar-se"
def distribuicao3 (forma1) :
    distribuicao3 = math.factorial(forma1)
    return distribuicao3
forma1 = 3
total3 = distribuicao3(forma1)

total = int(total1*total2*total3) 
print(f"O total de combinações nas quais os passageiros podem sentar-se é {total}")