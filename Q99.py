# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import comb

total_arranjos = comb(12, 4)

arranjos_consecutivos = 9

arranjos_nao_consecutivos = comb(9, 4)

probabilidade_consecutivos = arranjos_consecutivos / total_arranjos
probabilidade_nao_consecutivos = arranjos_nao_consecutivos / total_arranjos

print(f"Probabilidade de vagas vazias serem consecutivas: {probabilidade_consecutivos:.4f}")
print(f"Probabilidade de não haver duas vagas vazias consecutivas: {probabilidade_nao_consecutivos:.4f}")