class Pessoa:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")

class Aluno(Pessoa):
    def __init__(self, nome, matricula, nota01, nota02):
        super().__init__(nome, matricula)
        self.nota01 = nota01
        self.nota02 = nota02

    def calcular_media(self):
        return (self.nota01 + self.nota02) / 2

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Nota 1: {self.nota01}")
        print(f"Nota 2: {self.nota02}")
        print(f"Média: {self.calcular_media():.2f}")

class AlunoGraduacao(Aluno):
    def calcular_media(self):
        return (self.nota01 * 0.4) + (self.nota02 * 0.6)

class AlunoEAD(Aluno):
    def calcular_media(self):
        return (self.nota01 + self.nota02) / 2


p1 = Pessoa("Pedro", 123)
a1 = Aluno("Deyvison", 456, 7, 8)
ag1 = AlunoGraduacao("Denyver", 789, 6, 9)
ae1 = AlunoEAD("Kayo", 321, 10, 8)

lista = [p1, a1, ag1, ae1]

for pessoa in lista:
    print("===================")
    pessoa.exibir_dados()
