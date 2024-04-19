import subprocess

def conventional_commit(tipo, desc):

    # Formata o texto do commit
    message = f"{tipo}: {desc}"

    # Adiciona arquivos ao Stage
    subprocess.run(["git", "add", "."])

    # Realiza commit
    subprocess.run(["git", "commit", "-m", message])

    # Obtém o histórico de commits e salva em log.txt
    with open("./log.txt", "w") as log_file:
        subprocess.run(["git", "log", "--oneline"], stdout=log_file)

tipo = "Ci"

descricao = "Update da automação de commit convencional 1.0"

conventional_commit(tipo, descricao)