class Exame:
    def __init__(self, nome_paciente, valor):
        self.__nome_paciente = nome_paciente
        self.__valor = valor
        self.__status = "Agendado"

    def realizar_exame(self):
        self.__status = "Realizado"

    def cancelar_exame(self):
        self.__status = "Cancelado"

    def get_status(self):
        return self.__status

    def get_valor_base(self):
        return self.__valor

    def calcular_valor(self):
        return self.__valor

class ExameRaioX(Exame):
    def __init__(self, nome_paciente, valor, taxa_equipamento):
        super().__init__(nome_paciente, valor)
        self.__taxa_equipamento = taxa_equipamento

    def calcular_valor(self):
        return self.get_valor_base() + self.__taxa_equipamento

class ExameTomografia(Exame):
    def __init__(self, nome_paciente, valor, taxa_adicional, percentual_tecnico):
        super().__init__(nome_paciente, valor)
        self.__taxa_adicional = taxa_adicional
        self.__percentual_tecnico = percentual_tecnico

    def calcular_valor(self):
        valor_base = self.get_valor_base()
        adicional = valor_base * self.__percentual_tecnico
        return valor_base + self.__taxa_adicional + adicional