from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def ola_mundo():

    # return '<h1>Olá Mundo!</h1>'

    return render_template('index.html')

app.run(debug=True, port=8080)
