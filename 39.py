#Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo.
#En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos
#  y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
class Empleado:
    def __init__(self):
        self.nombre=input("Ingrese un nombre")
        self.sueldo=int(input("Ingrese su sueldo"))
    def imprimir(self):
        print("Estimado ser viviente",self.nombre, "su sueldo es: ",self.sueldo)
    def impuestos(self):
        if self.sueldo >3000:
            print("Tienes que pagar impuestos D:")
        else:
            print("No pagas impuestos :D")
Empleado1=Empleado()
Empleado1.imprimir()
Empleado1.impuestos()