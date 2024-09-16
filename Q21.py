# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"22 - O código morse usa palavras contendo de 1 a 4 letras, as letras são pontos e traços. Quantas palavras existem no código morse?"

" Dado o enunciado, podemos organizar o cálculo da seguinte maneira:"
" 1 letra = 2 possibilidades"
" 2 letras = 2x2 possibilidades"
" 3 letras = 2x2x2 possibilidades"
" 4 letras = 2x2x2x2 possibilidades"

"Para encontrar o resultado, somamos todos os produtos dessas quatro possibilidades" 

def palavras (uma_letra, duas_letras, tres_letras, quatro_letras) :
    palavras = uma_letra+duas_letras+tres_letras+quatro_letras
    return palavras

uma_letra = 2
duas_letras = 2*2
tres_letras = 2*2*2
quatro_letras = 2*2*2*2

total = palavras (uma_letra,duas_letras,tres_letras,quatro_letras)

print(f"O o código morse possui {total} palavras")