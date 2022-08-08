'''
try:
	num1="1"
	num2="2.5"

	num3=num1+float(num2)
	print(num3)
except TypeError as error:
	print(f'\nErro: {error}')
	raise
finally:
	print('\n Fim do try/except\n')
x = True
if x:
	pass
else:
	print('PlaceHolder')
'''
def divisao(x,y):
	if y==0:
		raise ZeroDivisionError
	return x/y
try:
	print(divisao(2,0))
except ZeroDivisionError:
	print("não deu pra dividir por '0'!")
