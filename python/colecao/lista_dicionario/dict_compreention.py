lista1 = [
    ('chave1',1),
    ('chave2',2),
    ('chave3',3),
    ('chave4',4),
]

def modifica_chave(c):
    return c.upper()

def modifica_valor(v):
    return v*2

d1 = { modifica_chave(x) : modifica_valor(y) for x , y in lista1 }

for c in d1:
    print(f'\nchave: {c}')
    print(f'valor: {d1[c]}\n')
