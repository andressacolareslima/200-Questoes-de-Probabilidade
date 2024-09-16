# Questões retiradas do livro Análise Combinatória e Estatística
# Autores: Augusto Cezar de Oliveira Morgado, João Bosco Pitombeira, Paulo Cezar Pinto Carvalho, Pedro Fernandez
# Edição: 10º edição
# Ano de lançamento : 2016
# ISBN : 978-85-8337-083-3

# 12 - Em uma banca, há 5 exemplares iguais da revista A, 6 exemplares iguais da revista B e 10 exemplares iguais da revista C.
# Quantas coleções não vazias de revistas dessa banca é possivel formar? 

def tres_revistas (revistas1, revista2, revista3):
    tres_revistas = revistas1*revista2*revista3
    return tres_revistas

revistas1 = 5
revistas2 = 6
revistas3 = 10
total_tres_revistas = tres_revistas(revistas1, revistas2, revistas3)
total_duas_revistas = revistas1 * revistas2 + revistas1 * revistas3 + revistas2 * revistas3
total_uma_revista =  revistas1 + revistas2 + revistas3
total = total_tres_revistas + total_duas_revistas + total_uma_revista

print(f"O total de coleções não vazias é com as três revistas é {total}")

