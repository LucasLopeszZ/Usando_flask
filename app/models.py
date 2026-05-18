class Aluno():

    def __init__(self, nome:str, email:str, idade:str,
                 sexo:str, matricula:str, cpf:str):

        self.nome = nome
        self.email = email
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula
        self.cpf = cpf

    def getinfo(self):

        return {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade,
            "sexo": self.sexo,
            "matricula": self.matricula,
            "cpf": self.cpf
        }