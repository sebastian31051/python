#Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en
#una tupla que luego debe retornar. La segunda función a implementar debe recibir una tupla 
#con la fecha y mostrarla por pantalla.
def cargar_fecha():
    dia=int(input("ingrese el dia"))
    mes=int(input("ingrese el mes"))
    año=int(input("ingrese el año"))
    return(dia,mes,año)
def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2], sep="/")

fecha=cargar_fecha()
imprimir_fecha(fecha)