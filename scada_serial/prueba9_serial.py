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
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtMultimedia import QAudioDeviceInfo, QAudio, QCameraInfo
import os

# Variables
dic_equipment = {
    'ESP-32': {'Name': 'ESP-32', 'Manufacturer': 'Silicon Labs', 'baudrate':115200,
                'ip': '192.168.222.222', 'port': 502, 'timeout':3,
                'page': 1, 'data_dict': 'data_dict_1', 'comand': 'read_holding_registers'},
    'Arduino nano': {'Name': 'Arduino nano', 'Manufacturer': 'wch.cn', 'baudrate':9600,
                 'ip': '192.168.222.180', 'port': 502, 'timeout':3,
                 'page': 2, 'data_dict': 'data_dict_2', 'comand': 'read_input_registers'},
}

# Definir un diccionario para almacenar los datos
# Diccionario para las variables del equipo 1: 'Sentrum'

data_dict_1 = {
  'Tensión L1-N': {'offset': 1, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L1-N', 'unit': ' [V]', 'graphic':0, 'factor':39},
  'Tensión L2-N': {'offset': 3, 'reg': 2, 'color': '#9103A6', 'label': 'Tension L2-N', 'unit': ' [V]','graphic':0, 'factor':38},
  'Tensión L3-N': {'offset': 5, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L3-N', 'unit': ' [V]','graphic':0,'factor':37},
  'I-L1': {'offset': 13, 'reg': 2, 'color': '#DF8905', 'label': 'I-L1', 'unit': ' [A]','graphic':1,'factor':1},
  'I-L2': {'offset': 15, 'reg': 2, 'color': '#DF8905', 'label': 'I-L2', 'unit': ' [A]','graphic':1,'factor':1.1},
  'I-L3': {'offset': 17, 'reg': 2, 'color': '#DF8905', 'label': 'I-L3', 'unit': ' [A]','graphic':1,'factor':1.3},
  'E-S': {'offset': 63, 'reg': 2, 'color': '#54548D', 'label': 'E-S', 'unit': ' [VA]','graphic':2,'factor':72},
  'E-P': {'offset': 65, 'reg': 2, 'color': '#558D54', 'label': 'E-P', 'unit': ' [W]','graphic':2,'factor':70},
  'E-Q': {'offset': 63, 'reg': 2, 'color': '#547E8D', 'label': 'E-Q', 'unit': ' [VAR]','graphic':2,'factor':71},
  'THD-V1': {'offset': 261, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': ' [%]','graphic':3,'factor':2.12},
#   'THD-V2': {'offset': 263, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V2', 'unit': ' [%]','graphic':4,'factor':2.14},
#   'THD-V3': {'offset': 265, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V3', 'unit': ' [%]','graphic':4,'factor':2.15},
  'Energía Aparente': {'offset': 2817, 'reg': 2, 'label': 'Energía Aparente', 'unit': ' [kVAh]','factor':1}
}
# Diccionario para las variables del equipo 2: 'Inversor'
data_dict_2 = {
    'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic': 0, 'factor': 1 / 3.4},
    'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]', 'graphic': 1, 'factor': 0.1},
    'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]', 'graphic': 2, 'factor': 1},
    'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]', 'graphic': 3, 'factor': 0.01},
    # 'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]', 'graphic': 4, 'factor': 0.01},
    # 'Energía Neta': {'offset': 33, 'reg': 1, 'color': '-w', 'label': 'Energía Neta', 'unit': ' [kWh]', 'graphic': 5, 'factor': 1},
    # 'Frecuencia': {'offset': 23, 'reg': 1, 'color': '-w', 'label': 'Frecuencia', 'unit': ' [Hz]', 'graphic': 5, 'factor': 1},
}

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = dir_actual + r"\QtScada"
nombre_interfaz = "scada0.ui"
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
        
        self.update_dic()
        self.devices_list = []
        for i, (key, val) in enumerate(dic_equipment.items()):
            self.devices_list.append(val['Name'])
        
        self.comboBox.addItems(self.devices_list)
        self.comboBox.currentIndexChanged['QString'].connect(self.update_now)
        self.comboBox.setCurrentIndex(0)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.gridLayout_4.addWidget(self.canvas, 2, 1, 1, 1)
        # self.reference_plots = {}
        self.reference_plots = {i: {} for i in range(4)}
        self.q = queue.Queue(maxsize=20)

        # self.device = self.devices_list[0]
        self.device = self.get_port(0)
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
        self.data_timer.setInterval(1/self.samplerate)  # Establece el intervalo de actualización de datos en milisegundos
        self.data_timer.timeout.connect(self.getData)

        self.lineEdit.textChanged['QString'].connect(self.update_window_length)
        self.lineEdit_2.textChanged['QString'].connect(self.update_sample_rate)
        self.lineEdit_3.textChanged['QString'].connect(self.update_down_sample)
        self.lineEdit_4.textChanged['QString'].connect(self.update_interval)
        self.pushButton.clicked.connect(self.start_worker)
        self.pushButton.clicked.connect(self.start_data_worker)

    def getData(self):
        try:
            values = []
            for key, val in self.selected_dict.items():
                value = self.ser.readline().decode('ascii', errors='ignore').strip()
                value = round(float(value),2)
                value = value * val['factor']
                value = round(float(value),2)
                # Agregar el valor a la lista
                values.append(value)

            # Envío de los datos a la cola
            self.q.put(tuple(values))
            # print(values)
        except Exception as e:
            print("ERROR: ", e)

    def start_worker(self):
        self.conf_serial()
        worker = Worker(self.start_stream, )
        self.threadpool.start(worker)
    
    def start_data_worker(self):
        self.data_timer.start()  # Inicia el timer para getData
        worker2 = Worker(self.start_data_stream, )
        self.data_threadpool.start(worker2)

    def start_stream(self):
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.pushButton.setEnabled(False)
        
    def start_data_stream(self):
        self.getData()

    def update_dic(self):
        puertos = serial.tools.list_ports.comports()
        puertos_disponibles = []
        for puerto in puertos:
            info_puerto = {
            'device': puerto.device,
            'manufacturer': puerto.manufacturer,
            }
            puertos_disponibles.append(info_puerto)
        for equipo in dic_equipment.values():
            for puerto in puertos_disponibles:
                if equipo['Manufacturer'] == puerto['manufacturer']:
                    equipo['port'] = puerto['device']
                    break
    
    def getDic(self):
        for key, val in dic_equipment.items():
            if val['port'] == self.device:
                self.selected_dict = globals()[val['data_dict']]
                # print(self.selected_dict)
                break
        if self.selected_dict is None:
            raise ValueError("No se encontró el diccionario de datos para el dispositivo seleccionado")
        return self.selected_dict
    
    def get_port(self, index):
        keys = list(dic_equipment.keys())
        key = keys[index]
        return dic_equipment[key]['port']
    
    def conf_serial(self):
        for key, val in dic_equipment.items():
            if val['port'] == self.device:
                self.ser = serial.Serial(
                    port=self.device,         # Puerto serial
                    baudrate=val['baudrate'],       # Velocidad en baudios
                    timeout=1            # Tiempo de espera para la lectura
                )
    
    def update_now(self, value):
        # print(value)
        # self.device = self.devices_list.index(value)
        # self.device = value
        self.device = self.get_port(self.devices_list.index(value))
        self.selected_dict = self.getDic()
        print(self.device)
        
        length = int(self.window_length * self.samplerate / (1000 * self.downsample))
        self.plotdata = np.zeros((length, len(self.selected_dict)))
        self.reference_plots = {i: {} for i in range(4)}
        # self.update_plot()
        # print('Device:', self.devices_list.index(value))

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
            print("Data:", data)
            print(len(self.selected_dict))
            
            shift = len(data)
            self.plotdata = np.roll(self.plotdata, -shift, axis=0)
            self.plotdata[-shift:, :] = data
            self.ydata = self.plotdata[:]
            
            if not any(self.reference_plots.values()):
                for i, (key, val) in enumerate(self.selected_dict.items()):
                    if 'graphic' in val:
                        graphic = val['graphic']
                        print(f"Setting up plot for graphic {graphic} with key {key}")
                        color = val['color']
                        self.reference_plots[graphic][key] = self.canvas.axes[graphic // 2, graphic % 2].plot(
                            self.ydata[:, i], color=color, label=val['label'])[0]
            else:
                for i, (key, val) in enumerate(self.selected_dict.items()):
                    if 'graphic' in val:
                        graphic = val['graphic']
                        print(f"Updating plot for graphic {graphic} with key {key}")
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
        except Exception as e:
            print("Error en la actualización de la gráfica:", e)
            pass

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
