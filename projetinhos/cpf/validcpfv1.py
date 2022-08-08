cpf = "01827632429"
#cpf = "16899535009"
temp = cpf[:-2]

soma = 0
count_desc = 10
for i in range(len(temp)):
    soma += int(temp[i]) * count_desc
    count_desc -= 1
print(f'soma = {soma}')

d1 = 11 - (soma%11)
if d1 > 9:
    d1 = 0
print(f'd1 = {d1}')
temp += str(d1)

soma = 0
count_desc = 11
for i in range(len(temp)):
    soma += int(temp[i]) * count_desc
    count_desc -= 1
print(f'soma = {soma}')

d2 = 11 - (soma%11)
if d2 > 9:
    d2 = 0
print(f'd2 = {d2}')
temp += str(d2)

sequencia = temp == str(temp[0])*len(cpf)

if temp == cpf and not sequencia:
    print(f'cpf "{temp}" é válido!')
else:
    print(f'cpf "{temp}" não é válido!')
