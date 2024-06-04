#   SETUP
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import json
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


#   Início
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/')
def intro():
    return render_template('index.html')


#   DISCIPLINA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/disciplina')
def disciplina():

    disciplinas = []

    with open("disciplinas.json", mode='r', encoding='utf-8') as arquivo:

        # Pegando a lista de disciplinas
        dados = json.load(arquivo)
        lista = dados["disciplinas"]

        # Passando os valores encontrados
        for i in lista:
            disciplinas.append(i)

    return render_template('disciplina.html', disc=disciplinas)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/disciplina-criar')
def disciplina_criar():

    return render_template('disciplina-criar.html')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/criar', methods=['POST', ])
def criar():

    nome = request.form["nome"]
    descricao = request.form["descricao"]
    carga = request.form["carga"]

    nova = {
        "nome": nome,
        "descricao": descricao,
        "carga": carga
    }

    with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:

        dados = json.load(arquivo)
        dados["disciplinas"].append(nova)

        arquivo.seek(0)
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        arquivo.truncate()

    return redirect(url_for('disciplina'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/apagar', methods=['POST', ])
def apagar():

    disc_id = int(request.form["disc_id"])

    with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
        if(0 <= disc_id < len(dados["disciplinas"])):
            del dados["disciplinas"][disc_id]

        arquivo.seek(0)
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        arquivo.truncate()

    return redirect(url_for('disciplina'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   AULA / EVENTO
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/aulas-eventos')
def aula_evento():

    return render_template('aulas-eventos.html')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    app.run(debug=True)
