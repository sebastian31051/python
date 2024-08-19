#Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades 
#la carga por teclado y su impresión.
#En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
#Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo
#y muestre si debe pagar impuestos (sueldo superior a 3000)
#También en el bloque principal del programa crear un objeto de la clase Empleado.
class persona:
    def __init__(self):
        self.nombre=input("Ingrese un nombre")
        self.edad=int(input("Ingrese la edad"))
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
class empleado(persona):
    def __init__(self):
        super().__init__()
        self.sueldo=int(input("Ingrese su sueldo"))
    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Tienes que pagar impuestos")
        else:
            print("No tienes que pagar impuestos")

persona1=persona()
persona1.imprimir()
print("______________________")
empleado1=empleado()
empleado1.imprimir()
empleado1.paga_impuestos()