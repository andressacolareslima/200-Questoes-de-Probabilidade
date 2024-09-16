# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"14 - Quantos números diferentes podem ser formados multiplicando alguns (ou todos) dos números 1,5,6,7,7,9,9,9"

def fatores (escolha_a, escolha_b, escolha_c, escolha_d) :
    fatores = escolha_a * escolha_b * escolha_c * escolha_d
    return fatores
"O número 1 pode ser escolhido quantas vezes quiser, pois ele não afeta o resultado da operação"
" O número 5 pode ser escolhido uma ou duas vezes, então seu expoente será 2"
escolha_a = 2
"O número 6 também poderá ser escolhido uma ou duas vezes, nesse caso seu expoente também será 2"
escolha_b = 2
"Já o número 7 poderá ser escolhido uma, duas ou três vezes, logo seu expoente será 3"
escolha_c = 3
"O número nove aparece 3 vezes, podendo ser escolhido uma, duas, três ou quatro vezes, por isso seu expoente será 4"
escolha_d = 4
"Para descobrir as possibilidades, poderemos multiplicar os expoentes de cada numeral"

total = fatores (escolha_a, escolha_b, escolha_c, escolha_d)

print (f"O numéro de possibildades é {total}")
