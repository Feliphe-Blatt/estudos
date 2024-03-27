numero = float(input('Digite o número para a tabuada:\n->'))

with open(f'tabuada_do_{numero}.txt', 'w') as tabuada:
    for i in range(1, 11):
        tabuada.write(f'{numero} x {i} = {numero * i}\n')
