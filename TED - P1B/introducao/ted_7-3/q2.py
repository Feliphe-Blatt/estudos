alunos = {'Mariana': 8, 'Feliphe': 7, 'Cristiane': 8, 'Cauã': 9, 'Pedro': 10}
total = 0
acima_da_media = 0

for chave, valor in alunos.items():
    total += valor

media = total / 5

for chave, valor in alunos.items():

    if (valor > media):
        acima_da_media += 1

print(f'\n-A média da turma é: {media}\n-E {acima_da_media} alunos estão acima da média da turma!\n')
