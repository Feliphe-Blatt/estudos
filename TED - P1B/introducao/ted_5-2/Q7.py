usuarios = []

flag = True

while flag:

    print("\nNovo cadastro:\n")

    nome = input("Digite o nome:\n->")
    idade = int(input("Digite a idade:\n->"))
    email = input("Digite o e-mail:\n->")

    usuarios.append({nome, idade, email})

    teste = input("\nQuer sair? (s-n)\n->")
    if teste == 's':
        flag = False
    elif teste == 'n':
        print('\nContinuando...\n')

with open('cadastro.txt', 'a') as arquivo:
    for pessoa in usuarios:
        arquivo.write(f'{pessoa}\n')
