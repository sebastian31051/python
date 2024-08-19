#Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
#Implementar las funciones:
#1) Carga de empleados.
#2) Impresión de los empleados y sus sueldos.
#3) Nombre del empleado con sueldo mayor.
#4) Cantidad de empleados con sueldo menor a 1000.
def cargar_empleados():
    empleados=[]
    for x in range(5):
        nombre=input("Ingrese el nombre del empleado")
        sueldo=int(input("Ingrese el sueldo del empleado"))
        empleados.append((nombre,sueldo))
    return empleados
def imprimir(empleados):
    print("lista de nombres de empleados y sueldos")
    for nombre,sueldo in empleados:
        print(nombre,sueldo)
def sueldo_mayor(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print("Empleado con mayor sueldo:",empleado[0],"su sueldo es:",empleado[1])
def sueldo_menor(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant=cant+1
    print("Cantidad de empleados con sueldo menor a 1000 son:",cant)

empleados=cargar_empleados()
imprimir(empleados)
sueldo_mayor(empleados)
sueldo_menor(empleados)