original = [0,1,2,3,4,5,6,7,8,9]
print(original)

def multiplica(x,y):
    return x*y

def par(x):
    if x%2==0:
        return True
    return False

pares = [i for i in original if par(i)]
print(pares)

quadrado = [i**2 for i in original]
print (quadrado)

multiplicacao = [multiplica(i,3) for i in original]
print (multiplicacao)

frase = "0123456789012345678901234567890123456789012345678901234567890123456789"
print(f'\n{frase}\n')
lista = [frase[n:n+10] for n in range(0,len(frase),10)]
print(f'{lista}\n')
junta = '.'.join(lista)
print(f'{junta}\n')

carrinho = [
    ('batata',1.5),
    ('macarrão',4),
    ('feijão',2.5),
    ('arroz',2),
]
total = sum([float(y) for x,y in carrinho])
print(f' Total do carrinho: R${total:.2f}\n')

