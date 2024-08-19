#Se debe crear y cargar una lista donde almacenar 5 sueldos.
#Desplazar el valor mayor de la lista a la última posición.
sueldos = []
for x in range(5):
    sueldo = int(input("Ingrese el valor del sueldo"))
    sueldos.append(sueldo)
print("Sueldo sin ordenar")
print(sueldos)
for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux
print("Sueldo ordenado ultimo dato")
print(sueldos)
