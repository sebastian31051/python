import tkinter as tk
#La librería tkinter está codificada con la metodología de programación orientada a objetos.
#El módulo 'tkinter' tiene una clase llamada 'Tk' que representa una ventana.
# Debemos crear un objeto de dicha clase:
ventana1=tk.Tk()
#Seguidamente llamamos al método 'title' y le pasamos un string con el mensaje que queremos que
#aparezca en la barra del título de la ventana:
ventana1.title("Hola Mundo")
#Para que se muestre la ventana en el monitor debemos llamar por último al método 'mainloop'
#que pertenece a la clase Tk:
ventana1.mainloop()