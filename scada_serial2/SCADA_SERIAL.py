import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import queue
import numpy as np
import struct  # Para decodificar los datos
from pymodbus.client.sync import ModbusTcpClient  # Para la conexión
import serial
import serial.tools.list_ports
import time
import pdb
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QVBoxLayout, QWidget
# from PyQt5.QtMultimedia import QAudioDeviceInfo, QAudio, QCameraInfo
import os
import pandas as pd
from pass1 import *

# Variables
dic_equipment = {
    'ESP-32': {'Name': 'ESP-32', 'Manufacturer': 'Silicon Labs', 'baudrate':115200,
                'ip': '192.168.222.222', 'port': 'COM6', 'timeout':3,
                'page': 1, 'data_dict': 'data_dict_1', 'comand': 'read_holding_registers', 'pack_method': 'method_2'},
    'Arduino nano': {'Name': 'Arduino nano', 'Manufacturer': 'wch.cn', 'baudrate':9600,
                 'ip': '192.168.222.180', 'port': 'COM8', 'timeout':3,
                 'page': 2, 'data_dict': 'data_dict_2', 'comand': 'read_input_registers', 'pack_method': 'method_1'},
}

# Diccionario para las variables del equipo 1:
data_dict_1 = {
  'Tensión L1-N': {'offset': 1, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L1-N', 'unit': ' [V]', 'graphic':0, 'factor':1,},
  'Tensión L2-N': {'offset': 3, 'reg': 2, 'color': '#9103A6', 'label': 'Tension L2-N', 'unit': ' [V]','graphic':0, 'factor':1,},
  'Tensión L3-N': {'offset': 5, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L3-N', 'unit': ' [V]','graphic':0,'factor':1,},
#   'Tensión L1-L2': {'offset': 7, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L1-L2', 'unit': ' [V]','graphic':0,'factor':1},
#   'Tensión L2-L3': {'offset': 9, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L2-L3', 'unit': ' [V]','graphic':0,'factor':1},
#   'Tensión L3-L1': {'offset': 11, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L3-L1', 'unit': ' [V]','graphic':0,'factor':1},
#   'I-L1': {'offset': 13, 'reg': 2, 'color': '#DF8905', 'label': 'I-L1', 'unit': ' [A]','graphic':1,'factor':1},
#   'I-L2': {'offset': 15, 'reg': 2, 'color': '#DF8905', 'label': 'I-L2', 'unit': ' [A]','graphic':1,'factor':1},
#   'I-L3': {'offset': 17, 'reg': 2, 'color': '#DF8905', 'label': 'I-L3', 'unit': ' [A]','graphic':1,'factor':1},
#   'E-S': {'offset': 63, 'reg': 2, 'color': '#54548D', 'label': 'E-S', 'unit': ' [VA]','graphic':2,'factor':1},
#   'E-P': {'offset': 65, 'reg': 2, 'color': '#558D54', 'label': 'E-P', 'unit': ' [W]','graphic':2,'factor':-1},
#   'E-Q': {'offset': 63, 'reg': 2, 'color': '#547E8D', 'label': 'E-Q', 'unit': ' [VAR]','graphic':2,'factor':1},
#   'THD-V1': {'offset': 261, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': ' [%]','graphic':3,'factor':1},
#   'THD-V2': {'offset': 263, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V2', 'unit': ' [%]','graphic':3,'factor':1},
#   'THD-V3': {'offset': 265, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V3', 'unit': ' [%]','graphic':3,'factor':1},
#   'THD-I1': {'offset': 267, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I1', 'unit': ' [%]','graphic':3,'factor':1},
#   'THD-I2': {'offset': 269, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I2', 'unit': ' [%]','graphic':3,'factor':1},
#   'THD-I3': {'offset': 271, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I3', 'unit': ' [%]','graphic':3,'factor':1},
#   'Energía Aparente': {'offset': 2817, 'reg': 2, 'label': 'Energía Aparente', 'unit': ' [kVAh]','factor':1/1000000},
}
# Diccionario para las variables del equipo 2:
data_dict_2 = {
    'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic': 0, 'factor': 1},
    # 'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]', 'graphic': 1, 'factor': 0.1},
    # 'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]', 'graphic': 2, 'factor': 1},
    # 'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]', 'graphic': 3, 'factor': 0.01},
    # 'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]', 'graphic': 4, 'factor': 0.01},
    # 'Energía Neta': {'offset': 33, 'reg': 1, 'color': '-w', 'label': 'Energía Neta', 'unit': ' [kWh]', 'graphic': 5, 'factor': 1},
    # 'Frecuencia': {'offset': 23, 'reg': 1, 'label': 'Frecuencia', 'unit': ' [Hz]', 'factor': 1},
}

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = dir_actual + r"\QtScada"
nombre_interfaz = "SCADA_simple.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_logo = "nano.png"
ruta_logo = os.path.join(dir_interfaz, nombre_logo)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # fig, self.axes = plt.subplots(2, 2, figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()

class LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        # self.stream = stream
        super().__init__()
        # QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi(ruta_interfaz, self)
        self.resize(888, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Telecontrol y Telemando')
        
        self.devices_list = [val['port'] for val in dic_equipment.values()]
        
        # Establecer la página predeterminada al arrancar
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        self.bt_log_in.clicked.connect(self.log_in)
        #acceder a las paginas
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_login))			
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_log_ins.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_log_ins))
        self.pushButton_log_ins.clicked.connect(self.activate_sheet_log_ins)

        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        # estado inicial botones
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_log_ins.setEnabled(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_eye.clicked.connect(self.toggle_password_visibility)
               
        # Configuraciones de visualización
        self.window_length = 50  # Establece la longitud de la ventana de visualización en milisegundos
        self.interval = 50  # Establece el intervalo de actualización del gráfico en milisegundos.

        self.plot_list = []
        self.legends = []
        
        # Inicializar gráficos
        self.init_graphics()

        # Iniciar los hilos de lectura de los dispositivos
        self.threads = []
        self.init_serial_threads()
    
    def init_graphics(self):
        self.graphs = {}
        self.graph_widgets = [self.ui.widget_1, self.ui.widget_2]

        for i, widget in enumerate(self.graph_widgets):
            layout = QVBoxLayout()
            canvas = MplCanvas(self, width=5, height=4, dpi=100)
            layout.addWidget(canvas)
            widget.setLayout(layout)
            self.graphs[i] = canvas.axes
 
    def init_serial_threads(self):
        for equipment in dic_equipment.values():
            thread = SerialPlot(
                equipment['port'],
                equipment['baudrate'],
                timeout=equipment['timeout'],
                data_dict=globals()[equipment['data_dict']],
                widget_id=equipment['page'] - 1  # Ajustamos a índice 0
            )
            self.threads.append(thread)
            thread.new_data.connect(self.update_plot)
            thread.start()

    def update_plot(self, data, widget_id):
        axes = self.graphs[widget_id]
        axes.clear()
        for key, value in data.items():
            if len(value) > self.window_length:
                value_to_plot = value[-self.window_length:]
            else:
                value_to_plot = value
            axes.plot(value_to_plot, label=key)
        axes.legend()
        self.graph_widgets[widget_id].layout().itemAt(0).widget().draw()

    def mover_menu(self):
        if True:
            width = self.ui.frame_control.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
            
    def log_in(self):
        self.message = getGroup(self.username.text(), self.password.text())
        _translate = QtCore.QCoreApplication.translate
        self.message_lg.setText(_translate("Form", self.message))
        if (self.message == 'JerarquiaA'):
            # Borro de pantalla
            self.username.setText('')
            self.password.setText('')
            # estado inicial botones
            self.pushButton_1.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_log_ins.setEnabled(True)
        elif (self.message == 'JerarquiaB'):
            # Borro de pantalla
            self.username.setText('')
            self.password.setText('')
            # estado inicial botones
            self.pushButton_1.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_log_ins.setEnabled(False)
            
    def activate_sheet_log_ins(self):     
        df = pd.read_csv('registros.csv')
        df = df.drop(df.columns[0], axis=1)
        self.table_log_in.setColumnCount(len(df.columns))
        self.table_log_in.setRowCount(len(df))
        self.table_log_in.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table_log_in.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))
        
    def toggle_password_visibility(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Password:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)

class SerialPlot(QtCore.QThread):
    new_data = QtCore.pyqtSignal(dict, int)

    def __init__(self, port, baudrate, timeout, data_dict, widget_id):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.data_dict = data_dict
        self.widget_id = widget_id
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.data_buffer = {key: [] for key in data_dict.keys()}

    def run(self):
        while True:
            try:
                if self.ser.in_waiting:
                    line = self.ser.readline().decode().strip()
                    self.process_data(line)
                    self.new_data.emit(self.data_buffer, self.widget_id)
            except Exception as e:
                print(f"Error reading serial data: {e}")

    def process_data(self, line):
        values = line.split(' ')
        print(f'values: {values}')
        # for key, settings in self.data_dict.items():
        #     print(f'key: {key}')
        #     pos = settings['pos']
        #     value = float(values[pos])
        #     self.data_buffer[key].append(value)
        for i, (key, settings) in enumerate(self.data_dict.items()):
            # print(f'i: {i}, key: {key}')
            # pos = settings['pos']
            # value = float(values[pos])
            value = float(values[i])
            self.data_buffer[key].append(value)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LIVE_PLOT_APP()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = LIVE_PLOT_APP()
    main_window.show()
    sys.exit(app.exec_())