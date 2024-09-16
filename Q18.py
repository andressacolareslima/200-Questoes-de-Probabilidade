# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"18 - Escrevem-se os inteiros de 1 até 222222. Quantas vezes o algarismo 0 é escrito?"

"Para essa questão, podemos analisar da seguinte forma: "

"Quando o 0 está na casa das unidades = 1*22222"
"Quando o 0 está na casa das dezenas = 10*2222"
"Quando o 0 está na casa das centenas = 100*222"
"Quando o 0 está casa das unidades de milhar = 1000*22"
"Quando o 0 está na casa das dezenas de milhar 10000*2"
"Após somar todas essas possibilidades teremos a quantidade de vezes que o número 0 foi escrito"

def quantidade_zero (uni,dez,cem,uni_mil,dez_mil) :
    quantidade_zero = (uni + dez + cem + uni_mil + dez_mil)
    return quantidade_zero
uni = 1*22222
dez = 10*2222
cem = 100*222
uni_mil = 1000*22
dez_mil = 10000*2

total = quantidade_zero(uni,dez,cem,uni_mil,dez_mil)

print (f"O algorismo 0 é escrito {total} vezes")