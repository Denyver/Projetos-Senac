class IMC:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.situacao = "Normal"

    def verificar_situacao(self):
        imc = self.peso / (self.altura * self.altura)

        if imc < 16:
            self.situacao = "Magreza Grau III"
        elif 16 <= imc <= 16.9:
            self.situacao = "Magreza Grau II"
        elif 17 <= imc <= 18.4:
            self.situacao = "Magreza Grau I"
        elif 18.5 <= imc <= 24.9:
            self.situacao = "Eutrofia"
        elif 25 <= imc <= 29.9:
            self.situacao = "Pré-Obesidade"
        elif 30 <= imc <= 34.9:
            self.situacao = "Obesidade Moderada (Grau 1)"
        elif 35 <= imc <= 39.9:
            self.situacao = "Obesidade Severa (Grau 2)"
        else:
            self.situacao = "Obesidade Grave (Grau 3)"

        return imc, self.situacao


pessoa1 = IMC("Denyver", 1.90, 80)

imc, situacao = pessoa1.verificar_situacao()

print(f"Nome: {pessoa1.nome}")
print(f"IMC: {imc:.2f}")
print(f"Situação: {situacao}")
