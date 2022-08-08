from dados import produtos,pessoas,listanum
"""
original = [0,1,2,3,4,5,6,7,8,9]
def pares(i):
	if i%2==0:
		return i

pares = list(filter(lambda i: i%2==0,listanum))

for n in pares:
	print(f'{n}')
"""
def maior_2(p):
	if p['valor'] > 2:
		return True

lista1 = filter(maior_2,produtos)

for produto in lista1:
	print(produto)
