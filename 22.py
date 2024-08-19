#Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.
def enteros():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese un valor entero"))
        lista.append(valor)
    return lista
def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")

lista=enteros()
imprimir(lista)