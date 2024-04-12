vetor = []

for i in range(5):

    temp = input(f'\nDigite o {i+1}° clube de futebol a adicionar:\n->')
    vetor.append(temp.lower())

compara = input(
    '\nAgora digite um clube para testar se está na lista anterior ou não:\n->')

flag = False

for i in vetor:
    if (i == compara.lower()):
        flag = True

if (flag):
    print("\nACHEI\n")
else:
    print("\nNÃO ACHEI\n")
