import random

matriz_A = []
matriz_B = []

for i in range(10):

    linha_A = []

    for j in range(10):

        linha_A.append(random.randint(1, 100))

    matriz_A.append(linha_A)

print('\n-> Matriz A:\n')
for lin in matriz_A:

    print(lin)

print('\n')

soma = 0

for linha in matriz_A:

    for numero in linha:

        soma += numero

print(f'A soma dos números é: {soma}\n')

for linha in matriz_A:

    linha_B = []

    for numero in linha:

        linha_B.append(numero * 3)

    matriz_B.append(linha_B)

print('\n-> Matriz B:\n')
for lin in matriz_B:

    print(lin)

print('\n')
