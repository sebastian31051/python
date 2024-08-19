#Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
#Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera 
#mostrar el nombre del país con mayor cantidad de habitantes.
def paises_poblacion():
    paises=[]
    for x in range(5):
        nom=input("Ingrese el nombre del pais")
        can=int(input("Ingrese la cantidad de habitantes"))
        paises.append((nom,can))
    return paises
def imprimir(paises):
    print("Paises y su poblacion")
    for x in range (len(paises)):
        print(paises[x][0],paises[x][1])

def mas_poblacion(paises):
    pos = 0
    for x in range(1, len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Pais con mayor cantidad de habitantes es:", paises[pos][0])

paises=paises_poblacion()
imprimir(paises)
mas_poblacion(paises)
