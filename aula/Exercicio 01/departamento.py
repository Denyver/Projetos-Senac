class Departamento:
    def __init__(self, idDepartamento, nomeDepartamento, tipoDepartamento):
        self.idDepartamento = idDepartamento
        self.nomeDepartamento = nomeDepartamento
        self.tipoDepartamento = tipoDepartamento

    def apresentacao(self):
        print(
            f"O id do departamento é: {self.idDepartamento}\n"
            f"Nome: {self.nomeDepartamento}\n"
            f"Tipo: {self.tipoDepartamento}"
        )