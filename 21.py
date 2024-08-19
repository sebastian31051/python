#Confeccionar una función que reciba el nombre de un operario,
#el pago por hora y la cantidad de horas trabajadas.
#Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.
def calcular_sueldo(nombre,cantidad_horas,pago_por_hora):
    sueldo = pago_por_hora*cantidad_horas
    print(nombre,"trabajo",cantidad_horas,"horas","y cobra un sueldo de:", pago_por_hora,
           "dolares por hora")

calcular_sueldo(nombre = "sebas", cantidad_horas= 8, pago_por_hora=250)
