from app import app

from flask import render_template

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/servico')
def servico():
    return render_template('servico.html')