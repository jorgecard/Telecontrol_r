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
import pyvisa
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QInputDialog, QLineEdit, QFileDialog
import os
import pandas as pd
from pass1 import *

# Variables
dic_equipment = {
    'Fuente programable': {'Name': 'Chroma_SOURCE', 'Type': 'TCP/IP', 'write_termination' : '\n', 'read_termination' : '\n',
                'open_resource': 'TCPIP0::192.168.222.58::2101::SOCKET', 'timeout':100,
                'widget': 'widget_1', 'data_dict': 'data_dict_1',},
    'Carga programable': {'Name': 'Chroma_LOAD', 'Type': 'TCP/IP', 'write_termination' : '\n', 'read_termination' : '\n',
                'open_resource': 'TCPIP0::192.168.222.59::2101::SOCKET', 'timeout':100,
                'widget': 'widget_2', 'data_dict': 'data_dict_2',},
    'Pila de Hidrógeno': {'Name': 'Pila de Hidrógeno', 'Type': 'SERIAL', 'port': 'COM3', 'baudrate':9600, 'timeout':3,
                'widget': 'widget_3', 'data_dict': 'data_dict_3',},
}

# Diccionario para las variables del equipo 1: 'Fuente programable'
data_dict_1 = {
  'Voltaje':  {'command': 'MEAS:VOLT?', 'color': '#9103A6', 'label': 'V', 'unit': ' [V]', 'graphic':0, 'factor':1,},
  'Corriente':{'command': 'MEAS:CURR?', 'color': '#DF8905', 'label': 'I', 'unit': ' [A]', 'graphic':1, 'factor':1},
  'Potencia': {'command': 'MEAS:POW?',  'color': '#54548D', 'label': 'P', 'unit': ' [W]', 'graphic':2, 'factor':1},
  'THD-V1':   {'command': 'MEAS:VOLT?', 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': ' [%]','graphic':3,'factor':1},
  'Voltaje1': {'command': 'MEAS:VOLT?', 'label': 'Voltaje1', 'unit': ' [kVAh]','factor':1, 'QLabel': 'lineEdit_3'},
  'Corriente1': {'command': 'FETC:CURR?', 'label': 'Corriente1', 'unit': ' [A]','factor':1, 'QLabel': 'lineEdit_4'},
  'Potencia1': {'command': 'MEAS:POW?', 'label': 'Potencia1', 'unit': ' [w]','factor':1/1000, 'QLabel': 'lineEdit_5'},
}

# Diccionario para las variables del equipo 2: 'Carga programable'
data_dict_2 = {
  'Voltaje':  {'command': 'MEAS:VOLT?', 'color': '#9103A6', 'label': 'V', 'unit': ' [V]', 'graphic':0, 'factor':1,},
  'Corriente':{'command': 'MEAS:CURR?', 'color': '#DF8905', 'label': 'I', 'unit': ' [A]', 'graphic':1, 'factor':1},
  'Potencia': {'command': 'MEAS:POW?',  'color': '#54548D', 'label': 'P', 'unit': ' [W]', 'graphic':2, 'factor':1},
  'THD-V2':   {'command': 'MEAS:VOLT?', 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': ' [%]','graphic':3,'factor':1},
  'Voltaje2': {'command': 'MEAS:VOLT?', 'label': 'Voltaje1', 'unit': ' [kVAh]','factor':1, 'QLabel': 'lineEdit_12'},
  'Corriente2': {'command': 'MEAS:CURR?', 'label': 'Corriente1', 'unit': ' [A]','factor':1, 'QLabel': 'lineEdit_13'},
  'Potencia2': {'command': 'MEAS:POW?', 'label': 'Potencia1', 'unit': ' [w]','factor':1/1000, 'QLabel': 'lineEdit_14'},
}

# Diccionario para las variables del equipo 3: 'Pila de Hidrógeno'
data_dict_3 = {
  'Voltaje_g':  {'char_i': 0, 'char_f': 3, 'color': '#9103A6', 'label': 'V', 'unit': ' [V]', 'graphic':0, 'factor':1,},
  'Corriente_g':{'char_i': 6, 'char_f': 9, 'color': '#DF8905', 'label': 'I', 'unit': ' [A]', 'graphic':1, 'factor':1},
  'Temperatura_g':{'char_i': 18, 'char_f': 21, 'color': '#DF8905', 'label': 'C', 'unit': ' [C]', 'graphic':2, 'factor':1},
  'Hydrogen_g':{'char_i': 53, 'char_f': 55, 'color': '#DF8905', 'label': '%', 'unit': ' [%]', 'graphic':3, 'factor':1/10},
  
  'Voltaje':  {'char_i': 0, 'char_f': 3, 'label': 'Voltaje', 'unit': ' [V]',   'factor':1, 'QLabel': 'lineEdit_15'},
  'Corriente':{'char_i': 6, 'char_f': 9, 'label': 'Corriente', 'unit': ' [A]', 'factor':1, 'QLabel': 'lineEdit_16'},
  'Temperatura': {'char_i': 12, 'char_f': 15, 'label': 'temperature', 'unit': ' [C]','factor':1, 'QLabel': 'lineEdit_19'},
  'Temperatura A': {'char_i': 18, 'char_f': 21, 'label': 'a temperature', 'unit': ' [C]','factor':1, 'QLabel': 'lineEdit_25'},
  'Temperatura T': {'char_i': 24, 'char_f': 27, 'label': 't temperature', 'unit': ' [C]','factor':1, 'QLabel': 'lineEdit_26'},
  'Speed of fans': {'char_i': 30, 'char_f': 33, 'label': 'Speed of fans', 'unit': ' [%]','factor':1/10, 'QLabel': 'lineEdit_18'},
  'o voltage': {'char_i': 37, 'char_f': 40, 'label': 'o voltage', 'unit': ' [V]','factor':1, 'QLabel': 'lineEdit_23'},
  'o current': {'char_i': 44, 'char_f': 48, 'label': 'o current', 'unit': ' [A]','factor':1, 'QLabel': 'lineEdit_24'},
  'Hydrogen concentration': {'char_i': 53, 'char_f': 55, 'label': 'Hydrogen', 'unit': ' [%]','factor':1/10, 'QLabel': 'lineEdit_20'},
}

# Diccionario de labels del eje y para cada gráfico
y_labels = {
    0: '[V]',
    1: '[A]',
    2: '[]',
    3: '[%]'
}

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = os.path.join(dir_actual, "QtScada")
nombre_interfaz = "SCADA.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_logo = "nano.png"
ruta_logo = os.path.join(dir_interfaz, nombre_logo)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = [fig.add_subplot(221), fig.add_subplot(222), fig.add_subplot(223), fig.add_subplot(224)]
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()

class LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(ruta_interfaz, self)
        self.resize(888, 600)
        
        self.ui.label_2.setPixmap(QtGui.QPixmap(os.path.join(dir_interfaz, "esquema3.png")))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Telecontrol y Telemando')
        
        self.devices_list = [val['open_resource'] if 'open_resource' in val else val['port'] for val in dic_equipment.values()]
        
        # Establecer la página predeterminada al arrancar
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        self.bt_log_in.clicked.connect(self.log_in)
        # acceder a las paginas
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_login))
        self.ui.pushButton_gen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_alarms.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_alarms))
        self.ui.pushButton_log_ins.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_log_ins))
        self.pushButton_log_ins.clicked.connect(self.activate_sheet_log_ins)
        self.pushButton_7.clicked.connect(self.open_dialog_box)
        self.pushButton_set_pow.clicked.connect(self.handle_set_pow_click)
        # inicializar load and source
        # self.pushButton_5.clicked.connect(self.set_source)
        # self.pushButton_6.clicked.connect(self.set_load)
        self.set_source()
        self.set_load()

        # menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        # estado inicial botones
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_log_ins.setEnabled(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_eye.clicked.connect(self.toggle_password_visibility)
               
        # Configuraciones de visualización
        self.window_length = 50  # Establece la longitud de la ventana de visualización en milisegundos
        self.interval = 100  # Establece el intervalo de actualización del gráfico en milisegundos.

        self.plot_list = []
        self.legends = []
        self.data_store = {}  # Inicializar el data_store
        
        # Inicializar gráficos
        self.init_graphics()

        # Iniciar los hilos de lectura de los dispositivos
        self.threads = []
        self.init_visa_threads()
        self.init_serial_threads()
                
        # Inicializar el temporizador para actualizar los gráficos
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all_plots)
        self.timer.start(self.interval)
        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.closeEvent = self.close_instruments

        # Inicializar temporizador para setear potencia
        self.pow_index = 0
        self.pow_timer = QTimer()
        self.pow_timer.timeout.connect(self.set_next_pow)
    
    def init_graphics(self):
        self.graphs = {}
        for key, val in dic_equipment.items():
            widget_name = val['widget']
            widget = getattr(self.ui, widget_name)
            layout = QVBoxLayout()
            canvas = MplCanvas(self, width=5, height=4, dpi=100)
            layout.addWidget(canvas)
            widget.setLayout(layout)
            self.graphs[widget_name] = canvas.axes
 
    def init_serial_threads(self):
        for equipment in dic_equipment.values():
            if equipment['Type'] == 'SERIAL':
                thread = SerialPlot(
                    equipment['port'],
                    equipment['baudrate'],
                    timeout=equipment['timeout'],
                    data_dict=globals()[equipment['data_dict']],
                    widget_id=equipment['widget']
                )
                self.threads.append(thread)
                thread.new_data.connect(self.store_data)
                thread.start()
    
    def init_visa_threads(self):
        for equipment in dic_equipment.values():
            if equipment['Type'] == 'TCP/IP':
                thread = VisaPlot(
                    equipment['open_resource'],
                    equipment['write_termination'],
                    equipment['read_termination'],
                    equipment['timeout'],
                    data_dict=globals()[equipment['data_dict']],
                    widget_id=equipment['widget']
                )
                self.threads.append(thread)
                thread.new_data.connect(self.store_data)
                thread.start()
    
    def store_data(self, data, widget_id):
        self.data_store[widget_id] = data

    def update_all_plots(self):
        for widget_id, data in self.data_store.items():
            self.update_plot(data, widget_id)

    def update_plot(self, data, widget_id):
        axes_list = self.graphs[widget_id]
        for ax in axes_list:
            ax.clear()
        data_dict_name = self.find_data_dict_name(widget_id)
        for key, value in data.items():
            if 'graphic' in globals()[data_dict_name][key]:
                color = self.find_color(data_dict_name, key)
                graphic_id = self.find_graphic_id(data_dict_name, key)
                if len(value) > self.window_length:
                    value_to_plot = value[-self.window_length:]
                else:
                    value_to_plot = value
                axes_list[graphic_id].plot(value_to_plot, label=key, color=color)
                axes_list[graphic_id].set_ylabel(y_labels[graphic_id])  # Establecer el label del eje y
            if 'QLabel' in globals()[data_dict_name][key]:
                qlabel_name = globals()[data_dict_name][key]['QLabel']
                qlabel = getattr(self.ui, qlabel_name)
                qlabel.setText(f"{value[-1]:.2f}")
        for ax in axes_list:
            ax.legend()
        # Utilizamos el canvas del gráfico para actualizar el widget
        canvas = axes_list[0].figure.canvas
        canvas.draw()

    def find_data_dict_name(self, widget_id):
        for eq_name, eq_data in dic_equipment.items():
            if eq_data['widget'] == widget_id:
                return eq_data['data_dict']
        return None
    
    def find_color(self, data_dict_name, key):
        if 'color' in globals()[data_dict_name][key]:
            return globals()[data_dict_name][key]['color']
        return '#000000'  # Default color if not found

    def find_graphic_id(self, data_dict_name, key):
        return globals()[data_dict_name][key]['graphic']
    
    def mover_menu(self):
        width = self.ui.frame_control.width()
        normal = 0
        extender = 200 if width == 0 else normal
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
    
    def open_dialog_box(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Open File', dir_actual, 'All Files (*)')
        self.path_lb.setText(self.filename)
        self.load_data()
        
    def load_data(self):
        df = pd.read_excel(self.filename)
        # self.values_list = df.iloc[0, 3:8].tolist()
        self.values_list = df.iloc[11, 108:].tolist()
        self.values_list = [val * 1 for val in self.values_list]
        self.pow_index = 0
        self.pow_timer.start(5000)  # Iniciar el temporizador para setear potencia cada 5 segundos

    def handle_set_pow_click(self):
        try:
            kpow = float(self.ui.line_c_pow.text())
            self.set_pow(kpow)
        except ValueError:
            print("Error: Please enter a valid number in the line_c_pow field.")
    
    def set_pow(self, kpow):
        try:
            rm = pyvisa.ResourceManager()
            resource = dic_equipment['Carga programable']['open_resource']
            instrument = rm.open_resource(resource)
            instrument.write_termination = dic_equipment['Carga programable']['write_termination']
            instrument.read_termination = dic_equipment['Carga programable']['read_termination']
            instrument.timeout = dic_equipment['Carga programable']['timeout']
            
            if 0 < kpow < 2.8:
                instrument.write(f'VOLT:STAT:ILIM {kpow * 1000 / 49}')
                print(f'kpow seteada: {kpow}')
            else:
                print(f'Carga fuera de rango: {kpow}')
            instrument.close()
        except Exception as e:
            print(f"Error setting pow: {e}")

    def set_next_pow(self):
        if self.pow_index < len(self.values_list):
            self.set_pow(self.values_list[self.pow_index])
            print(f'setting pow [{self.pow_index}]: {self.values_list[self.pow_index]}')
            self.pow_index += 1
        else:
            self.pow_timer.stop()
            print('Fin lista')
            
    def set_load(self):
        try:
            rm = pyvisa.ResourceManager()
            resource = dic_equipment['Carga programable']['open_resource']
            instrument = rm.open_resource(resource)
            instrument.write_termination = dic_equipment['Carga programable']['write_termination']
            instrument.read_termination = dic_equipment['Carga programable']['read_termination']
            instrument.timeout = dic_equipment['Carga programable']['timeout']
            
            instrument.write('MODE CVL')
            instrument.write('MODE?')
            try:
                response = instrument.read()
                print(f": {response}")
            except pyvisa.errors.VisaIOError as e:
                print(f"Error de lectura: {e}")
            instrument.write('VOLT:STAT:L1 0')
            instrument.write('VOLT:STAT:L2 0')
            instrument.write('VOLT:STAT:ILIM 1.0')
            instrument.write('LOAD ON')
            instrument.write('LOAD?')
            try:
                response = instrument.read()
                print(f": {response}")
            except pyvisa.errors.VisaIOError as e:
                print(f"Error de lectura: {e}")
            instrument.close()
        except Exception as e:
            print(f"Error setting load: {e}")
    
    def set_source(self):
        try:
            rm = pyvisa.ResourceManager()
            resource = dic_equipment['Fuente programable']['open_resource']
            instrument = rm.open_resource(resource)
            instrument.write_termination = dic_equipment['Fuente programable']['write_termination']
            instrument.read_termination = dic_equipment['Fuente programable']['read_termination']
            instrument.timeout = dic_equipment['Fuente programable']['timeout']
            instrument.write('SOUR:CURR 8.0')
            instrument.write('SOUR:VOLT 49.0')
            instrument.write('CONF:OUTPut ON')
            instrument.write('CONF:OUTPut?')
            try:
                response = instrument.read()
                print(f": {response}")
            except pyvisa.errors.VisaIOError as e:
                print(f"Error de lectura: {e}")
            instrument.close()
        except Exception as e:
            print(f"Error setting Source: {e}")
            
    def close_instruments(self, event):
        for thread in self.threads:
            if isinstance(thread, VisaPlot):
                thread.instrument.close()
            elif isinstance(thread, SerialPlot):
                thread.ser.close()
        event.accept()
        # # Off Source
        # try:
        #     rm = pyvisa.ResourceManager()
        #     resource = dic_equipment['Fuente programable']['open_resource']
        #     instrument = rm.open_resource(resource)
        #     instrument.write_termination = dic_equipment['Fuente programable']['write_termination']
        #     instrument.read_termination = dic_equipment['Fuente programable']['read_termination']
        #     instrument.timeout = dic_equipment['Fuente programable']['timeout']
        #     instrument.write('CONF:OUTPut OFF')
        #     instrument.write('CONF:OUTPut?')
        #     try:
        #         response = instrument.read()
        #         print(f": {response}")
        #     except pyvisa.errors.VisaIOError as e:
        #         print(f"Error de lectura: {e}")
        #     instrument.close()
        # except Exception as e:
        #     print(f"Error setting Source: {e}")
        # # Off load
        # try:
        #     rm = pyvisa.ResourceManager()
        #     resource = dic_equipment['Carga programable']['open_resource']
        #     instrument = rm.open_resource(resource)
        #     instrument.write_termination = dic_equipment['Carga programable']['write_termination']
        #     instrument.read_termination = dic_equipment['Carga programable']['read_termination']
        #     instrument.timeout = dic_equipment['Carga programable']['timeout']
            
        #     instrument.write('VOLT:STAT:L1 0')
        #     instrument.write('VOLT:STAT:L2 0')
        #     instrument.write('VOLT:STAT:ILIM 1.0')
        #     instrument.write('LOAD 0')
        #     instrument.write('LOAD?')
        #     try:
        #         response = instrument.read()
        #         print(f": {response}")
        #     except pyvisa.errors.VisaIOError as e:
        #         print(f"Error de lectura: {e}")
        #     instrument.close()
        # except Exception as e:
        #     print(f"Error setting load: {e}")
               
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
    new_data = QtCore.pyqtSignal(dict, str)

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
                if self.ser.in_waiting > 0:
                    line = self.ser.readline().decode('utf-8').strip()
                    self.process_data(line)
                    self.new_data.emit(self.data_buffer, self.widget_id)
                time.sleep(1)
            except Exception as e:
                print(f"Error reading serial data: {e}")

    def process_data(self, line):
        for key, settings in self.data_dict.items():
            char_i = settings['char_i']
            char_f = settings['char_f']
            value = float(line[char_i:char_f]) * settings['factor']
            self.data_buffer[key].append(value)

class VisaPlot(QtCore.QThread):
    new_data = QtCore.pyqtSignal(dict, str)

    def __init__(self, resource, write_termination, read_termination, timeout, data_dict, widget_id):
        super().__init__()
        self.resource = resource
        self.write_termination = write_termination
        self.read_termination = read_termination
        self.timeout = timeout
        self.data_dict = data_dict
        self.widget_id = widget_id
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource(resource)
        self.instrument.timeout = timeout
        self.instrument.write_termination = write_termination
        self.instrument.read_termination = read_termination
        self.data_buffer = {key: [] for key in data_dict.keys()}

    def run(self):
        while True:
            try:
                for key, settings in self.data_dict.items():
                    self.instrument.write(settings['command'])
                    response = self.instrument.read()
                    value = float(response) * settings['factor']
                    self.data_buffer[key].append(value)
                self.new_data.emit(self.data_buffer, self.widget_id)
                time.sleep(1)  # Ajustar el intervalo de muestreo según sea necesario
            except Exception as e:
                print(f"Error reading VISA data: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LIVE_PLOT_APP()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()