A = [11, 22, 33, 44, 55, 66, 77, 88, 99, 0]

X = float(input('Digite um número para multiplicar os valores de A:\n->'))

M = []

for num in A:

    M.append(num * X)

print(f'Vetor M:', M)
