tarefas = {
    'Tarefa':'Descrição'
}

undo_list = {}

#//////////////////////////////////////////////////////////////////////////////////
def tarefa_add(lista):
    nome = input('\nNome da nova tarefa: ')
    desc = input('\n\tDescrição:\n\t> ')
    lista[nome] = desc

#//////////////////////////////////////////////////////////////////////////////////
def tarefa_undo(lista, un):
    if not lista:
        print('\n  Aviso: Não há mais nenhuma tarefa a Desfazer!')
        return
    else:
        t, d = lista.popitem()
        un[t] = d
        print('\n  Tarefa Desfeita!')

#//////////////////////////////////////////////////////////////////////////////////
def tarefa_redo(lista, un):
    if not un:
        print('\n  Aviso: Não há mais nenhuma tarefa a Refazer!')
        return None
    else:
        t, d = un.popitem()
        lista[t] = d
        print('\n  Tarefa Refeita!')
        
#//////////////////////////////////////////////////////////////////////////////////
def tarefa_listar(lista):
    for t, d in lista.items():
        print(f'\n  Tarefa: {t}\n\tDescrição:\n\t> {d}')

#//////////////////////////////////////////////////////////////////////////////////
print('\n\t'+'#'*20)
while True:

    opcao = input('\n\t1> Adicionar Tarefa;\n\t2> Undo;\n\t3> Redo;\n\t4> Listar Tarefas;\n\t5> Sair!\n\t> ')
    print('\n\t'+'#'*20)

    if opcao == '1':
        tarefa_add(tarefas)

    elif opcao == '2':
        tarefa_undo(tarefas, undo_list)

    elif opcao == '3':
        tarefa_redo(tarefas, undo_list)

    elif opcao == '4':
        tarefa_listar(tarefas)

    elif opcao == '5':
        break
    else:
        print(f'\n\tA opção "{opcao}" é inválida!')
    print('\n\t'+'#'*20)
