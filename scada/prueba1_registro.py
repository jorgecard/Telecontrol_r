from PyQt5 import QtWidgets, uic
import os
import sys

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = dir_actual
nombre_interfaz = "prueba1_registro.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_interfaz = "prueba1_registro2.ui"
ruta_interfaz2 = os.path.join(dir_interfaz, nombre_interfaz)

# Iniciar aplicación 
app = QtWidgets.QApplication([])

# Cargar archivos .ui
login = uic.loadUi(ruta_interfaz)
entrar = uic.loadUi(ruta_interfaz2)

def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if name == "Master" and password == "1234":
        gui_entrar()

def gui_entrar():
    login.hide()
    entrar.show()

def toggle_password_visibility():
    if login.lineEdit_2.echoMode() == QtWidgets.QLineEdit.Password:
        login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        login.pushButton_act.setText("Ocultar Contraseña")
    else:
        login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        login.pushButton_act.setText("Mostrar Contraseña")

# Configuración del campo de contraseña
login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

# Conexión del botón
login.pushButton_act.clicked.connect(toggle_password_visibility)

# Botones
login.pushButton.clicked.connect(gui_login)

# Ejecutable
login.show()
app.exec()
