dicionario = {"A":1, "B":2, "C":3, "D":4}
d2 = dict(c1='v1',c2='v2')

print("\n",dicionario,"\n\nA:",dicionario["A"],"\n")

get_chave = d2.get('c2')
print(get_chave)
set_chave = d2.update({'chave3':'valor3'})

for chave in dicionario:
	print("\nChave:", chave, "\nValor:", dicionario[chave])

for chave in d2:
	print(f'\nChave: {chave}, Valor: {d2[chave]}\n')

print('chave3' in d2,end='\n\n')  #d2.keys()
print('v2' in d2.values(),end='\n\n')
print(len(d2),end='\n\n')

retorna = d2.items()
print(retorna,end='\n\n')

for k, v in d2.items():
	print(k, v)
print('')

import copy
alunos = {
	'feliphe blatt': {
		'n1':10,
		'n2':20,
		'n3':30
	},'joão da silva': {
		'n1':40,
		'n2':50,
		'n3':60
	},'maria antonieta': {
		'n1':70,
		'n2':80,
		'n3':90
	}
}

backup = copy.deepcopy(alunos)  # Copia e viram dois dicts separados
ref_alunos = alunos  # Referência dicionário original, mudam os dois ao mesmo tempo
ref_alunos_copy = alunos.copy()  # cria dict separado, mas utiliza valores originais como padrão
d1 = dict(alunos)
'''
d1.pop('maria antonieta')
d1.popitem()
d1.update(alunos)
for aluno_k, aluno_v in d1.items():
	print(f'Aluno: {aluno_k};')
	for nota_k, nota_v in aluno_v.items():
		print(f'\t{nota_k}: {nota_v}')
'''
for aluno_k, aluno_v in alunos.items():
	print(f'Aluno: {aluno_k};')
	for nota_k, nota_v in aluno_v.items():
		print(f'\t{nota_k}: {nota_v}')
