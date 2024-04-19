import subprocess

def conventional_commit(tipo, desc):

    # Formata o texto do commit
    message = f"{tipo}: {desc}"

    # Adiciona arquivos ao Stage
    subprocess.run(["git", "add", "."])

    # Realiza commit
    subprocess.run(["git", "commit", "-m", message])

    # Salva histórico em log.txt
    subprocess.run(["git", "log", "--oneline", ">>", "./log.txt"])

tipo = "Ci"

descricao = "Update da automação de commit convencional 1.0"

conventional_commit(tipo, descricao)