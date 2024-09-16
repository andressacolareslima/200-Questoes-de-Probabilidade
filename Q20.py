# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

"20 - Em um concurso há três candidatos e cinco examinadores, devendo cada examinador votar em um canditado."
"De quantos modos os votos podem ser distribuidos?"

"Cada examinador possui 3 possibilidades de votos, ficando 3x3x3x3x3"

import math

examinadores = int (math.pow(3,5))

print (f"O total de possibilidades é {examinadores}")