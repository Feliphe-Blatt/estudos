# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   SETUP
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import json
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Início / Menu
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/')
def intro():
    return render_template('index.html')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Disciplinas - Página Principal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/disciplinas')
def disciplinas():

    disciplinas = []

    with open("disciplinas.json", mode='r', encoding='utf-8') as arquivo:

        # Pegando a lista de disciplinas
        dados = json.load(arquivo)
        lista = dados["disciplinas"]

        # Passando os valores encontrados para Exibir
        for i in lista:
            disciplinas.append(i)

    return render_template('disciplinas.html', disc=disciplinas)


#   Página de Adição de Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/disciplina-add')
def disciplina_criar():

    return render_template('disciplina-add.html')


#   Adiciona Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/criar-disciplina', methods=['POST', ])
def criar_disciplina():

    # Recolhe Informações
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    carga = request.form["carga"]

    nova = {
        "nome": nome,
        "descricao": descricao,
        "carga": carga
    }

    # Atualiza Arquivo JSON
    with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:

        dados = json.load(arquivo)
        dados["disciplinas"].append(nova)

        arquivo.seek(0)
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        arquivo.truncate()

    return redirect(url_for('disciplinas'))



#   Página de Edição de Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/disciplina-editar/<int:disc_id>')
def disciplina_editar(disc_id):

    # Carrega a disciplina do arquivo JSON
    with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:

        dados = json.load(arquivo)
        disciplina = dados["disciplinas"][disc_id]

    return render_template('disciplina-edit.html', disciplina=disciplina, disc_id=disc_id)


#   Grava Edição da Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/editar-disciplina', methods=['POST', ])
def editar_disciplina():

    # Recolhe Informações
    disc_id = int(request.form["disc_id"])
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    carga = request.form["carga"]

    # Atualiza Arquivo JSON
    with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

        dados["disciplinas"][disc_id] = {
            "nome": nome,
            "descricao": descricao,
            "carga": carga
        }

        arquivo.seek(0)
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        arquivo.truncate()

    return redirect(url_for('disciplinas'))

#   Deleta Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/disciplina-del', methods=['POST', ])
def apagar_disciplina():

    # Recolhe Informações
    disc_id = int(request.form["disc_id"])

    # Deleta e Atualiza Arquivo JSON
    with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

        if (0 <= disc_id < len(dados["disciplinas"])):
            del dados["disciplinas"][disc_id]

        arquivo.seek(0)
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        arquivo.truncate()

    return redirect(url_for('disciplinas'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   AULA / EVENTO - Página Principal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/aulas-eventos')
def aula_evento():

    return render_template('aulas-eventos.html')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Inicia o APP
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    app.run(debug=True)
