#Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. 
#Mostrar un menú de opciones que permita:
#1- Cargar alumnos.
#2- Listar alumnos.
#3- Mostrar alumnos con notas mayores o iguales a 7.
#4- Finalizar programa.
class Alumnos:
    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()
    def cargar(self):
        for x in range(5):
            nom=input("Ingrese su nombre:")
            self.nombres.append(nom)
            no=int(input("Ingrese su nota"))
            self.notas.append(no)

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print(self.nombres[x],self.notas[x])
        print("___________________________")

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7:")
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x],self.notas[x])
        print("___________________________")
Alumnos1 = Alumnos()
Alumnos1.menu()