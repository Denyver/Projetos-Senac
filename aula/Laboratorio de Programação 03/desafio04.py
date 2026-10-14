class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):

    def calcular_bonus(self):
        return self.salario * 0.20
        
class Estagiario(Funcionario):
    
    def calcular_bonus(self):
        return self.salario * 0.05
    
f = Funcionario(input("Digite o nome do funcionario: "), float(input("Digite o salário: ")))
g = Gerente(input("Digite o nome do gerente: "), float(input("Digite o salário: ")))
e = Estagiario(input("Digite o nome do estagiario: "), float(input("Digite o salário: ")))

lista = [f, g, e]

# Aplicando Polimorfismo
for funcionario in lista:
    print(f"{funcionario.nome} - Tem seu bonus de: {funcionario.calcular_bonus()}")
