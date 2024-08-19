fecha_tupla=(17,8,2024)
print("fecha tupla:",fecha_tupla)
fecha_lista=list(fecha_tupla)
fecha_lista[0]=31
print("con fecha lista se puede modificar los datos por tanto se cambia el dia",fecha_lista)
fecha_tupla2=tuple(fecha_lista)
print("Y si volvemos a tupla queda con la ultima modificacion pero no se dejara cambiar en tupla",
fecha_tupla2)