class Funcionario:
    def __init__ (self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def apresentacao(self):
        print(
            f"O nome do funcionario é: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Sexo: {self.sexo}"
        )