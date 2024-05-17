import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import *

# Obtener la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agregar el nombre del archivo de interfaz
nombre_interfaz = "main.ui"
ruta_interfaz = os.path.join(directorio_actual, nombre_interfaz)

class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla,self).__init__()
        uic.loadUi(ruta_interfaz, self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = pantalla()
    d.show()
    sys.exit(app.exec())