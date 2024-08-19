#Confeccionar una función que reciba una palabra y verifique si es capicúa
#(es decir que se lee igual de izquierda a derecha que de derecha a izquierda)
def capicua(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice= indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es apicua")
    else:
        print("no es apicua")


capicua("neuquen")
capicua("casa")