#Confeccionar una función que le enviemos un número de mes como parámetro
#y nos retorne una tupla con todos los nombres de meses que faltan hasta fin de año.
def meses_faltantes(numerones):
    meses=('enero','febrero','marzo','abril','mayo','junio',
           'julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numerones:]
print("imprimir los nombres de meses que faltan hasta fin de año")
numerones=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numerones)
print(mesesfalta)