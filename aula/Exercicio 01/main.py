from departamento import Departamento
from funcionario import Funcionario

class Main:
    def __init__ (self):
        funcionario = Funcionario(
            "Deivison",
            50,
            "Masculino")

        departamento = Departamento(
            "teste",
            30,
            "Feminino")
        
        funcionario.apresentacao()
        departamento.apresentacao()

main = Main()