from app import app
from app.froms import StudenteForm
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

@app.route('/listagem')
def listagem():
    return render_template('listagem.html')

@app.route('/cadastro',methods = ['GET','POST'])
def cadastro():
    form = StudenteForm()
    if form.validate_on_submit():
        form.SalvarAluno()
        
    return render_template('cadastro.html', form = form)
