lista1 = [0,1,2,3,4,5,6,7,8,9]
lista2 = ["joão","maria","fulano","cicrano","marcos","polo","feliphe","cristiane","jair","elias"]
lista3 = [9,8,7,6,5,4,3,2,1,0]
lista4 = lista2 + lista3
lista5 = list(range(0, 100, 8))
teste = "fELIPHE bLATT, programador de c, c++, python 3, javascript, html5 e css3."
'''
print("\n",lista2[2:7],sep="",end="\n\n")  # do índice [2] ao [6]
print(lista2[::-1], "\n")  # sentido contrário

lista1.extend(lista2)
print(lista1, end="\n\n")

lista2.append('mama mia')
print(lista2,"\n")

lista1.insert(0, "bacana")
print(lista1)

lista3.pop()
print(lista3)

x = "garibaldo da silva"
print("nome:",x)
x = input("digite um novo nome:")
completo = x.split(" ")
print(*completo,sep='_')
'''
del(lista2[2:4])
print(lista2)

print(max(lista1))
print(min(lista5))

for nome in lista2:
    if nome.lower().startswith('j'):
        print(f'o nome "{nome}" começa com "j"')

split1 = teste.lower().split(' ')
print()

