lista = ['casa', 'carro', 'abacate', 'pipoca']

lista_decrescente = sorted(lista, key=lambda x: len(x), reverse=True)

print(f'\nLista ordenada de forma decrescente:\n\n-> {lista_decrescente}\n')
