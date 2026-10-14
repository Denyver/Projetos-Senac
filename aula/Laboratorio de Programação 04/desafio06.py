class AmbienteRadiologico:
    def __init__(self, nome_ambiente, nivel_radiacao, limite_maximo):
        self._nome_ambiente = nome_ambiente
        self._nivel_radiacao = nivel_radiacao
        self._limite_maximo = limite_maximo

    def adicionar_radiacao(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            self._nivel_radiacao += valor
        else:
            print("Valor Inválido")

    def verificar_seguranca(self):
        if self._nivel_radiacao > self._limite_maximo:
            print(f"ALERTA: {self._nome_ambiente} está acima do limite! ({self._nivel_radiacao}/{self._limite_maximo})")
        else:
            print(f"Seguro: {self._nome_ambiente} está dentro do limite.")
    
    def get_nivel_radiacao(self):
        return self._nivel_radiacao

class Tomografia(AmbienteRadiologico):    
    def adicionar_radiacao(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            # Tomografia adiciona o valor base + 30% de taxa técnica
            self._nivel_radiacao += valor * 1.3
        else:
            print("Valor Inválido")

class Ressonancia(AmbienteRadiologico):
    def adicionar_radiacao(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            self._nivel_radiacao += valor * 1.8
        else:
            print("Valor Inválido")

class RaioX(AmbienteRadiologico):
    def adicionar_radiacao(self, valor):
        if isinstance(valor, (float, int)) and valor > 0:
            self._nivel_radiacao += valor * 1.5
        else:
            print("Valor Inválido")

sala_raiox = RaioX("Sala A1", 0, 100)
sala_raiox.adicionar_radiacao(50)
sala_raiox.verificar_seguranca() # 50 * 1.5 = 75 (Dentro do limite)

sala_raiox.adicionar_radiacao(30)
sala_raiox.verificar_seguranca() # 75 + (30 * 1.5) = 120 (Acima do limite)