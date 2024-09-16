# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

import itertools

# Algoritmo para a questão a) Que lugar ocupa o número 62417?

# Os dígitos disponíveis
digitos = [1, 2, 4, 6, 7]

# Encontrar todas as permutações possíveis
permutacoes = sorted(itertools.permutations(digitos))

# Convertendo a lista de dígitos para um número
numero_alvo = tuple([6, 2, 4, 1, 7])

# Encontrar a posição do número 62417 na lista de permutações
posicao_62417 = permutacoes.index(numero_alvo) + 1

# Algoritmo para a questão b) Qual o número que ocupa o 66º lugar?

# Encontrar a 66ª permutação
permutacao_66 = permutacoes[65]  # O índice é 65 porque a indexação começa do 0

# Convertendo para um número inteiro
numero_66 = int(''.join(map(str, permutacao_66)))

posicao_62417, numero_66

# Questão c) Qual o 200º algarismo escrito?

# Para resolver isso, devemos entender que queremos o 200º dígito (algarismo)
# se listarmos todos os números gerados pelas permutações consecutivamente.

# Vamos concatenar todas as permutações como uma única string
todos_algarismos = ''.join(''.join(map(str, p)) for p in permutacoes)

# O 200º algarismo é o que está na posição 199 (índice 198, porque a indexação começa do 0)
algarismo_200 = todos_algarismos[199]

# Questão d) Qual a soma dos números assim formados?

# A soma de todas as permutações pode ser calculada convertendo cada permutação em um número
# e somando-os todos.
soma_total = sum(int(''.join(map(str, p))) for p in permutacoes)

algarismo_200, soma_total
