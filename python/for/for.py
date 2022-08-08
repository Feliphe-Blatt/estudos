# continue
# break
'''
teste = 'python'

for n, letra in enumerate(teste):
    print(n, letra)
'''

teste = 'python'
inicio = 0
fim = len(teste)
passo = 1

for letra in range(inicio, fim, passo):
    if teste[letra] == 'h':
        continue
    elif teste[letra] == 'n':
        break
    else:
        print(teste[letra])
