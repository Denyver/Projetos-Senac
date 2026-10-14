class Disciplina:
    def __init__(self, nome):
        self.nome = nome


class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def adicionarDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listarDisciplinas(self):
        print(f"Professor {self.nome} ministra:")
        for d in self.disciplinas:
            print(f"- {d.nome}")


disc1 = Disciplina("Banco de Dados")
disc2 = Disciplina("POO")

prof = Professor("Bergh")
prof.adicionarDisciplina(disc1)
prof.adicionarDisciplina(disc2)

prof.listarDisciplinas()
