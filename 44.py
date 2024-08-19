#Plantear un programa que permita jugar a los dados. Las reglas de juego son:
#se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió
import random
class dado:
    def tirar(self):
        self.valor=random.randint(1,6)
    def imprimimr(self):
        print("el resultado del dado es:",self.valor)
    def retornar_dado(self):
        return self.valor
class juego_de_dados:
    def __init__(self):
        self.dado1=dado()
        self.dado2=dado()
        self.dado3=dado()
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimimr()
        self.dado2.tirar()
        self.dado2.imprimimr()
        self.dado3.tirar()
        self.dado3.imprimimr()
        if self.dado1.retornar_dado()==self.dado2.retornar_dado() and self.dado1.retornar_dado()==self.dado3.retornar_dado():
            print("gano")
        else:
            print("perdio")
juego_dados=juego_de_dados()
juego_dados.jugar()