#Desarrollar un programa que permita ingresar el lado de un cuadrado.
#Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.
def perimetro(lado):
    per = lado*4
    print("El perimetro es: ",per)
def superficie(lado):
    sup = lado*lado
    print("La superficie es:",sup)

def cargar():
    la=int(input("Ingrese tamaño del lado del cuadrado"))
    elegir=int(input("Digite '1' si desea hallar el perimetro, o digite '2' si desea hallar la superficie"))
    if elegir == 1:
        perimetro(la)
    else:
        if elegir == 2:
            superficie(la)
        else:
            print("fuera de rango")
cargar()