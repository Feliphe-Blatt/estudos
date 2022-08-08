def func(*args, **kwargs):  #args é uma tupla (imutável) 
    print(args)  #kwargs para valores padrão (nome= None... etc)
    return args, kwargs

v1,*v2 = func(1,2,3,nome= 'joão')
lista = list(func(3,2,1,nome='maria'))

print(v1, v2, sep='_',end='.\n')
print(*lista,sep=' ')
s1, s2 = lista
print(s1)
print(s2)
