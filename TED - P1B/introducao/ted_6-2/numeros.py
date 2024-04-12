import random

vetor = []

for i in range(5):

    numero_temporario = random.randint(10, 20)
    vetor.append(numero_temporario)

for i, num in enumerate(vetor):

    print(f'\nN° {i+1}: {num}\n')
