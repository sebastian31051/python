#Confeccionar una función que le enviemos como parámetro un string y nos retorne
#la cantidad de caracteres que tiene.
#En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces.
#Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.
def largo(cadena):
    return len(cadena)

nombre1=input("Ingrese un nombre")
nombre2=input("Ingrese otro nombre")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres ",nombre1,nombre2,"tienen el mismo tamaño de caracteres")
else:
    if la1>la2:
            print("El nombre",nombre1,"Es mas largo")
    else:
         print("El nombre",nombre2,"Es mas largo")