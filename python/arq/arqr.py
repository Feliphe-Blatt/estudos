arq = open("bomdia.txt", "r") #abre arquivo somente leitura

lista = arq.readlines() #cria lista com linhas

print(lista)

lidototal = arq.read() #cria string com tudo

print(lidototal)

linha = arq.readline() #lê uma string até "\n"

print(linha)