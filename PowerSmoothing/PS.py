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
from func1 import *

# Variables
dic_equipment = {
    'Panels': {'Name': 'Panels', 'Type': 'TCP/IP', 
               'ip' : '192.168.222.9', 'port' : 502, 'timeout':3,
               'widget': 'widget_1', 'data_dict': 'data_dict_1',},
    'Bat_Li': {'Name': 'Bat_Li', 'Type': 'TCP/IP', 
               'ip' : '192.168.222.12', 'port' : 502, 'timeout':3,
               'widget': 'widget_2', 'data_dict': 'data_dict_2',},
    'super_C': {'Name': 'super_C', 'Type': 'TCP/IP', 
               'ip' : '192.168.222.14', 'port' : 502, 'timeout':3,
               'widget': 'widget_3', 'data_dict': 'data_dict_3',},
}

# Diccionario 1
data_dict_1 = {
    'Potencia': {'label': 'P 1', 'unit': ' [kW]', 'address': 20, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_15', 'graphic':3},
    'Voltaje':  {'label': 'V 1', 'unit': ' [V]',  'address': 5,  'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_13'},
    'Corriente':{'label': 'I 1', 'unit': ' [A]',  'address': 11, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_14'},
    
    'V r':  {'label': 'Vr', 'unit': ' [V]', 'address': 5, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_18', 'graphic':0,'color': '#ADD8E6'},
    'V s':  {'label': 'Vs', 'unit': ' [V]', 'address': 6, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_19', 'graphic':0,'color': '#4682B4'},
    'V t':  {'label': 'Vt', 'unit': ' [V]', 'address': 7, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_20', 'graphic':0,'color': '#00008B'},
    
    'I r':  {'label': 'Ir', 'unit': ' [A]', 'address': 11, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_21','graphic':1,'color': '#800080'},
    'I s':  {'label': 'Is', 'unit': ' [A]', 'address': 12, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_22','graphic':1,'color': '#9370DB'},
    'I t':  {'label': 'It', 'unit': ' [A]', 'address': 13, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_23','graphic':1,'color': '#4B0082'},
    
    'P':  {'label': 'P', 'unit': ' [kW]', 'address': 20, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_24','graphic':2,'color': '#FF6347'},
    'Q':  {'label': 'Q', 'unit': ' [kVAr]', 'address': 21, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_25','graphic':2,'color': '#FF69B4'},
    'S':  {'label': 'S', 'unit': ' [kVA]', 'address': 22, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_26','graphic':2,'color': '#8B0000'},
}

# Diccionario 2 Batería  litio
data_dict_2 = {   
    'Voltaje':  {'label': 'V',   'unit': ' [V]', 'address': 25, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_3'},
    'Corriente':{'label': 'I',   'unit': ' [A]', 'address': 26, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_4'},
    'Potencia': {'label': 'P',   'unit': ' [kW]','address': 27, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_5'},
    'SOC_2':      {'label': 'SOC', 'unit': ' [%]', 'address': 5,  'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_16'},
    'SOH_2':      {'label': 'SOH', 'unit': ' [%]', 'address': 6,  'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_48',},
    
    'SOC':      {'label': 'SOC ', 'unit': ' [%]', 'address': 5,  'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_52', 'graphic':3, 'color': '#9103A6',},
    'SOH':      {'label': 'SOH',  'unit': ' [%]', 'address': 6,  'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_53', 'graphic':3, 'color': '#ADD8E6',},
    'Vol bat':  {'label': 'Vbat', 'unit': ' [V]', 'address': 7,  'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_54',  'graphic':0, 'color': '#00008B',},
    
    #Conexión DC
    'V':  {'label': 'V_DC', 'unit': ' [V]',  'address': 25, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_49','graphic':0,'color': '#FF0000'},
    'I':  {'label': 'I_DC', 'unit': ' [A]',  'address': 26, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_50','graphic':1,'color': '#FF0000'},
    'P':  {'label': 'P_DC', 'unit': ' [kW]', 'address': 27, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_51','graphic':2,'color': '#FF0000'},
    
    #Conexión AC
    'V r':  {'label': 'Vr', 'unit': ' [V]', 'address': 28, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_27','graphic':0,'color': '#ADD8E6'},
    'V s':  {'label': 'Vs', 'unit': ' [V]', 'address': 29, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_28','graphic':0,'color': '#4682B4'},
    'V t':  {'label': 'Vt', 'unit': ' [V]', 'address': 30, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_29','graphic':0,'color': '#00008B'},
    
    'I r':  {'label': 'Ir', 'unit': ' [A]', 'address': 34, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_30','graphic':1,'color': '#800080'},
    'I s':  {'label': 'Is', 'unit': ' [A]', 'address': 35, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_31','graphic':1,'color': '#9370DB'},
    'I t':  {'label': 'It', 'unit': ' [A]', 'address': 36, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_32','graphic':1,'color': '#4B0082'},
    
    'P_tot':  {'label': 'P', 'unit': ' [kW]',  'address': 43, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_33','graphic':2,'color': '#FF6347'},
    'Q_tot':  {'label': 'Q', 'unit': ' [kVAr]','address': 44, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_34','graphic':2,'color': '#FF69B4'},
    'S_tot':  {'label': 'S', 'unit': ' [kVA]', 'address': 45, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_35','graphic':2,'color': '#8B0000'},
    
}

# Diccionario 3 Supercondensador
data_dict_3 = {
    'Voltaje':  {'label': 'V',   'unit': ' [V]', 'address': 2, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_10'},
    'Corriente':{'label': 'I',   'unit': ' [A]', 'address': 3, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_11'},
    'Potencia': {'label': 'P',   'unit': ' [kW]','address': 4, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_12'},
    'SOC_1':      {'label': 'SOC', 'unit': ' [%]', 'address': 31,'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_17'},
    
    #Conexión DC
    'SOC':{'label': 'SOC', 'unit': ' [%]', 'address': 31,'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_61', 'graphic':3},
    'V':  {'label': 'V_DC', 'unit': ' [V]', 'address': 2, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_58','graphic':0,'color': '#FF0000'},
    'I':  {'label': 'I_DC', 'unit': ' [A]', 'address': 3, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_59','graphic':1,'color': '#FF0000'},
    'P1': {'label': 'P_DC',   'unit': ' [kW]','address': 4, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_60','graphic':1,'color': '#FF0000'},
    
    #Conexión AC
    'V r':  {'label': 'Vr', 'unit': ' [V]', 'address': 5, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_39','graphic':0,'color': '#ADD8E6'},
    'V s':  {'label': 'Vs', 'unit': ' [V]', 'address': 6, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_40','graphic':0,'color': '#4682B4'},
    'V t':  {'label': 'Vt', 'unit': ' [V]', 'address': 7, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_41','graphic':0,'color': '#00008B'},
    
    'I r':  {'label': 'Ir', 'unit': ' [A]', 'address': 11, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_42','graphic':1,'color': '#800080'},
    'I s':  {'label': 'Is', 'unit': ' [A]', 'address': 12, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_43','graphic':1,'color': '#9370DB'},
    'I t':  {'label': 'It', 'unit': ' [A]', 'address': 13, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_44','graphic':1,'color': '#4B0082'},
    
    'P':  {'label': 'P', 'unit': ' [kW]', 'address': 20, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_45','graphic':2,'color': '#FF6347'},
    'Q':  {'label': 'Q', 'unit': ' [kVAr]', 'address': 21, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_46','graphic':2,'color': '#FF69B4'},
    'S':  {'label': 'S', 'unit': ' [kVA]', 'address': 21, 'count': 1, 'factor':1/10, 'QLabel': 'lineEdit_47','graphic':2,'color': '#8B0000'},
}

# Diccionario de labels del eje y para cada gráfico
y_labels = {
    0: ' ',
    1: ' ',
    2: ' ',
    3: ' '
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

class MplSingleCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplSingleCanvas, self).__init__(fig)
        fig.tight_layout()

class LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(ruta_interfaz, self)
        self.resize(1000, 600)
        
        self.ui.label_2.setPixmap(QtGui.QPixmap(os.path.join(dir_interfaz, "esquema.png")))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Telecontrol y Telemando')
        
        self.devices_list = [val['ip'] if 'ip' in val else val['port'] for val in dic_equipment.values()]
        
        # Establecer la página predeterminada al arrancar
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_general)
        
        # acceder a las paginas
        self.ui.pushButton_gen.clicked.connect(lambda: self.change_page(self.ui.page_general, "Página general"))
        self.ui.pushButton_0.clicked.connect(lambda: self.change_page(self.ui.page_metodo_control, "Power Smoothing"))
        self.ui.pushButton_1.clicked.connect(lambda: self.change_page(self.ui.page_gr_fv, "Generación Fotovoltaica"))
        self.ui.pushButton_2.clicked.connect(lambda: self.change_page(self.ui.page_gr_bat, "Batería de Litio"))
        self.ui.pushButton_3.clicked.connect(lambda: self.change_page(self.ui.page_gr_sc, "Super Capacitores"))
        self.pushButton_14.clicked.connect(self.open_dialog_box)
        self.pushButton_set_pow.clicked.connect(self.start_loaded_data)
        self.pushButton_13.clicked.connect(self.set_end_pow)

        # menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        # estado inicial botones
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        
        # Inicializar el comboBox con los métodos de optimización
        self.ui.comboBox.addItems(['-----', 'RR Method', 'Exponential Method',])
        self.ui.comboBox.setCurrentIndex(2)  # Seleccionar 'Control 1' por defecto

        self.path_lb_6.setText('C:/Users/jorge/Documents/GitHub/Telecontrol_r/PowerSmoothing/ps_data/FV.txt')
        self.filename = 'C:/Users/jorge/Documents/GitHub/Telecontrol_r/PowerSmoothing/ps_data/FV.txt'
        self.load_data()
        
        # Conectar la señal de cambio de selección del comboBox a la función control
        self.ui.comboBox.currentIndexChanged.connect(self.control)
        
        # Configuraciones de visualización
        self.window_length = 50  # Establece la longitud de la ventana de visualización en milisegundos
        self.interval = 100  # Establece el intervalo de actualización del gráfico en milisegundos.
        
        # inicializar Variables
        self.P_pv = 0
        self.P_sc = 0
        self.P_res = 0
        self.SOC = 50
        # Variables control 1-----
        self.window_c1 = 3
        self.rampa_base = 0.001
        self.factor_dinamico = 0.05
        # Variables control 2-----
        self.alpha = 0.01
        self.P_pvc = 4.57
        self.data_array = []  # Inicializar el array para almacenar P_pv
        
        self.plot_list = []
        self.legends = []
        self.data_store = {}  # Inicializar el data_store
        self.data_array_widget_0 = []  # Inicializar el array para almacenar P_pv para la gráfica widget_0
        
        # Inicializar gráficos
        self.init_graphics()

        # Iniciar los hilos de lectura de los dispositivos
        self.threads = []
        self.init_modbus_threads()
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
        # Inicializar el gráfico de widget_0 como una sola gráfica
        widget_0 = self.ui.widget_0
        layout_0 = QVBoxLayout()
        canvas_0 = MplSingleCanvas(self, width=5, height=4, dpi=100)
        layout_0.addWidget(canvas_0)
        widget_0.setLayout(layout_0)
        self.graphs['widget_0'] = [canvas_0.axes]
 
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
    
    def init_modbus_threads(self):
        for equipment in dic_equipment.values():
            if equipment['Type'] == 'TCP/IP':
                thread = ModbusPlot(
                    equipment['ip'],
                    equipment['port'],
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
        # Actualizar el gráfico de widget_0
        if len(self.data_array_widget_0) > 0:
            self.update_widget_0_plot()

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
                label = f"{globals()[data_dict_name][key]['label']} {globals()[data_dict_name][key]['unit']}"
                axes_list[graphic_id].plot(value_to_plot, label=label, color=color)
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

    def update_widget_0_plot(self):
        axes = self.graphs['widget_0'][0]
        axes.clear()
        t = list(range(len(self.data_array_widget_0)))
        axes.plot(t, [val[0] for val in self.data_array_widget_0], label='P_pv')
        axes.plot(t, [val[1] for val in self.data_array_widget_0], label='P_sc')
        axes.plot(t, [val[2] for val in self.data_array_widget_0], label='P_res')
        axes.legend()
        axes.set_ylabel('Potencia [W]')
        axes.set_xlabel('Muestras')
        canvas = axes.figure.canvas
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
    
    def open_dialog_box(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Open File', dir_actual, 'All Files (*)')
        self.path_lb_6.setText(self.filename)
        self.load_data()
    
    def control(self):
        selected_control = self.ui.comboBox.currentText()
        self.path_lb_7.setText(selected_control)        
        
        if selected_control == 'RR Method':
            self.P_sc = control_rr(self.data_array, self.SOC, self.rampa_base)
            self.P_res = self.P_sc + self.P_pv
            print(f"RR Method, P_sc: {self.P_sc}")
        elif selected_control == 'Exponential Method':
            self.P_sc, self.P_pvc = control_e(self.data_array, self.SOC, self.alpha, self.P_pvc)
            self.P_res = self.P_sc + self.P_pv
            print(f"Exponential Method, P_sc: {self.P_sc}")
        elif selected_control == 'Control 2':
            print("Se ha seleccionado Control 2")
            self.P_sc = control1(self.data_array, self.SOC, self.window_c1, self.rampa_base, self.factor_dinamico)
        else:
            print("Seleccion no válida")
        
    def load_data(self):
        with open(self.filename, 'r') as file:
            # Lee todas las líneas y las almacena en una lista
            lines = file.readlines()
        
        # Convierte las líneas en valores flotantes y almacénalos en una lista
        values = [float(line.strip()) for line in lines]
        # self.values_list = values
        # self.values_list = values[164078:280234]
        self.values_list = values[164078:167078]
        
    def start_loaded_data(self):
        self.pow_index = 0
        # self.pow_timer.start(self.interval)  # Iniciar el temporizador Real Time
        self.pow_timer.start(1)  # Iniciar el temporizador para setear potencia cada 1 mili segundos
        
        resultados_path = os.path.join(dir_actual, 'ps_data')
        self.resultados_filename = get_unique_filename(resultados_path, 'resultados', 'txt')        
        print(f'archivo creado: {self.resultados_filename}')
        self.resultados = open(self.resultados_filename, 'w')
        self.resultados.write('{}\t{}\t{}\n'.format(
            'P_pv',
            'P_sc',
            'P_resultante'
        ))

    def set_pow(self, kpow):
        # try:
        #     print(f'kpow: {kpow}')
        # except Exception as e:
        #     print(f"Error setting pow: {e}")
        pass

    def set_next_pow(self):
        if self.pow_index < len(self.values_list):
            self.P_pv = self.values_list[self.pow_index]
            self.data_array.append(self.P_pv)  # Agregar el valor a data_array
            if len(self.data_array) > self.window_c1:  # Mantener el array con longitud igual a window_c1
                self.data_array.pop(0)
            self.control()
            self.data_array_widget_0.append((self.P_pv, self.P_sc, self.P_res))  # Agregar valores a data_array_widget_0
            if len(self.data_array_widget_0) > self.window_length:  # Mantener el array con longitud igual a window_length
                self.data_array_widget_0.pop(0)    
            self.resultados.write('{}\t{}\t{}\n'.format(
                self.P_pv,
                self.P_sc,
                self.P_res
            ))
            self.set_pow(self.values_list[self.pow_index])
            print(f'setting pow [{self.pow_index}]: {self.values_list[self.pow_index]}')
            self.pow_index += 1
        else:
            self.pow_timer.stop()
            print('Fin lista')
            self.resultados.close()
            
    def set_end_pow(self):
        self.pow_index = len(self.values_list) + 1
        print('Stop')
            
    def close_instruments(self, event):
        for thread in self.threads:
            if isinstance(thread, ModbusPlot):
                thread.client.close()
            elif isinstance(thread, SerialPlot):
                thread.ser.close()
        event.accept()

    def change_page(self, page, page_name):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.lineEdit_6.setText(page_name)

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

class ModbusPlot(QtCore.QThread):
    new_data = QtCore.pyqtSignal(dict, str)

    def __init__(self, ip, port, timeout, data_dict, widget_id):
        super().__init__()
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.data_dict = data_dict
        self.widget_id = widget_id
        self.client = ModbusTcpClient(ip, port=port, timeout=timeout)
        self.data_buffer = {key: [] for key in data_dict.keys()}

    def run(self):
        self.client.connect()
        while True:
            try:
                for key, settings in self.data_dict.items():
                    response = self.client.read_holding_registers(settings['address'], settings['count'], unit=1)
                    if response.isError():
                        continue
                    value = struct.unpack('<h', struct.pack('<H', response.registers[0]))[0] * settings['factor']
                    self.data_buffer[key].append(value)
                self.new_data.emit(self.data_buffer, self.widget_id)
                time.sleep(1)
            except Exception as e:
                print(f"Error reading Modbus data: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LIVE_PLOT_APP()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()