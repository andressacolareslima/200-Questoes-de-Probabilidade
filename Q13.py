# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 13 -  De um baralho comum (52 cartas) sacam-se sucessivamente e sem posição três cartas. Quantas são as extrações
# nas quais a primeira carta é de copas, a segunda é um rei e a terceira não é uma dama?

"Quando a primeira carta é um rei de copas - Caso 1"

def caso1 (numero_damas, numero_reis, numero_copas):
  caso1 = numero_copas * numero_reis * numero_damas
  return caso1

numero_copas = 1
numero_reis = 3
numero_damas = 46

total1 = caso1(numero_damas, numero_reis,numero_copas)

"Primeira carta não é um rei de copas - Caso 2"
def caso2 (numero_damas,numero_copas,numero_reis):
    caso2 = numero_copas * numero_reis * numero_damas
    return caso2

numero_copas = 11
numero_reis = 4
numero_damas = 46

total2 = caso2(numero_damas,numero_reis,numero_copas)

"Quando a primeira carta é uma dama de copas - Caso 3"

def caso3 (numero_damas, numero_reis,numero_copas) :
   caso3 = numero_copas*numero_reis*numero_damas
   return caso3

numero_copas = 1
numero_reis = 4
numero_damas = 47

total3 = caso3 (numero_damas,numero_copas,numero_reis)

resultado = total1 + total2 + total3

print (f"O número de extrações possíveis é {resultado}")