# Listas principais utilizadas
VET = []
repetidos = []

# Input dos valores no vetor VET
for i in range(10):

    VET.append(float(input(f'\nDigite o numero {i+1}:\n-> ')))

# Percorrendo os elementos de VET para identificar ocorrências múltiplas
for i, numero in enumerate(VET):

    contador = 0
    posicoes = []

    for j, compara in enumerate(VET):

        # Se for igual (vai ser ao menos uma vez)
        if (numero == compara):

            contador += 1
            posicoes.append(j)

    if (contador != 1):
        repetidos.append([numero, contador, tuple(posicoes)])

# Retirando as redundâncias com 'set'
repetidos_filtrados = [list(tup) for tup in set(map(tuple, repetidos))]

print(VET)

for rep in repetidos_filtrados:

    # Número em si
    numero = rep[0]

    # Quantidade de repetições
    quantidade = rep[1]

    # Índices que aparece em VET
    indices = rep[2]

    print(f'O número {numero} repete {quantidade} vezes nos índices: {indices}')
