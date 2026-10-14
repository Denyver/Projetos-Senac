class ContaBancaria:
    def __init__ (self, banco, agencia, cod_agencia, valor):
        self.banco = banco
        self.agencia = agencia
        self.cod_agencia = cod_agencia
        self.valor = valor

    def mostrar_dados(self):
        print("Banco: ", self.banco)
        print("Agencia: ", self.agencia)
        print("Código da Agência: ", self.cod_agencia)
        print("Valor: ", self.valor)          


class ContaCorrente(ContaBancaria):
    def depositarConta(self, valor_depositado):
        self.valor += valor_depositado
        print("Valor depositado com sucesso! Novo Saldo: ", self.valor)
    
    def sacarConta(self, valor_saque):
        if valor_saque <= self.valor:
            self.valor -= valor_saque
            print("Valor sacado com sucesso! Novo Saldo: ", self.valor)
        else:
            print("Saldo Insuficiente!")


class ContaPoupanca(ContaBancaria):
    def depositarConta(self, valor_depositado):
        self.valor += valor_depositado
        print("Valor depositado com sucesso! Novo Saldo: ", self.valor)
    
    def sacarConta(self, valor_saque):
        if valor_saque <= self.valor:
            self.valor -= valor_saque
            print("Valor sacado com sucesso! Novo Saldo: ", self.valor)
        else:
            print("Saldo Insuficiente!")

class InternetBanking(ContaCorrente, ContaPoupanca):
    def ConsultarConta(self):
        print ("Essa classe irá consultar os valores das contas correntes e poupança")

banco1 = input("Digite o nome do banco: ")
agencia1 = input("Digite o número da agência: ")
cod_agencia1 = input("Digite o código da agência: ")
valor1 = float(input("Digite o saldo inicial: "))

conta1 = ContaCorrente(banco1, agencia1, cod_agencia1, valor1)

while True:
    print("\n===== MENU =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar saldo")
    print("4 - Sair")
    print("================\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_depositado = float(input("Digite o valor que deseja depositar: "))
        conta1.depositarConta(valor_depositado)

    elif opcao == "2":
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        conta1.sacarConta(valor_saque)

    elif opcao == "3":
        conta1.mostrar_dados()

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
