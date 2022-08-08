#////////////////////////////////////////////////////////////////////////////////////////////////
# Decorador: imprime retorno das operações

def decorador(func):
    def wrapper(*args, **kwargs):

        print('\n'+'#'*40)

        resultado = func(*args,**kwargs)
        print(f'\n{resultado}\n')

        print('#'*40)

        return resultado
    return wrapper

#////////////////////////////////////////////////////////////////////////////////////////////////
# Operações disponíveis: Calcula e retorna resultado

@decorador
def soma(x,y):
    return f'X + Y = {x+y:.2f}'

@decorador
def subtrai(x,y):
    return f'X - Y = {x-y:.2f}'

@decorador
def divide_normal(x,y):
    return f'X / Y = {x/y:.2f}'

@decorador
def divide_inteiro(x,y):
    return f'X // Y = {x//y}'

@decorador
def divide_resto(x,y):
    return f'X % Y = {x%y}'

@decorador
def multiplica(x,y):
    return f'X * Y = {x*y:.2f}'

@decorador
def exponencial(x,y):
    return f'X ** Y = {x**y:.2f}'

#////////////////////////////////////////////////////////////////////////////////////////////////
# Menu Principal: Responsável por escolher qual operação a ser executada entre X e Y

print('\n'+'#'*80)

while(input('\n\tEnter para calcular ou digite "sair" para fechar o programa: ') != "sair"):
	try:
		x = float(input("\n\tX = "))
		operador = input("\n\tOperador( +, -, *, /, **, //, % ): ")
		y = float(input("\n\tY = "))

		if operador == '+':
			soma(x,y)

		elif operador == '-':
			subtrai(x,y)

		elif operador == '*':
			multiplica(x,y)

		elif operador == '/':
			divide_normal(x,y)

		elif operador == "**":
			exponencial(x,y)

		elif operador == "//":
			divide_inteiro(x,y)

		elif operador == "%":
			divide_resto(x,y)

		else:
			print('\n\t'+'#'*18+"\n\tOperador inválido!\n\t"+'#'*18+'\n')
	except:
		print("\n\tNúmero inválido!")
