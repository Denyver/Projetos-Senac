class Camera:
    def tirar_foto(self):
        print("Foto Capturada!")

class Telefone:
    def fazer_ligacao(self):
        print("Ligando para o contato...")

class Smartphone(Camera, Telefone):
    pass

c = Smartphone()
c.tirar_foto()
c.fazer_ligacao()
print(Smartphone.__mro__)