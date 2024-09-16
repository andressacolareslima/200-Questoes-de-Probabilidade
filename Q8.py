# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 8 - Quantos divisores naturais possui o número 360? Quantos são pares?

divisores = []
divisores_pares = []

for i in range (1,361) :
    if 360%i==0:
        divisores.append(i) 
        if i%2==0: divisores_pares.append(i)
print ("Quantidades de divisores de 360 é:", len(divisores))
print ("Quantidade de divisores pares de 360 é:", len(divisores_pares))