#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
#Definir los métodos para inicializar sus atributos,
#imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def imprimir(self):
        print("El alumnno",self.nombre,"tiene nota de",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")

Alumno1 = Alumno()
Alumno1.inicializar("Sebastian",4)
Alumno1.imprimir()
Alumno1.mostrar_estado()