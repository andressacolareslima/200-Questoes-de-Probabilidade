# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import comb

def count_planes_with_at_least_three_points(total_points, coplanar_points):
    if total_points < 3:
        return 0
    
    total_planes = 0
    for k in range(3, coplanar_points + 1):
        total_planes += comb(coplanar_points, k)
    
    return total_planes

# Para o conjunto C com 20 pontos, onde 8 são coplanares
total_points = 20
coplanar_points = 8
print("Número de planos que contêm pelo menos três pontos de C:", count_planes_with_at_least_three_points(total_points, coplanar_points))
