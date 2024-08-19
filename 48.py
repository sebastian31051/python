#Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista 
#con los nombres de los hijos.
#Definir el método especial __str__ que retorne un string con el nombre del padre,
#la madre y de todos sus hijos.
class familia:
    def __init__(self,padre,madre,hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos
    def __str__(self):
        cadena=self.padre+","+self.madre
        for hi in self.hijos:
            cadena=cadena+","+hi
        return cadena
familia1=familia("German","Leidy",["Sebas","Mariangel","Joselin"])
familia2=familia("Pug","Pug hembra",["Minipug","Minipug2","Minipugsin"])
familia3=familia("Luis","maria",["marcos"],)
print(familia1)
print(familia2)
print(familia3)