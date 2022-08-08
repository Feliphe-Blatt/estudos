lista = [0,1,2,3,4,5,6,7,8,9]

lista2 = [
	["joão",18],["maria",20],["betinho", 25]
]

for indice, valor in enumerate(lista):
	print(indice, valor, sep="-",end=' ')
print('')

for indice, tabela in enumerate(lista2):
	print(indice, end='->')
	nome, idade = tabela
	print(f'nome: {nome} idade: {idade}')
print('')