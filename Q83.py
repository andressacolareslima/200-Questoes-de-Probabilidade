# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def calcular_modos_iluminacao(n):
    return 2 ** n - 1

n_lampadas = 7
resultado = calcular_modos_iluminacao(n_lampadas)
print(f'Número total de modos de iluminar a sala (com pelo menos uma lâmpada acesa): {resultado}')