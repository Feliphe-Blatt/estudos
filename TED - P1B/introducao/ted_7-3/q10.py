from random import sample

matriz = []

# Lista de números disponíveis para colocar na matriz sem repetir de 0 a 200
disponiveis = list(range(201))

# Gera cada linha com os números ainda não usados e salva na matriz
for coluna in range(10):

    linha = sample(disponiveis, 10)
    matriz.append(linha)

    # Retira dos disponíveis os números utilizados
    for num in linha:
        disponiveis.remove(num)

# Exibindo a matriz
print("\nMatriz:")

for linha in matriz:
    print(linha)

# Tupla contendo informações do maior número encontrado e posição
maior = (-1, 0, 0)

for i, linha in enumerate(matriz):
    for j, num in enumerate(linha):

        # Atualiza as informações do maior número
        if (maior[0] < num):
            maior = (num, i+1, j+1)

# Exibindo o maior número e sua posição
print(f'\nO maior número é {maior[0]} que fica na linha {maior[1]} e coluna {maior[2]}...\n')
