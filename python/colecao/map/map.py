from dados import produtos,pessoas,listanum
'''
def dobro(x):
    return x*2
multi = map(dobro,listanum)

for m in multi:
    print(f'{m}')

print(f'{list(multi)}')

for m in multi:
    print(f'{m}')
'''
def aumenta_preco(p):
    p['valor'] = round(p['valor'] * 1.05,2)
    return p

precos = map(aumenta_preco, produtos)  # Funciona com lambda

for p in precos:
    print(f'{p}')
