# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 6 - Quantos números de quatro dígitos são maiores que 2400 e:
#c) Tem as propiedades a) e b) simultaneamente

import math

#Numeros iniciados em 2
def num_excluidos (qnt_num): 
    num_excluidos = math.prod (qnt_num)
    total_excluidos = num_excluidos
    return total_excluidos
qnt_num = [1, 4, 7, 6]
total_excluidos = num_excluidos(qnt_num) - 1

#Outros numeros

def num_excluidos2 (qnt_num2) :
    num_excluidos2 = math.prod (qnt_num2)
    total_excluidos2 = num_excluidos2
    return total_excluidos2
qnt_num2 = [4, 6, 5, 4]
total_excluidos2 = num_excluidos2(qnt_num2)

resultado = total_excluidos + total_excluidos2

print ("O resultado utilizando as problematicas dos itens a e b são:", int(resultado))