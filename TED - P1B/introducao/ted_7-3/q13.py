import random

numeros = []

for i in range(10):
    numeros.append(random.randint(0, 50))

print('\nNúmeros:', numeros)

def mostra_soma(lista):

    contagem = 0

    for num in numeros:
        
        if ((num % 2) == 0):
            contagem += num
    
    return contagem

print(f'\nSoma os números pares: {mostra_soma(numeros)}\n')
