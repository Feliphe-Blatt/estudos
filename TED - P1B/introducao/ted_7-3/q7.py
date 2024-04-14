import random

V1 = []
V2 = []


# Preenchendo os vetores
for i in range(10):
    V1.append(random.randint(0, 10))
    V2.append(random.randint(0, 10))

contador = 0

for i in range(len(V1)):

    if (V1[i] == V2[i]):
        contador += 1

print(f'\nV1:', V1)
print(f'V2:', V2)

print(f'\nV1 e V2 possuem números iguais com a mesma posição {contador} vezes!\n')
