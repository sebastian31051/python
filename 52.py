#Mostrar una ventana y en su interior dos botones y una label. La label muestra inicialmente el valor 1.
#Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y label")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="black")

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.Incrementar)
        self.boton1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Decrementar", command=self.Decrementar)
        self.boton1.grid(column=0, row=2)

        self.ventana1.mainloop()
    def Incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
    def Decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)
aplicacion1=Aplicacion()