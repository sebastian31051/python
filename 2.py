pieza = 0
x = 1
cantidad = int(input("Ingrese la cantidad de piezas"))
while x <= cantidad:
    tamaño = float(input("Ingrese el tamaño de la pieza"))
    if tamaño >= 1.2 and tamaño <= 1.3:
        pieza = pieza + 1
    x = x + 1  # Esta línea debe estar dentro del bucle
print("El total de piezas en el rango son")
print(pieza)