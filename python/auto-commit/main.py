import subprocess

tipo = "Doc"

descricao = "Documentação do commit convencional 1.0"

def conventional_commit(tipo, desc):

    # Formata o texto do commit
    mensagem = f"{tipo}: {desc}"

    # Adiciona arquivos ao Stage
    subprocess.run(["git", "add", "."])

    # Realiza commit
    subprocess.run(["git", "commit", "-m", mensagem])

    # Obtém o histórico de commits e salva em log.txt
    with open("./log.txt", "w") as log_file:
        subprocess.run(["git", "log", "--oneline"], stdout=log_file)


conventional_commit(tipo, descricao)