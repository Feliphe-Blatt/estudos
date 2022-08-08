while(input('\n\tEnter para calcular ou digite "sair" para fechar o programa: ') != "sair"):
	try:
		a = float(input("Um valor para a: "))
		sinal = input("Operação: ")
		b = float(input("Um valor para b: "))

		if sinal == '+':
			print("a + b =",a+b)
		elif sinal == '-':
			print("a - b =",a-b)
		elif sinal == '*':
			print("a * b =",a*b)
		elif sinal == '/':
			print("a / b =",a/b)
		elif sinal == "**":
			print("a**b =",a**b)
		elif sinal == "//":
			print("a//b =",a//b)
		elif sinal == "%":
			print(r"a%b =",a%b)
		else:
			print("Caractere de sinal inválido!")
			
		flag_calc = input('Digite "sair" para sair da calculadora:\n ->')
	except:
		print("Opção inválida!")
