# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"25 -  a) Qual a soma dos divisores inteiros e positivos de 720?"

divisores = []

for i in range (1,721) :
    if 720%i==0:
        divisores.append(i)
soma = sum(divisores)

print (f"Resposta item a) A somados divisores inteiro e positivos de 720 é {soma}")

"b) De quantos modos 720 pode ser decomposto em um produto de dois inteiros positivos?"

int_positivos = len(divisores)
descomposto = int (int_positivos / 2)

print (f"Resposta item b) 720 pode ser decomposto de {descomposto} formas ")

"c) De quantos modos De quantos modos 720 pode ser decomposto em um produto de três inteiros positivos? "

"720 não é um cubo perfeito por isso não existe em sua decomposição uma tupla do tipo a*a*a, porém, temos a variação a*a*b, que aparece 6 vezes na decomposição"
"Sendo elas, 1*1*720, 2*2*180, 3*3*80, 4*4*45, 5*5*20, 6*6*20 e 12*12*5"
"270 é o número de combinações"
"3*6 é a quantidade de combinações no formato a*a*b"
"6 é o numeros de tuplas do formato a*a*b que existem nos divisores de 720"

num_combinacoes = 270
qtd_combinacoes = 3*6
tuplas = 6

total = int(((num_combinacoes - qtd_combinacoes) / tuplas) + tuplas)

print (f"Resposta item c) 720 pode ser decomposto em um produto de três inteiros positivos de {total} formas")

"d) De quantos modos 144 pode ser decomposto em um produto de dois inteiros positivos?"
"144 pode ser formado por 4 pares de divisores, o 12x12 não foi contado neste calculo, por isso o 1 representa essa expressão"

divisores_1 = []

for x in range (1,145) :
    if 144%x==0:
        divisores_1.append(x)
int_positivos1 = len(divisores_1)
total1 = int(int_positivos1/2) + 1

print(f"Resposta item d) 144 pode ser decomposto de {total1} formas")