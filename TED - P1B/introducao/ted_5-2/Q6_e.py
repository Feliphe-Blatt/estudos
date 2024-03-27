celebridades = ["Padre marcelo Rossi", "Tiririca",
                "Richard Rasmussen", "Angélica", "Luciano hulk"]

print('\n--------------------------------------\n')

for pessoa in celebridades:
    print(f'Olá {pessoa}, vem jantar aqui!\n')

nao_pode_ir = ["Luciano hulk"]

print('--------------------------------------\n')

for pessoa in celebridades:

    for n in nao_pode_ir:

        if n == pessoa:

            print(f'Eita! {pessoa} não pôde vir!\n')

            posicao = celebridades.index(f'{n}')

            celebridades[posicao] = input(
                'Digite o nome da pessoa a substituir:\n->')

print('------------ Nova Lista: -------------\n')

for pessoa in celebridades:
    print(f'Olá {pessoa}, vem jantar aqui!\n')

print('--------------------------------------\n')
