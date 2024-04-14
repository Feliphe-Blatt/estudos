import random

V1 = []

# Preenchendo o vetor
for i in range(30):
    V1.append(random.randint(0, 10))

compara = int(input('\nDigite um número para achar no vetor:\n-> '))

contador = 0

for num in V1:

    if (compara == num):
        contador += 1

print("\nVetor:", V1)

print(f'\nO número "{compara}" aparece {contador} vezes dentro do vetor!\n')
