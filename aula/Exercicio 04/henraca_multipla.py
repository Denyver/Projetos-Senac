class Pai:
    def __init__(self):
        print("Iniciando a calsse A")
        super().__init__()

class Mae:
    def __init__(self):
        print("Iniciando a classe B")
        super().__init__()

class Filho(Mae, Pai):
    def __init__ (self):
        print("Iniciando a classe C")
        super().__init__()

a = Filho()