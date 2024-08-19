#Definir por asignación una lista de enteros en el bloque principal del programa.
#Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos,
#la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.
def sumalizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
def mayor(lista):
    mayor=lista[0]
    for x in range(1, len(lista)):
        if lista[x]>mayor:
            mayor = lista[x]
    return mayor
        
def menor(lista):
    menor=lista[0]
    for x in range(1, len(lista)):
        if lista[x]<menor:
            menor = lista[x]
    return menor
lista_valores=[15,18,19,20,30]
print("La lista completa es:", lista_valores)
print("La suma es:",sumalizar(lista_valores))
print("El valor mayor es:",mayor(lista_valores))
print("El valor menor es:",menor(lista_valores))