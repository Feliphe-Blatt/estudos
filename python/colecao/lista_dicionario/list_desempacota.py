lista = [0,1,2,3,4,5,6,7,8,9]

lista2 = [
	["joão",18],["maria",20],["betinho", 25],["bielzon",25],["alberto",30]
]
sep1, sep2, *temp, ultimo = lista2  # utilizar somente "*_" se quiser pular o restante 'temp'
print(sep1)
print(sep2)
print(*temp)
print(ultimo)

sep1, sep2 = sep2, sep1  # troca os valores quaisquer que sejam
print(sep1)
print(sep2)
