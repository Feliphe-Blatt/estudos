total = int(input('\nquantidade total de aulas:'))
concluidas = int(input("\naulas assistidas:"))

porcentagem = float((concluidas*100)/total)

print(f'\nporcentagem concluída: {porcentagem:.2f}%\n')
meta = float(input('qual sua porcentagem desejada? '))
faltam = float(((meta*total)/100) - concluidas)
print(f"\nfaltam {faltam:.2f} aulas\n")
input('\n Pressione ENTER para sair:')
