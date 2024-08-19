#Definir una clase Cliente que almacene un código de cliente y un nombre.
#En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que 
#tienen suspendidas sus cuentas corrientes.
#Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.
class cliente:
    suspendidos=[]
    def __init__(self,codigo,nombre ):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("______________________________")
        
    def suspender(self):
        cliente.suspendidos.append(self.codigo)

cliente1=cliente(1,"sebas")
cliente2=cliente(2,"mariangel")
cliente3=cliente(3,"jose")
cliente4=cliente(4,"ricardo")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(cliente.suspendidos)
