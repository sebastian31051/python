#Definir una clase llamada Punto con dos atributos x e y.
#Crearle el método especial __str__ para retornar un string con el formato (x,y).
class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
punto1=punto(10,4)
punto2=punto(3,6)
print(punto1)
print(punto2)