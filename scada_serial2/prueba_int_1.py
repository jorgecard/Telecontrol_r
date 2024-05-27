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
import os
import pandas as pd
from pass1 import *

# Variables
dic_equipment = {
    'ESP-32': {'Name': 'ESP-32', 'Manufacturer': 'Silicon Labs', 'baudrate':115200,
                'ip': '192.168.222.222', 'port': 'COM6', 'timeout':3,
                'page': 1, 'data_dict': 'data_dict_1', 'comand': 'read_holding_registers', 'pack_method': 'method_2'},
    'Arduino nano': {'Name': 'Arduino nano', 'Manufacturer': 'wch.cn', 'baudrate':9600,
                 'ip': '192.168.222.180', 'port': 'COM7', 'timeout':3,
                 'page': 2, 'data_dict': 'data_dict_2', 'comand': 'read_input_registers', 'pack_method': 'method_1'},
}

# Diccionario para las variables del equipo 1:
data_dict_1 = {
  'Tensión L1-N': {'offset': 1, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L1-N', 'unit': ' [V]', 'graphic':0, 'factor':1},
  'Tensión L2-N': {'offset': 3, 'reg': 2, 'color': '#9103A6', 'label': 'Tension L2-N', 'unit': ' [V]','graphic':0, 'factor':1},
  'Tensión L3-N': {'offset': 5, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L3-N', 'unit': ' [V]','graphic':0,'factor':1},
  'Tensión L1-L2': {'offset': 7, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L1-L2', 'unit': ' [V]','graphic':0,'factor':1},
  'Tensión L2-L3': {'offset': 9, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L2-L3', 'unit': ' [V]','graphic':0,'factor':1},
  'Tensión L3-L1': {'offset': 11, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L3-L1', 'unit': ' [V]','graphic':0,'factor':1},
  'I-L1': {'offset': 13, 'reg': 2, 'color': '#DF8905', 'label': 'I-L1', 'unit': ' [A]','graphic':1,'factor':1},
  'I-L2': {'offset': 15, 'reg': 2, 'color': '#DF8905', 'label': 'I-L2', 'unit': ' [A]','graphic':1,'factor':1},
  'I-L3': {'offset': 17, 'reg': 2, 'color': '#DF8905', 'label': 'I-L3', 'unit': ' [A]','graphic':1,'factor':1},
  'E-S': {'offset': 63, 'reg': 2, 'color': '#54548D', 'label': 'E-S', 'unit': ' [VA]','graphic':2,'factor':1},
  'E-P': {'offset': 65, 'reg': 2, 'color': '#558D54', 'label': 'E-P', 'unit': ' [W]','graphic':2,'factor':-1},
  'E-Q': {'offset': 63, 'reg': 2, 'color': '#547E8D', 'label': 'E-Q', 'unit': ' [VAR]','graphic':2,'factor':1},
  'THD-V1': {'offset': 261, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': ' [%]','graphic':3,'factor':1},
  'THD-V2': {'offset': 263, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V2', 'unit': ' [%]','graphic':3,'factor':1},
  'THD-V3': {'offset': 265, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V3', 'unit': ' [%]','graphic':3,'factor':1},
  'THD-I1': {'offset': 267, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I1', 'unit': ' [%]','graphic':3,'factor':1},
  'THD-I2': {'offset': 269, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I2', 'unit': ' [%]','graphic':3,'factor':1},
  'THD-I3': {'offset': 271, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I3', 'unit': ' [%]','graphic':3,'factor':1},
  'Energía Aparente': {'offset': 2817, 'reg': 2, 'label': 'Energía Aparente', 'unit': ' [kVAh]','factor':1/1000000},
}
# Diccionario para las variables del equipo 2:
data_dict_2 = {
    'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic': 0, 'factor': 1},
    'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]', 'graphic': 1, 'factor': 0.1},
    'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]', 'graphic': 2, 'factor': 1},
    'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]', 'graphic': 3, 'factor': 0.01},
    # 'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]', 'graphic': 4, 'factor': 0.01},
    # 'Energía Neta': {'offset': 33, 'reg': 1, 'color': '-w', 'label': 'Energía Neta', 'unit': ' [kWh]', 'graphic': 5, 'factor': 1},
    # 'Frecuencia': {'offset': 23, 'reg': 1, 'label': 'Frecuencia', 'unit': ' [Hz]', 'factor': 1},
}

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = dir_actual + r"\QtScada"
nombre_interfaz = "SCADA.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_logo = "nano.png"
ruta_logo = os.path.join(dir_interfaz, nombre_logo)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class SerialPlot:
    def __init__(self, port='COM6', baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        self.x = np.arange(0, 100, 1)
        self.y = np.zeros(100)
        self.ptr = 0
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')  # Set background to white
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pg.mkPen(color='b', width=2))
        
        # Start the timer for updating the plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)  # Interval in milliseconds
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def read_data(self):
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                data = float(line)
                return data
            except ValueError:
                return None
        return None

    def update_plot(self):
        data = self.read_data()
        if data is not None:
            self.y = np.roll(self.y, -1)
            self.y[-1] = data
            self.data_line.setData(self.x, self.y)

    def close(self):
        self.ser.close()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi(ruta_interfaz, self)
        
        # Set the window icon
        self.setWindowIcon(QtGui.QIcon(ruta_logo))
        
        # Serial plot setup
        self.serial_plot = SerialPlot(port='COM6', baudrate=115200, timeout=1)
        self.graph_layout = self.findChild(QVBoxLayout, 'graphLayout')
        self.graph_layout.addWidget(self.serial_plot.graphWidget)
        
        # Ensure the plot updates
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)
        
    def update_plot(self):
        self.serial_plot.update_plot()

    def closeEvent(self, event):
        self.serial_plot.close()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
