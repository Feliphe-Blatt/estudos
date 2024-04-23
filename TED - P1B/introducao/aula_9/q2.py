def calcula_fatorial(numero:int) -> int:

    fatorial = 1

    for n in range(1, numero + 1):

        fatorial *= n

    return fatorial

num = 7

print(f'\nO fatorial de {num} é: {calcula_fatorial(num)}\n')
