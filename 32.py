#Confeccionar un programa que almacene en un diccionario como clave el nombre de un 
# contacto y como valor su número telefónico:
#1) Carga de contactos y su número telefónico.
#2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
#3) Imprimir la lista completa de contactos con sus números telefónicos.

def cargar():
    contactos={}
    continua="s"
    while continua =="s":
        nombre=input("Ingrese el nombre del contacto")
        numero=int(input("Ingrese el numero del contacto"))
        contactos[nombre]=numero
        continua=input("Ingresa otro contacto s/n?")
    return contactos

def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre de contacto a modificar en el telefono")
    if nombre in contactos:
        numero=input("ingrese el nuevo numero de telefono")
        contactos[nombre]=numero
    else:
        print("no existe un contacto con ese nombre")

def imprimir(contactos):
    print("listado de contactos")
    for nombre in contactos:
        print(nombre,contactos[nombre])

contactos=cargar()
modificar_telefono(contactos)
imprimir(contactos)
