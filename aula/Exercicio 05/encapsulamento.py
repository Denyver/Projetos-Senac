class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo Insuficiente!")

    def consultar_saldo(self):
        return self.__saldo
    
c1 = ContaBancaria("Jhonathan", 1000)
c1.depositar(500)
c1.sacar(100)

print(f"Saldo Atual: {c1.consultar_saldo()}")