sueldos = []
for x in range(5):
    sueldo = int(input("Ingrese el valor del sueldo"))
    sueldos.append(sueldo)
print("Sueldo sin ordenar")
print(sueldos)
for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
print("Sueldo ordenado ultimo dato")
print(sueldos)