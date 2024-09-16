# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def calcular_diagonais(n):
    if n < 3:
        return 0  # Um polígono com menos de 3 lados não possui diagonais
    diagonais = (n * (n - 3)) // 2
    return diagonais

# Exemplo de uso:
n = 6  # Número de lados do polígono
resultado_diagonais = calcular_diagonais(n)
print(f'O número de diagonais em um polígono de {n} lados é: {resultado_diagonais}')
