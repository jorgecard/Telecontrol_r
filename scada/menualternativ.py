import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic

# Obtener la ruta actual y la ruta del archivo de interfaz
dir_actual = os.path.dirname(os.path.abspath(__file__))
nombre_interfaz = "menudefinitivo.ui"
ruta_interfaz = os.path.join(dir_actual, nombre_interfaz)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        try:
            uic.loadUi(ruta_interfaz, self)
        except Exception as e:
            print(f"Error loading UI file: {e}")
            sys.exit(1)

        # Acceder a pushButton dentro de frame_control y conectar su señal
        try:
            self.frame_control.findChild(QPushButton, 'pushButton').clicked.connect(self.page_login)
        except AttributeError:
            print("Error: pushButton not found within frame_control in the UI file.")
            sys.exit(1)

        # Esconder el botón bt_comprimir si existe
        try:
            self.bt_comprimir.hide()
        except AttributeError:
            print("Warning: bt_comprimir not found in the UI file.")

    def page_login(self):
        # Lógica para cambiar a la página de login
        
        print("Login button clicked")
        # Aquí va la lógica específica para manejar el evento

####### Interfaz login
# Agrega aquí los métodos y la lógica relacionados con la interfaz de login

####### Interfaz Ampere
# Agrega aquí los métodos y la lógica relacionados con la interfaz de Ampere

###### Interfaz Sentron
# Agrega aquí los métodos y la lógica relacionados con la interfaz de Sentron

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
