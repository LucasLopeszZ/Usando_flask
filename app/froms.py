from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange
from app.controllerAluno import controller_aluno
from app.models import Aluno



class StudenteForm(FlaskForm):
    nome = StringField("Nome", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    idade = IntegerField("Idade", validators = [DataRequired(),NumberRange(min= 0, max = 100)])
    sexo = StringField("Sexo", validators = [DataRequired()])
    matricula = StringField("Matricula", validators =  [DataRequired()])
    cpf = StringField("Cpf", validators = [DataRequired()])
    btnSubmit = SubmitField("Cadastrar")

    def SalvarAluno(self):
        aluno = Aluno ( nome = self.nome.data,
                      email = self.email.data,
                      idade = self.idade.data,
                      sexo = self.sexo.data,
                      matricula = self.matricula.data,
                      cpf = self.cpf.data)
        
        controller_aluno.saveAluno(aluno)

        