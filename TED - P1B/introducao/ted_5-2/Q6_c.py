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

print('--------------------------------------\n')
