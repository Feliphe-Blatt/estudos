lista1 = [0,1,2,3,4,5,6,7,8,9]

lista2 = ["joão","maria","fulano","cicrano","marcos","polo","feliphe","cristiane","jair","elias","último"]

lista3 = [9,8,7,6,5,4,3,2,1,0]

for cres,nome,decres in zip(lista1,lista2, lista3):
	print(cres, nome, decres)

print('#'*20)
from itertools import zip_longest

for cres, nome, decres in zip_longest(lista1, lista2, lista3, fillvalue='-'):
	print(cres, nome, decres)
