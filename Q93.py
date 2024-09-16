# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

def soma_coeficientes(expoente):
    resultado = (-1) ** expoente
    return resultado

expoente = 1822

soma = soma_coeficientes(expoente)

print(f"A soma dos coeficientes é: {soma}")