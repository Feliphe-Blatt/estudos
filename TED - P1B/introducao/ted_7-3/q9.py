from random import sample

D = []

# Lista de números disponíveis para colocar na matriz sem repetir de 0 a 50
disponiveis = list(range(51))

# Gera cada linha com os números ainda não usados e salva em 'D'
for coluna in range(5):

    linha = sample(disponiveis, 5)
    D.append(linha)

    # Retira dos disponíveis os números utilizados
    for num in linha:
        disponiveis.remove(num)

compara = int(input('\nDigite um número para procurar na matriz:\n-> '))

# Exibindo a matriz
print("\nMatriz 'D':")

for linha in D:
    print(linha)

# Indicador se achou ou não o número
achei = False

# Procura o numero na matriz e se achar altera o indicador
for linha in D:
    for numero in linha:

        if (numero == compara):
            achei = True

# Exibindo se existe ou não
if (achei):
    print(f'\nO número {compara} EXISTE dentro da matriz "D"!\n')

else:
    print(f'\nO número {compara} NÃO EXISTE dentro da matriz "D"!\n')
