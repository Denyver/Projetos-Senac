class ContaBancaria:
    # Método Construtor
    def __init__ (self, titular, saldo_inicial, data_transferencia):
        # Atributos
        self.titular = titular
        self.saldo = saldo_inicial
        self.data_transferencia = data_transferencia

    # Método
    def depositar(self, valor):
        self.saldo += valor
        print(f"O valor depositador: {valor:.2f} realizado com sucesso")

    # Método        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"O valor sacado: {valor:.2f} realizado com sucesso")
        else:
            print(f"Saldo insuficiente")

    # Método
    def consultarSaldo(self):
        print(f"Saldo de {self.titular} atual é: R$ {self.saldo:.2f}")
    

conta1 = ContaBancaria("Denyver", 4900, "27/03/2002")
conta1.depositar(1000)
conta1.sacar(500)
conta1.consultarSaldo()