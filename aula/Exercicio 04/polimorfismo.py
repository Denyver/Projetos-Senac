class Animal:
    def emitir_som(self):
        print("O Animal faz um som.")

class Cachorro:
    def emitir_som(self):
        print("O cachorro faz: Au au!")

class Gato:
    def emitir_som(self):
        print("O gato faz: Miau!")

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitir_som()