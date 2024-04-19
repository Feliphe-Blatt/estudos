# COnventional commits

## Como utilizar
  - Edite as variáveis "tipo" e "descricao":
    > Escreva o tipo do commit e descrição respectivamente

  - Edite os arquivos a adicionar ao stage e que vão entrar no commit:
    > Em subprocess.run(["git", "add", "."]) deve-se trocar o argumento "." por "nome completo do arquivo"

  - Em seguida poderá rodar o script
    >  Irá gerar um arquivo "log.txt" com o histórico de commits do repositório, porém ele será gerado APÓS o commit
    >  portanto é esperado que "log.txt" esteja no estado "modified" e não esteja incluso no commit
