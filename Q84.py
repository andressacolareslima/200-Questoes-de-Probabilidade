# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

def numero_de_coqueteis(n):
    total_coqueteis = sum(comb(n, k) for k in range(2, n+1))
    return total_coqueteis

# Número de ingredientes
n_ingredientes = 7
resultado = numero_de_coqueteis(n_ingredientes)
print(f'Número total de coquetéis possíveis: {resultado}')