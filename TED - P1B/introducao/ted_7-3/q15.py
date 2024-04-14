banco_de_horas = (
    (7, 12),
    (13, 18),
    (7, 9.5)
)

soma = 0

for tup in banco_de_horas:

    soma += (tup[1] - tup[0])

print(f'\nTotal das horas trabalhadas: {soma}\n')
