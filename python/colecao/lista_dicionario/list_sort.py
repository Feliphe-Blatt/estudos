'''
a = float(input("Digite um valor para a:"))
b = float(input("Digite um valor para b:"))
c = float(input("Digite um valor para c:"))

lista = [a,b,c]
lista = sorted(lista)

print(lista)
'''
lista = [
    ['9','b'],
    ['3','c'],
    ['4','a'],
    ['1','d'],
    ['0','f'],
    ['7','g'],
    ['8','h'],
    ['18','j'],
    ['58','j'],
    ['11','u'],
    ['6','i']
]
print(*sorted(lista,key=lambda i:i[1],reverse=False))
lista.sort(key=lambda i:(int(i[0])),reverse=True)
print(*lista)
