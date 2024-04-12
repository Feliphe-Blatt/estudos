N = []

A = [11, 22, 33, 44, 55, 66, 77, 88, 99, 0]
B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(A)):

    soma = A[i] + B[i]
    N.append(soma)

print(f'\nVetor A:', A)

print(f'\nVetor B:', B)

print(f'\nVetor N:', N, "\n")