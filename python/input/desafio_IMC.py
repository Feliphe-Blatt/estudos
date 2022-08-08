nome = str(input('Digite seu nome: '))
idade = int(input('Sua idade: '))
altura = float(input('Altura em "M": '))
peso = float(input('Peso: '))

imc = peso/(altura**2)
nascimento = 2021 - idade

print(f'\nOlá "{nome}"\n Seu IMC = "{imc:.2f}"\n\n Nascido em {nascimento}\n')
