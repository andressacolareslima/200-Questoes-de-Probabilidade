# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def gerar_triangulo_pascais(n_linhas):
    triangulo = [[1]]  

    for i in range(1, n_linhas):
        linha_anterior = triangulo[-1]
        nova_linha = [1]  
        for j in range(1, len(linha_anterior)):
            nova_linha.append(linha_anterior[j - 1] + linha_anterior[j])
        nova_linha.append(1)  
        triangulo.append(nova_linha)

    return triangulo

def imprimir_triangulo(triangulo):
    for linha in triangulo:
        print(' '.join(map(str, linha)).center(40)) 
n_linhas = 7
triangulo_pascais = gerar_triangulo_pascais(n_linhas)
imprimir_triangulo(triangulo_pascais)