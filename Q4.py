# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 4 - De quantos modos diferentes podem ser escolhidos um presidente e um secretário de um conselho que tem 12 membros?

import math

def presidente_secretario(votos_membros):
  presidente_secretario = math.prod(votos_membros)
  total_votos = presidente_secretario

  return total_votos

votos_membros = [12, 11]
total_votos = presidente_secretario(votos_membros)

print("Os modos diferentes para escolha distintas de presidente e secretário é:", int(total_votos))

#Explicação do código: Cada membro, inicialmente, possui 12 possibilidades para o primeiro voto
# (contando a si mesmo), restando 11 possibilidades para tecer o segundo voto. Sendo assim, o cálculo ficará
#12x11, resultando em 132 formas distintas para votar.