from app.models import Aluno


class controller_aluno():

    AlunoList = []

    @classmethod
    def saveAluno(cls, aluno: Aluno):

        cls.AlunoList.append(aluno)

    @classmethod
    def printDate(cls):

        for aluno in cls.AlunoList:
            print(aluno.getinfo())

    @classmethod
    def getAlunoList(cls):

        data = []

        for aluno in cls.AlunoList.copy():
            data.append(aluno.getinfo())

        return data