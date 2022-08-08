frase = 'o rato roeu a roupa do rei de roma'
contador = 0
tam = len(frase)
temp = ''

while contador < tam:
    letra = frase[contador]
    contador += 1
    if letra == 'r':
        temp += 'L'
    else:
        temp += letra
print(temp)
