class Cliente:
    def __init__ (self, nome, endereco, bairro, cidade, uf):
        self.nome = nome
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf

class Pessoa_Fisica:
    def __init__ (self, nome, endereco, bairro, cidade, uf, cpf):
        self.nome = nome
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cpf = cpf

class Pessoa_Juridica:
    def __init__ (self, nome, endereco, bairro, cidade, uf, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cnpj = cnpj


cliente = Cliente(
    nome="Denyver Francisco da Silva",
    endereco="Rua A, 123",
    bairro="Centro",
    cidade="Paulista",
    uf="PE"
)

print("Nome:", cliente.nome)
print("Endereço:", cliente.endereco)
print("Bairro:", cliente.bairro)
print("Cidade:", cliente.cidade)
print("UF:", cliente.uf)
