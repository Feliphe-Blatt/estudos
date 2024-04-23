palavras = ["python", "programação", "desenvolvimento", "computador", "linguagem", "tecnologia", "dados", "inteligência", "artificial", "aplicativo"]

# Testa se as palavras começam com certa letra e retorna uma lista somente com as palavras que comecem com a letra específica
def encontra_palavras(lista: list, letra: str) -> list:
    
    nova_lista = []

    for palavra in lista:

        if (palavra[0] == letra.lower()):
            nova_lista.append(palavra)

    return nova_lista

# Perguntando ao usuário qual letra deseja pesquisar
teste = input('\nDigite uma letra para achar as palavras que começam com ela:\n-> ').lower()

palavras_selecionadas = encontra_palavras(palavras, teste)

print(f'\nLista de palavras que começam com "{teste}":\n-> {palavras_selecionadas}\n')
