#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y 
#añadirlos a la lista. Imprimir la lista generada.
lista = []
for x in range(5):
    entero = int(input("Ingrese un valor entero"))
    lista.append(entero)
print(lista)