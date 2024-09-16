# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def encontrar_tamanho_conjunto(subconjuntos_desejados):
    for n in range(1, 21): 
        num_subconjuntos = 2 ** n
        if num_subconjuntos == subconjuntos_desejados:
            return n
    return None

subconjuntos_desejados = 48
tamanho_conjunto = encontrar_tamanho_conjunto(subconjuntos_desejados)

if tamanho_conjunto is not None:
    print(f'Um conjunto com exatamente {subconjuntos_desejados} subconjuntos deve ter {tamanho_conjunto} elementos.')
else:
    print(f'Não é possível ter um conjunto com exatamente {subconjuntos_desejados} subconjuntos.')