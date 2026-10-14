class Impressora:
    def imprimir(self):
        print("Imprimindo...")

class Relatorio:
    def imprimir(self):
        while True:
            print("Gerando um relario, em quanto formato deseja?")
            print("1 - PDF")
            print("2 - JPG")
            print("3 - JPEG")
            print("4 - PNG")
            escolha = int(input(""))

            if escolha == 1:
                print("Imprimindo em formato PDF...")
            elif escolha == 2:
                print("Imprimindo em formato JPG...")
            elif escolha ==  3:
                print("Imprimindo em formato JPEG...")
            elif escolha == 4:
                print("Imprimindo em formato PNG...")
            else:
                print("Formato Inválido")
                break

def executar_impressao(objeto):
        objeto.imprimir()

executar_impressao(Impressora())
executar_impressao(Relatorio())