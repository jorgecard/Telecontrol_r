import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import *

# Obtener la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agregar el nombre del archivo de interfaz
nombre_interfaz = "main.ui"
ruta_interfaz = os.path.join(directorio_actual, nombre_interfaz)

class pantalla(QMainWindow): # precargado de la pantalla
    def __init__(self):
        super(pantalla,self).__init__()
        uic.loadUi(ruta_interfaz, self)
        self.setWindowTitle('Telecontrol y Telemando')
        self.pushButton.clicked.connect(self.suma)
    
    def suma(self):
        op1, op2 = 3,2
        self.label_5.setText(str(op1+op2))
        # try:
        #     op1 = int(self.dato1.toPlainText())
        #     op2 = int(self.dato1.toPlainText())
        #     self.lcdNumber.display(op1+op2)
        # except:
        #     QMessageBox.critical(self, "Error", 'verifique los datos ingresados')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = pantalla()
    d.show()
    sys.exit(app.exec())
