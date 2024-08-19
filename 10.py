#Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas.
#Luego ordenar las notas de mayor a menor.
#Imprimir las notas y los nombres de los alumnos.
estudiantes=[]
notas=[]
for x in range(5):
    est = input("ingrese su nombre")
    estudiantes.append(est)
    n = float(input("Ingrese su nota"))
    notas.append(n)
   
for k in range(4):
    for x in range(4-k):
        if notas[x]<notas[x+1]:
            aux1 = notas[x]
            notas[x] = notas[x+1]
            notas[x+1] = aux1
            aux2 = estudiantes[x]
            estudiantes[x] = estudiantes[x+1]
            estudiantes[x+1] = aux2

print("Las notas de los estudiantes son:")
for x in range(5):
    print(notas[x],estudiantes[x])