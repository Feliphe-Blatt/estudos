while True:
    cpf = input("digite seu cpf (somente números): ")
    temp = cpf[:-2]  #retira 2 últimos dígitos
    soma = 0
    count = 10
    for i in range(19):
        if i > 8:  #reinicia contagem index
            i -= 9  #quantidade de números do cpf sem os dois últimos dígitos
        soma += int(temp[i]) * count
        count-=1  #soma tudo e decrementa 1 do count

        if count < 2:
            count = 11
            d = 11 - (soma%11)
            if d > 9:
                d=0
            soma = 0
            temp+=str(d)
    
    sequencia = temp == str(temp[0]) * len(cpf)
    if (temp == cpf) and (not sequencia):
        print(f'O cpf "{temp}" é válido!')
        break
    else:
        print(f'o cpf "{temp}" não é válido!')
