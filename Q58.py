# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


def max_intersections(n,comb):
    if n < 4:
        return 0
    return comb(n, 4)

# Exemplo para n pontos
n = 5  # Substitua n pelo valor desejado
print("Número máximo de pontos de interseção de retas com", n, "pontos:", max_intersections(n))
