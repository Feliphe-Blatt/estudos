'''
palavra = 'banana'
palavra = palavra.replace('a','4')
flag_contem = False

while(not flag_contem):
    tentativa = input('Digite uma letra que possa conter na palavra: ')

    if (tentativa in palavra) and len(tentativa)==1:
        print(f'A letra "{tentativa}" existe na palavra "{palavra}"!')
        flag_contem = True

    elif (tentativa in palavra) and len(tentativa)>1:
        print(f'A letra "{tentativa}" não é uma letra só, mas existe na palavra "{palavra}"')
        flag_contem = True
        
    else:
        print(f'A letra "{tentativa}" não existe na palavra "{palavra}"')
'''

# Os índices de uma string podem ser positivos para correr normalmente
# Ou índices negativos para correr de trás pra frente
teste = "fELIPHE bLATT"
teste2 = "fELIPHE bLATT,programador de c,c++,python 3,javascript,feliphe blatt,html5,css3"
print(teste.lower())
print(teste.upper())
print(teste.title())  #imprime somente com as primeiras letras maiúsculas
print(teste[:-1])  # imprime string até certo índice (o fim não é incluído)
print(teste[2:7:2].lower())  # ':2' no final pula de 2 em 2

split1 = teste2.lower().split(',')  # cria lista com strings separadas pelo caractere escolhido

split2 = teste2.lower().split(',')
mais_recorrente = 0
palavra = ''
for word in split2:
    quantidade = split2.count(word)

    if quantidade > mais_recorrente:
        mais_recorrente = quantidade
        palavra = word

print(f'A palavra mais recorrente do "split2" é "{palavra}"({mais_recorrente}x)!')

for word in split2:
    print(f'"{word}"',end='-')
