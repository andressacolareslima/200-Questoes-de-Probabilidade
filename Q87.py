# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

from math import factorial

def combinacao(n, k):
  return factorial(n) // (factorial(k) * factorial(n-k))

n = 21

for p in range(n+1):
  resultado = combinacao(n, p)
  print(f"C({n}, {p}) = {resultado}")