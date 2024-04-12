import random

# Criando um vetor Q e gerando 20 números de 0 a 100
Q = []

for i in range(20):
    Q.append(random.randint(0, 100))

# Tuplas para guardar os maiores e menores números e suas posições
# Números estão -1 e 101 de propósito
maior = (-1, 0)
menor = (101, 0)

for i, num in enumerate(Q):
    
    if (maior[0] < num):
        maior = (num, i)
        
    if (menor[0] > num):
        menor = (num, i)

print(f'\nVetor Q:', Q)

print(f'\nO maior elemento gerado foi: {maior[0]} que está no índice {maior[1]}\n')
print(f'\nO menor elemento gerado foi: {menor[0]} que está no índice {menor[1]}\n')
