print('olá')
print("olá", "amigo"+" "+"tudo bem?")
print("olá", "amigo", "tudo", "bem?",sep="-", end="#\n")
print("texto com 'aspas' aqui")
print('texto com "aspas" aqui')
print('texto com "aspas" aqui'+str(10))
print(20*'A')
print(f'porcentagem concluída: {5.1234:.2f};')  # pode ser variável
imc = 5.1234
print('porcentagem concluída: {i:.2f};'.format(i=imc))
print('porcentagem concluída: {:.2f};'.format(imc))  # ':s' ':d' ':f' ':.2f'
i = 1
print(f'{i:0>10.2f}')  #imprime '10' casas do valor, se for maior preenche com '0' na esquerda
x = "olha só que bacana"
print(f'{x:1<20}')  #coloca '1' na direita
print(f'{x:1^20}')  #coloca '1' em volta
y = 'feliphe blatt'
formatado = '{i:@^20}'.format(i=x)
print(formatado)
format_test = '{0},{1},{2},{3},{4}'.format(imc, i, x, y, formatado)
format_test = '{a},{b},{c},{d},{e}'.format(a=imc, b=i, c=x, d=y, e=formatado)
print(format_test)

print("tipo:",str(type(10))+"\n") #indica o tipo da "variável"
