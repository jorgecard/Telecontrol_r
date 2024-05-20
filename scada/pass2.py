# from pass1 import *

# message = getGroup('Jorge Cardenas', '.%u`B,s6m)v//?5jH=Ae5+<k)')
# print(message)

# import os
# dir_actual = os.path.dirname(os.path.abspath(__file__))

# # Nombre del archivo
# nombre_archivotxt = "archivo_texto.txt"
# ruta = os.path.join(dir_actual, nombre_archivotxt)

# # Texto a agregar
# texto_a_agregar = "Este es un nuevo texto que se agregará al archivo.\n"

# # Abrir el archivo en modo 'append' (agregar)
# with open(ruta, "a") as archivo:
#     # Escribir el texto en el archivo
#     archivo.write(texto_a_agregar)

# print("Texto agregado al archivo con éxito.")


from datetime import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.now()

# Formatear la fecha y hora en el formato deseado
formato_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

# Imprimir la fecha y hora exactas
print("Fecha y hora exactas:", formato_fecha_hora)