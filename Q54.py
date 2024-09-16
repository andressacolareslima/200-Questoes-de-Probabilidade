# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def divide_into_two_groups_of_10(total_people, comb):
    if total_people != 20:
        return 0
    return comb(total_people, 10) // 2

print("Número de maneiras de dividir 20 pessoas em dois grupos de 10:", divide_into_two_groups_of_10(20))

def divide_into_four_groups_of_5(total_people):
    if total_people != 20:
        return 0
    from math import factorial
    return factorial(total_people) // (factorial(5) ** 4 * factorial(4))

print("Número de maneiras de dividir 20 pessoas em quatro grupos de 5:", divide_into_four_groups_of_5(20))

def divide_into_group_of_12_and_8(total_people,comb):
    if total_people != 20:
        return 0
    return comb(total_people, 12)

print("Número de maneiras de dividir 20 pessoas em um grupo de 12 e um de 8:", divide_into_group_of_12_and_8(20))

def divide_into_three_groups_of_6_and_one_of_2(total_people):
    if total_people != 20:
        return 0
    from math import factorial
    return factorial(total_people) // (factorial(6) ** 3 * factorial(2) * factorial(4))

print("Número de maneiras de dividir 20 pessoas em três grupos de 6 e um de 2:", divide_into_three_groups_of_6_and_one_of_2(20))

