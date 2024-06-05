# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   SETUP
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

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

    try:
        with open("disciplinas.json", mode='r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            lista = dados.get("disciplinas", [])
    except (FileNotFoundError, json.JSONDecodeError):
        lista = []

    return render_template('disciplinas.html', disciplinas=lista)

#   Página de Adição de Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/disciplinas/add')
def disciplinas_add():
    return render_template('disciplinas-add.html')

#   Adiciona Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/disc-add', methods=['POST', ])
def disc_add():
    try:
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

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#   Página de Edição de Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/disciplinas/edit/<int:disc_id>')
def disciplinas_edit(disc_id):
    try:
        # Carrega a disciplina do arquivo JSON
        with open("disciplinas.json", mode='r+', encoding='utf-8') as arquivo:

            dados = json.load(arquivo)
            disciplina = dados["disciplinas"][disc_id]

        return render_template('disciplinas-edit.html', disciplina=disciplina, disc_id=disc_id)

    except (FileNotFoundError, IndexError, json.JSONDecodeError):
        return "Disciplina não encontrada", 404

#   Grava Edição da Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/disc-edit', methods=['POST', ])
def disc_edit():
    try:
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

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#   Deleta Disciplina
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/disciplina-del', methods=['POST', ])
def disc_del():
    try:
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

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   AULA / EVENTO - Página Principal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/eventos')
def eventos():
    try:
        with open("aulas-eventos.json", mode='r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            lista = dados.get("eventos", [])

    except (FileNotFoundError, json.JSONDecodeError):
        lista = []

    return render_template('aulas-eventos.html', eventos=lista)

#   Página de Adição de evento
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/eventos/add')
def eventos_add():
    return render_template('eventos-add.html')

#   Adiciona evento
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/event-add', methods=['POST'])
def event_add():
    try:
        data = request.form["data"]
        descricao = request.form["descricao"]
        tipo = request.form["tipo"]

        # Convertendo a data para formato (DD/MM/AAAA)
        data_formatada = datetime.strptime(
            data, "%Y-%m-%d").strftime("%d/%m/%Y")

        novo_evento = {
            "data": data_formatada,
            "descricao": descricao,
            "tipo": tipo
        }

        with open("aulas-eventos.json", mode='r+', encoding='utf-8') as arquivo:

            dados = json.load(arquivo)
            dados["eventos"].append(novo_evento)

            arquivo.seek(0)
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            arquivo.truncate()

        return redirect(url_for('eventos'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#   Página de Edição de evento
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/eventos/edit/<int:event_id>')
def eventos_edit(event_id):
    try:
        with open("aulas-eventos.json", mode='r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            evento = dados["eventos"][event_id]

            evento['data_normal'] = datetime.strptime(
                evento['data'], "%d/%m/%Y").strftime("%Y-%m-%d")

        return render_template('eventos-edit.html', evento=evento, event_id=event_id)

    except (FileNotFoundError, IndexError, json.JSONDecodeError):
        return "Evento não encontrado", 404

#   Edita evento
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/event-edit', methods=['POST'])
def event_edit():
    try:
        event_id = int(request.form["event_id"])
        data = request.form["data"]
        descricao = request.form["descricao"]
        tipo = request.form["tipo"]

        # Convertendo a data para um formato apropriado (DD/MM/AAAA)
        data_formatada = datetime.strptime(
            data, "%Y-%m-%d").strftime("%d/%m/%Y")

        with open("aulas-eventos.json", mode='r+', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            dados["eventos"][event_id] = {
                "data": data_formatada,
                "descricao": descricao,
                "tipo": tipo
            }
            arquivo.seek(0)
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            arquivo.truncate()

        return redirect(url_for('eventos'))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#   Apaga Evento
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/event-del', methods=['POST'])
def event_del():
    try:
        event_id = int(request.form["event_id"])

        with open("aulas-eventos.json", mode='r+', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            if (0 <= event_id < len(dados["eventos"])):
                del dados["eventos"][event_id]

            arquivo.seek(0)
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            arquivo.truncate()

        return redirect(url_for('eventos'))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Inicia o APP
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':
    app.run(debug=True)
