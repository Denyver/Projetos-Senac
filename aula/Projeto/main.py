class Conta:
    def __init__(self):
        self.__nome = None
        self.__senha = None
        self.__agencia = None
        self.__cadastrado = False

    def cadastro(self):
        if self.__cadastrado:
            print("Já existe uma conta cadastrada!\n")
            return
        
        while True:
            print("Digite seu nome")
            self.__nome = input(": ")
            if isinstance(self.__nome ,str):
                break
            else:
                print("Nome não deve conter número!")

        while True:
            print("Digite sua agência")
            self.__agencia = int(input(": "))
            if isinstance(self.__agencia, int):
                break
            else:
                print("Agência deve ser número!")

        self.__senha = input("Digite sua senha: ")

        self.__cadastrado = True
        print("Cadastro realizado com sucesso!\n")

    def login(self):
        if not self.__cadastrado:
            print("Nenhuma conta cadastrada ainda!\n")
            return

        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        agencia = int(input("Digite sua agência: "))

        if isinstance(agencia, int):
            pass
        else:
            print("Agência inválida!\n")
            return

        if nome == self.__nome and senha == self.__senha and agencia == self.__agencia:
            print("Login realizado com sucesso!\n")
            menu.menuCliente()
        else:
            print("Nome, senha ou agência incorretos!\n")
class Menu:
    def __init__(self):
        self.conta = Conta()
    def iniciar(self):
        while True:
            print("===== MENU =====")
            print("1 - Cadastro")
            print("2 - Login")
            print("3 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.conta.cadastro()
            elif opcao == "2":
                self.conta.login()
            elif opcao == "3":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!\n")

    def menuCliente(self):
        while True:
            print("===== Seja Bem Vindo! =====")
            print("1 - Sacar")
            print("2 - Depositar")
            print("3 - Emprestimo")
            print("4 - Transfêrencia")
            print("5 - Extrato")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                pass
            elif opcao == "2":
                pass
            elif opcao == "3":
                pass
            elif opcao == "4":
                pass
            elif opcao == "5":
                pass
            else:
                print("Opção inválida!\n")
    

menu = Menu()
menu.iniciar()