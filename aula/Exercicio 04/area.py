from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2
    
q = int(input("Digite a área do Quadrado: "))
c = int(input("Digite a área do Circulo: "))
    
formas = [Quadrado(q), Circulo(c)]

for forma in formas:
    print("Área: ", forma.calcular_area())


    