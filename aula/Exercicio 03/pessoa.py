class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def __del__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Denyver", 23)

print(p1.nome)
print(p1.idade)

class Exemplo:
    def __init__ (self):
        print("Objeto Criado")

    def __del__ (self):
        print("Objeto Destruído")

obj = Exemplo()