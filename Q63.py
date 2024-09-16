# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def dinner_invites(n_students, days, group_size):
    from math import comb
    total_pairs = comb(n_students, 2)
    # O número de maneiras de escolher grupos de tamanho `group_size` sem repetir pares
    return comb(total_pairs, days * comb(group_size, 2))

# Exemplo para 7 alunos e 7 jantares
n_students = 7
days = 7
group_size = 3
print("Número de modos de fazer os convites:", dinner_invites(n_students, days, group_size))
