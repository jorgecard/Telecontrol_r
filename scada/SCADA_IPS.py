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
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QAudioDeviceInfo, QAudio, QCameraInfo
import os
from pass1 import *

# Variables
dic_equipment = {
    'Inversor': {'Name': 'Inversor', 'ip': '192.168.222.136', 'port': 502, 'timeout': 3,
                 'page': 2, 'data_dict': 'data_dict_2', 'comand': 'read_input_registers', 'pack_method': 'method_2'},
    'Sentrum': {'Name': 'Sentrum', 'ip': '192.168.222.222', 'port': 502, 'timeout': 3,
                'page': 1, 'data_dict': 'data_dict_1', 'comand': 'read_holding_registers', 'pack_method': 'method_1'},
}

# Definir un diccionario para almacenar los datos
# Diccionario para las variables del equipo 1: 'Sentrum'
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
# Diccionario para las variables del equipo 2: 'Inversor'
data_dict_2 = {
    'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic': 0, 'factor': 1},
    'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]', 'graphic': 1, 'factor': 0.1},
    'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]', 'graphic': 2, 'factor': 1},
    'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]', 'graphic': 3, 'factor': 0.01},
    # 'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]', 'graphic': 4, 'factor': 0.01},
    # 'Energía Neta': {'offset': 33, 'reg': 1, 'color': '-w', 'label': 'Energía Neta', 'unit': ' [kWh]', 'graphic': 5, 'factor': 1},
    'Frecuencia': {'offset': 23, 'reg': 1, 'label': 'Frecuencia', 'unit': ' [Hz]', 'factor': 1},
}
data_dict_2 = {
    'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic': 0, 'factor': 1 / 3.4},
    'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]', 'graphic': 0, 'factor': 0.1},
    'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]', 'graphic': 1, 'factor': 1},
    'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]', 'graphic': 2, 'factor': 0.01},
    'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]', 'graphic': 3, 'factor': 0.01},
    'Energía Neta': {'offset': 33, 'reg': 1, 'label': 'Energía Neta', 'unit': ' [kWh]', 'factor': 1},
    # 'Frecuencia': {'offset': 23, 'reg': 1, 'color': '-w', 'label': 'Frecuencia', 'unit': ' [Hz]', 'graphic': 5, 'factor': 1},
}

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = dir_actual + r"\QtScada"
nombre_interfaz = "SCADA.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_logo = "nano.png"
ruta_logo = os.path.join(dir_interfaz, nombre_logo)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        fig, self.axes = plt.subplots(2, 2, figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()

class PyShine_LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi(ruta_interfaz, self)
        self.resize(888, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Telecontrol y Telemando')
        self.threadpool = QtCore.QThreadPool()
        self.data_threadpool = QtCore.QThreadPool()
        
        self.devices_list = []
        for i, (key, val) in enumerate(dic_equipment.items()):
            self.devices_list.append(val['ip'])
        
        # Establecer la página predeterminada al arrancar
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        #acceder a las paginas
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_login))			
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ampere))
        self.pushButton_2.clicked.connect(self.activate_sheet_2)
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_sentron))
        self.pushButton_3.clicked.connect(self.activate_sheet_3)
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_registros))
        self.pushButton_5.clicked.connect(self.activate_sheet_4)
        # cambio de device
        self.ui.pushButton_2.clicked.connect(lambda: self.update_now(self.devices_list[0]))
        self.ui.pushButton_3.clicked.connect(lambda: self.update_now(self.devices_list[1]))
        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        # estado inicial botones
        # self.pushButton_2.setEnabled(False)
        # self.pushButton_3.setEnabled(False)
        # self.pushButton_5.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_4.clicked.connect(self.toggle_password_visibility)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        # self.ui.widget.addWidget(self.canvas, 2, 1, 1, 1)
        # layout = QVBoxLayout(self.widget)
        # layout.addWidget(self.canvas)
        # self.widget.setLayout(layout)
        self.reference_plots = {i: {} for i in range(4)}
        self.q = queue.Queue(maxsize=20)

        self.device = self.devices_list[0]
        print(self.device)
        self.selected_dict = self.getDic()
        self.window_length = 1000  # Establece la longitud de la ventana de visualización en milisegundos
        self.downsample = 1  # Establece el factor de submuestreo. Un valor de 1 significa que no se realizará submuestreo.
        # self.channels = [1, 2]  # Establece los canales de audio ([1] mono)
        self.interval = 100  # Establece el intervalo de actualización del gráfico en milisegundos.

        self.samplerate = 20  # tasa de muestreo a 20 Hz (estándar)
        length = int(self.window_length * self.samplerate / (1000 * self.downsample))  # Cantidad de muestras

        # MATRIZ que almacena los datos
        self.plotdata = np.zeros((length, len(self.selected_dict)))

        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)  # msec
        self.timer.timeout.connect(self.update_plot)
        # self.timer.timeout.connect(self.getData)
        self.timer.start()

        # Configurar el timer para getData
        self.data_timer = QtCore.QTimer()
        # self.data_timer.setInterval(1/self.samplerate)  # Establece el intervalo de actualización de datos en milisegundos
        self.data_timer.setInterval(200)
        self.data_timer.timeout.connect(self.getData)

        # self.lineEdit.textChanged['QString'].connect(self.update_window_length)
        # self.lineEdit_2.textChanged['QString'].connect(self.update_sample_rate)
        # self.lineEdit_3.textChanged['QString'].connect(self.update_down_sample)
        # self.lineEdit_4.textChanged['QString'].connect(self.update_interval)
        self.pushButton_2.clicked.connect(self.start_worker)
        self.pushButton_2.clicked.connect(self.start_data_worker)
        self.pushButton_3.clicked.connect(self.start_worker)
        self.pushButton_3.clicked.connect(self.start_data_worker)
        self.bt_log_in.clicked.connect(self.log_in)

    def getData(self):
        try:
            # Conexión al cliente Modbus TCP (por defecto el primer dispositivo del diccionario)
            client = ModbusTcpClient(self.device, port=502, timeout=3)
            client.connect()
            
            # Conexión al servidor Modbus TCP
            if not client.connect():
                print("Error: No se pudo conectar al dispositivo Modbus TCP:", self.device)
                return

            # Inicializar una lista para almacenar los valores
            values = []

            # Leer los registros de retención
            for key, val in self.selected_dict.items():
                offset = val['offset']
                count = val['reg']
                
                # Obtener el método de lectura correcto del cliente Modbus
                read_method = getattr(client, self.command_name)

                # Leer los registros de retención para la variable actual
                raw_values = read_method(address=offset, count=count, unit=1)
                if self.pack_method == 'method_1':
                    packed_value = struct.pack('>I', (raw_values.registers[0] << 16) | raw_values.registers[1])
                    value = struct.unpack('!f', packed_value)[0]
                elif self.pack_method == 'method_2':
                    packed_value = struct.unpack('<h', struct.pack('<H', raw_values.registers[0]))[0]
                    value = packed_value

                value = round(float(value),2)
                value = value * val['factor']
                value = round(float(value),2)
                # print(value)
                # Agregar el valor a la lista
                values.append(value)

            # Envío de los datos a la cola
            self.q.put(tuple(values))
            
            # # Lectura de los registros de retención
            # raw_values_1 = client.read_holding_registers(address=1, count=2, unit=1)
            # raw_values_3 = client.read_holding_registers(address=3, count=2, unit=1)
            # packed_value_1 = struct.pack('>I', (raw_values_1.registers[0] << 16) | raw_values_1.registers[1])
            # value_1 = struct.unpack('!f', packed_value_1)[0]
            # packed_value_3 = struct.pack('>I', (raw_values_3.registers[0] << 16) | raw_values_3.registers[1])
            # value_3 = struct.unpack('!f', packed_value_3)[0]

            # # Envío de los datos a la cola
            # self.q.put((value_1, value_3))
            # print(f'value_1: {value_1} - value_3: {value_3}')

            # print(value)
            
            # Cierre de la conexión con el cliente Modbus TCP
            # client.close()
        except Exception as e:
            print("ERROR: ", e)

    def start_worker(self):
        # self.data_timer.start()  # Inicia el timer para getData
        worker = Worker(self.start_stream, )
        self.threadpool.start(worker)
    
    def start_data_worker(self):
        self.data_timer.start()  # Inicia el timer para getData
        worker2 = Worker(self.start_data_stream, )
        self.data_threadpool.start(worker2)

    def start_stream(self):
        # self.lineEdit.setEnabled(False)
        # self.lineEdit_2.setEnabled(False)
        # self.lineEdit_3.setEnabled(False)
        # self.lineEdit_4.setEnabled(False)
        # self.comboBox.setEnabled(False)
        self.pushButton.setEnabled(True)
        # self.getData()
        
    def start_data_stream(self):
        self.getData()
    
    def getDic(self):
        self.commmand_name = None
        for key, val in dic_equipment.items():
            if val['ip'] == self.device:
                self.selected_dict = globals()[val['data_dict']]
                # print(self.selected_dict)
                self.command_name = val['comand']
                self.pack_method = val['pack_method']
                break
        if self.selected_dict is None:
            raise ValueError("No se encontró el diccionario de datos para el dispositivo seleccionado")
        return self.selected_dict
    
    def update_now(self, value):
        # print(value)
        # self.device = self.devices_list.index(value)
        self.device = value
        self.selected_dict = self.getDic()
        print(self.device)
        # print(self.selected_dict)
        
        length = int(self.window_length * self.samplerate / (1000 * self.downsample))
        self.plotdata = np.zeros((length, len(self.selected_dict)))
        self.reference_plots = {i: {} for i in range(4)}
        # self.update_plot()
        # print('Device:', self.devices_list.index(value))
        #Limiar gráfica
        for graphic in range(4):
            ax = self.canvas.axes[graphic // 2, graphic % 2]
            ax.cla()
            # ax.grid(True, linestyle='--')
            # ax.legend(loc='upper right')
        # self.canvas.draw()

    def update_window_length(self, value):
        self.window_length = int(value)
        length = int(self.window_length * self.samplerate / (1000 * self.downsample))
        # self.selected_dict = self.getDic()
        self.plotdata = np.zeros((length, len(self.selected_dict)))
        self.update_plot()

    def update_sample_rate(self, value):
        self.samplerate = int(value)
        length = int(self.window_length * self.samplerate / (1000 * self.downsample))
        # self.selected_dict = self.getDic()
        self.plotdata = np.zeros((length, len(self.selected_dict)))
        self.update_plot()

    def update_down_sample(self, value):
        self.downsample = int(value)
        length = int(self.window_length * self.samplerate / (1000 * self.downsample))
        # self.selected_dict = self.getDic()
        self.plotdata = np.zeros((length, len(self.selected_dict)))
        self.update_plot()

    def update_interval(self, value):
        self.interval = int(value)
        self.timer.setInterval(self.interval)  # msec
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        try:
            # self.selected_dict = self.getDic()
            data = np.zeros((1, len(self.selected_dict)))
            
            try:
                data_tuple = self.q.get_nowait()  # Obtener la tupla de la cola
            except queue.Empty:
                return
            data_list = [float(value) for value in data_tuple]
            data = np.array(data_list).reshape(1, len(self.selected_dict))
            # print(data)
            # print(self.selected_dict)
            
            shift = len(data)
            self.plotdata = np.roll(self.plotdata, -shift, axis=0)
            self.plotdata[-shift:, :] = data
            self.ydata = self.plotdata[:]
            
            if not any(self.reference_plots.values()):
                for i, (key, val) in enumerate(self.selected_dict.items()):
                    if 'graphic' in val:
                        graphic = val['graphic']
                        color = val['color']
                        self.reference_plots[graphic][key] = self.canvas.axes[graphic // 2, graphic % 2].plot(
                            self.ydata[:, i], color=color, label=val['label'])[0]
            else:
                for i, (key, val) in enumerate(self.selected_dict.items()):
                    if 'graphic' in val:
                        graphic = val['graphic']
                        self.reference_plots[graphic][key].set_ydata(self.ydata[:, i])

            for graphic in range(4):
                ax = self.canvas.axes[graphic // 2, graphic % 2]
                ax.yaxis.grid(True, linestyle='--')
                
                if graphic == 0:
                    ax.set_ylim(ymin=0, ymax=301)
                    start, end = ax.get_ylim()
                    ax.yaxis.set_ticks(np.arange(start, end, 40))
                elif graphic == 1:
                    ax.set_ylim(ymin=0, ymax=5.1)
                    start, end = ax.get_ylim()
                    ax.yaxis.set_ticks(np.arange(start, end, 1))
                elif graphic == 2:
                    ax.set_ylim(ymin=0, ymax=301)
                    start, end = ax.get_ylim()
                    ax.yaxis.set_ticks(np.arange(start, end, 40))
                elif graphic == 3:
                    ax.set_ylim(ymin=0, ymax=8.1)
                    start, end = ax.get_ylim()
                    ax.yaxis.set_ticks(np.arange(start, end, 1))
                    
                ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
                ax.legend(loc='upper right')
            
            self.canvas.draw()
            
            # no graph
            for i, (key, val) in enumerate(self.selected_dict.items()):
                    if 'graphic' not in val:
                        self.varn1_2.setText(str(data_tuple[i]))
                        
        except Exception as e:
            print("Error en la actualización de la gráfica:", e)
            pass

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
        self.message_lg.setText(self.message)
        if (self.message == 'JerarquiaA'):
            # Borro de pantalla
            self.username.setText('')
            self.password.setText('')
            # estado inicial botones
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_5.setEnabled(True)
        elif (self.message == 'JerarquiaB'):
            # Borro de pantalla
            self.username.setText('')
            self.password.setText('')
            # estado inicial botones
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            
    def activate_sheet_2(self):
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)
        self.widget.setLayout(layout)
    def activate_sheet_3(self):
        layout = QVBoxLayout(self.widget_2)
        layout.addWidget(self.canvas)
        self.widget_2.setLayout(layout)
    def activate_sheet_4(self):
        # self.lineEdit.setText('')
        self.txt = readtxt()
        self.lineEdit.setText(self.txt)
        
    def toggle_password_visibility(self):
        if self.password.echoMode() == QtWidgets.QLineEdit.Password:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
# www.pyshine.com
class Worker(QtCore.QRunnable):
    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.function(*self.args, **self.kwargs)

app = QtWidgets.QApplication(sys.argv)
mainWindow = PyShine_LIVE_PLOT_APP()
mainWindow.show()
sys.exit(app.exec_())
