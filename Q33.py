# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3


from math import factorial

def maneiras_colocar_em_fila(r, m):
    """Calcula o número de maneiras de colocar r rapazes e m moças em fila com as moças juntas."""
    return factorial(r + 1) * factorial(m)

# Exemplo de uso
rapazes = 4  # Número de rapazes
mocas = 3    # Número de moças

resultado = maneiras_colocar_em_fila(rapazes, mocas)
print(f'O número de maneiras de colocar {rapazes} rapazes e {mocas} moças em fila com as moças juntas é: {resultado}')
