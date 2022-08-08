
def buscaPalavra(nome):
    import random

    palavras = []
    palavra_esc = ''

    arq = open(nome, "r")
    while True:
        temp_r = arq.readline()
        temp = temp_r.replace('\n','')
        if temp == '-':
            break
        palavras.append(temp)
    arq.close()

    palavra_esc = palavras[random.randint(0,len(palavras)-1)]

    return palavra_esc

#/////////////////////////////////////////////////////////////////////////////////////////

def forca(arquivo):
    import os
    # nome = input('\n\tNome do arq: ')
    # palavra_escolhida = buscaPalavra(nome)
    palavra = buscaPalavra(arquivo)
    digitadas = []
    os.system('cls')
    print('\n '+'#'*30)

    while True:
        acertos = []
        tentativa = input("\n Tentativa de acertar letra:  ")

        if (len(tentativa)>1) or tentativa.isdigit() or not tentativa.isalpha():
            print(f'\n\t> "{tentativa}" Não é letra válida')
            continue
        else:
            digitadas.append(tentativa)
            
        print('\n\t',end='')
        for letra in palavra:
            if letra in digitadas:
                print(letra,end='')
                acertos.append(letra)
            else:
                print('*', end='')

        print(f' Tem "{len(palavra)}" letras.\n')

        print('\n '+'#'*30)

        if len(acertos) == len(palavra):
            print(f'\nVocê acertou a palavra "{palavra}" completamente, parabéns!\n\n')
            print('\n '+'#'*30)
            break

#/////////////////////////////////////////////////////////////////////////////////////////

forca("palavras.txt")
