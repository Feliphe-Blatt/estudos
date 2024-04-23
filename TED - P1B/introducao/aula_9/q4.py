def verifica_primo(numero:int) -> bool:

    primo = True

    if (numero <= 1):

        primo = False
    
    for i in range(2, int(numero ** .5) + 1):

        if ((numero % i) == 0):

            primo = False

    return primo

teste = int(input('\nDigite um número inteiro positivo para testar se é primo:\n-> '))

if (verifica_primo(teste)):

    print(f'\nO número {teste} É primo!\n')

else:
    
    print(f'\no número {teste} NÃO É primo!\n')
