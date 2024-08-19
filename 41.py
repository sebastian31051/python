#Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e 
#inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método
#de la clase Operación y llamarlos desde el mismo método __init__
class Operacion:
    def __init__(self):
        self.valor1=int(input("Ingrese un valor:"))
        self.valor2=int(input("Ingrese un valor:"))
        self.sumar()
        self.resta()
        self.multiplicacion()
        self.division()

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es:",suma)

    def resta(self):
        rest=self.valor1-self.valor2
        print("La resta es:",rest)

    def multiplicacion(self):
        mult=self.valor1*self.valor2
        print("La multiplicacion es:",mult)

    def division(self):
        div=self.valor1/self.valor2
        print("La division es:",div)

operacion1 = Operacion()