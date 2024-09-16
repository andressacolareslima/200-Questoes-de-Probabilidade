# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import comb

def calcular_funcoes_crescentes(m, n):
    if m > n:
        return 0  # Não é possível escolher m elementos de um conjunto menor que m
    return comb(n, m)

# Exemplo: Calcular para m = 3 e n = 5
m = 3
n = 5
resultado_funcoes = calcular_funcoes_crescentes(m, n)
print(f'O número de funções estritamente crescentes é: {resultado_funcoes}')
