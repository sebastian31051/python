#Confeccionar un programa que solicite la carga de un valor entero por teclado y 
#luego nos muestre la raíz cuadrada del número y el valor elevado al cubo y el factorial
from math import sqrt, pow as elevado, factorial

valor = int(input("ingrese un valor"))
r1=sqrt(valor)
r2=elevado(valor,3)
r3=factorial(valor)
print("La raiz cuadrada es:",r1)
print("El cubo es:",r2)
print("El factorial es:",r3)