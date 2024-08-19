#Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros,
#retornar la suma de dichos parámetros.
def sumar(n1,n2,*lista):
    suma=n1+n2
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma

print(sumar(23,19))
print(sumar(25,13,19))
print(sumar(1,2,3,4,5,6,7))
print(sumar(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2))

def sumatoria(v1,v2,v3,v4,v5,v6,v7,v8):
    return v1 + v2 + v3 + v4 + v5 +v6 + v7 + v8
li=[1,2,3,4,5,6,7,8]

def titulo_subrayado(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


titulo_subrayado("sumatoria")
print(li)
#se llama con un * para citar a todos los numeros que esten dentro del parametro
su=sumatoria(*li)
print(su)