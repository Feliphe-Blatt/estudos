from functools import reduce
from dados import produtos,pessoas,listanum

original = [0,1,2,3,4,5,6,7,8,9,10]

def soma(x,y):
	return x+y

soma = reduce(soma, original,0)
print(soma)

preco_medio = reduce(lambda x,p : p['valor'] + x , produtos,0)
preco_medio = preco_medio/len(produtos)
print(f'{preco_medio}')
