from random import sample

vetor = []

vetor = sample(range(101), 20)

compara = int(input('\nDigite um número inteiro para tentar achar na lista:\n-> '))

novo_vetor = []
achou = False

for num in vetor:
    if (num == compara):
        achou = True

if (achou):

    for num in vetor:
        if (num != compara):
            novo_vetor.append(num)

    print(f'\nVetor modificado:', novo_vetor, "\n")
else:
    print(f'\nVetor original:', vetor, "\n")

