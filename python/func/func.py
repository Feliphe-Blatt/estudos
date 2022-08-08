'''
/////////////////////////////////////////// q1
def saudacao(sauda, nome):
    print(f'{sauda}, {nome}!')
    return (f'{sauda}, {nome}')

saudacao('bom dia', 'feliphe blatt')

print(saudacao('boa tarde', 'joao'))
/////////////////////////////////////////// q2
def soma(a, b, c):
    print(a+b+c)
    return a+b+c

print(soma(1,2,3))
/////////////////////////////////////////// q3
def ajuste_percentual(x,y):
    return x + ((x/100)*y)

print(ajuste_percentual(100,-50))
/////////////////////////////////////////// q4
from random import randint
def fb(x):
    if x%3==0 and x%5==0:
        return f'FizzBuzz {x}'
    if x%3==0:
        return f'Fizz {x}'
    if x%5==0:
        return f'Buzz {x}'
    return x
print(fb(randint(0,100)))
/////////////////////////////////////////// desafio
def principal(func,*args,**kwargs):
    return func(*args,**kwargs)

def endereco(rua):
    return f'{rua}'

def saudacao(sauda,nome):
    return f'{sauda}, {nome}'

sauda = principal(saudacao,sauda="bem vindo",nome="fulano da silva")
print(sauda)
residencia = principal(endereco, 'manoel arruda')
print(residencia)
'''
a = lambda x, y: x * y
print(a(1,2))
