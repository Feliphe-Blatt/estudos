"""
Separa duas sequências de dna em formato '.fasta' e organiza em um dicionário 'sequencias'

O formato fasta tem o seguinte layout (usando inclusive o '>'):

>Cabeçalho identificando sequência de DNA (quebra de linha)
Sequência

"""
import os
os.system("cls")
flag_menu = True
#feedBack das funções utilizadas
feedback = ""
sequencias = {}
"""
Lê arquivo '.fasta' e compara as sequências (funciona com .txt também, contanto que esteja organizado em formato Fasta)
"""
def arq_ler():
	try:
		global sequencias
		nome = input("Nome do arquivo a ser lido/gravado: ")
		arq = open(nome, "r")

		linhas = arq.readlines()
		for linha in linhas:
			if linha[0] == ">":
				cab = linha[1:].strip()
				sequencias[cab] = ""
			else:
				sequencias[cab] += linha.strip()

		return "Arquivo lido e sequencias gravadas!"
		#return f'{sequencias}'
	except:
		return "Não foi possível acessar o arquivo!"

#////////////////////////////////////////////////////////////////////////////////////////////////
def arq_sobrepor():
	try:
		nome = input("Nome do arquivo a ser criado/sobreposto: ")
		arq = open(nome, "w")
		cab = input("Cabeçalho da nova sequência: ")
		seq = input ("Sequência: ")
		arq.write(">" + cab + "\n" + seq + "\n")
		arq.close()
		return "Sequência subtituida!"
	except:
		return "Algo deu errado, tente novamente!"
#////////////////////////////////////////////////////////////////////////////////////////////////
def arq_add():
	try:
		nome = input("Nome do arquivo a ser criado/concatenado: ")
		arq = open(nome, "a")
		cab = input("Cabeçalho da nova sequência: ")
		seq = input ("Sequência: ")
		arq.write(">" + cab + "\n" + seq + "\n")
		arq.close()
		return "Sequência concatenada!"
	except:
		return "Algo deu errado, tente novamente!"
#////////////////////////////////////////////////////////////////////////////////////////////////
while(flag_menu):
	menu = input("\n1- Ler arquivo '.fasta' e gravar em dicionário;\n 2- Criar/Sobrepor arquivo;\n  3- Criar/Adicionar no arquivo;\n   4- Sair!\n ->")
	os.system("cls")
#////////////////////////////////////
	if menu == "1":
		feedback = arq_ler()
		print("\n"+feedback+"\n")

		for seq in sequencias:
			print("Cabeçalho: "+seq+"\n Sequência: "+sequencias[seq]+"\n")
#////////////////////////////////////
	elif menu == "2":
		feedback = arq_sobrepor()
		print("\n"+feedback+"\n")
#////////////////////////////////////
	elif menu == "3":
		feedback = arq_add()
		print("\n"+feedback+"\n")
#////////////////////////////////////
	elif menu == "4":
		print("\nsaiu do programa!\n")
		flag_menu = False
#////////////////////////////////////
	else:
		print("\nOpção inválida!\n")
