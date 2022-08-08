num = input('\n\nNúmero inteiro pra testar se é par/ímpar: ')

try:
    num = int(num)
    if num%2:
        print(f'\n\nO número "{num}" é ímpar!\n\n')
    else:
        print(f'\n\nO número "{num}" é par!\n\n')
except:
    print('\n\nNão é um número inteiro válido!\n\n')