# https://www.youtube.com/watch?v=Ng00Mj5Tt8o&t=934s

import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import queue
import numpy as np
import struct  # Para decodificar los datos
from pymodbus.client.sync import ModbusTcpClient  # Para la conexión
import time
import sounddevice as sd
import pdb
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtMultimedia import QAudioDeviceInfo,QAudio,QCameraInfo
import os
input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)

# # Borrar esta parte después
# ip = '192.168.222.136' # Coloca la dirección IP de tu multímetro
# client = ModbusTcpClient(ip, port=502, timeout=3)
# client.connect()

# Variables
dic_equipment = {
  'Sentrum': {'Name': 'Sentrum', 'ip': '192.168.222.222', 'page': 1, 'data_dict' : 'data_dict_1'},
  'Inversor': {'Name': 'Inversor', 'ip': '192.168.222.180', 'page': 2, 'data_dict' : 'data_dict_2'},
}

# Definir un diccionario para almacenar los datos
# Diccionario para las variables del equipo 1: 'Sentrum'
data_dict_1 = {
  'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic':1, 'factor':1/3.4},
  'Voltaje DC2': {'offset': 13, 'reg': 1, 'color': '#FF5733', 'label': 'Voltaje DC2', 'unit': ' [V]','graphic':1, 'factor':1},
}

# Diccionario para las variables del equipo 2: 'Inversor'
data_dict_2 = {
  'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic':1, 'factor':1/3.4},
  'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]','graphic':1,'factor':0.1},
  'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]','graphic':2,'factor':1},
  'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]','graphic':3,'factor':0.01},
  'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]','graphic':4,'factor':0.01},
  'Energía Neta': {'offset': 33, 'reg': 1, 'color': '-w', 'label': 'Energía Neta', 'unit': ' [kWh]','graphic':5,'factor':1},
  'Frecuencia': {'offset': 23, 'reg': 1, 'color': '-w', 'label': 'Frecuencia', 'unit': ' [Hz]','graphic':5,'factor':1},
}


dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = dir_actual + r"\QtScada"
nombre_interfaz = "scada0.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_logo = "nano.png"
ruta_logo = os.path.join(dir_interfaz, nombre_logo)

class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()

class PyShine_LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi(ruta_interfaz,self)
        self.resize(888, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Telecontrol y Telemando')
        self.threadpool = QtCore.QThreadPool()	
        self.devices_list= []
        
        for i, (key, val) in enumerate(dic_equipment.items()):
            self.devices_list.append(val['ip'])

        self.comboBox.addItems(self.devices_list)
        self.comboBox.currentIndexChanged['QString'].connect(self.update_now)
        self.comboBox.setCurrentIndex(0)
        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.gridLayout_4.addWidget(self.canvas, 2, 1, 1, 1)
        self.reference_plots = {}
        self.q = queue.Queue(maxsize=20)

        self.device = self.devices_list[0]
        self.window_length = 1000        # Establece la longitud de la ventana de visualización en milisegundos
        self.downsample = 1              # Establece el factor de submuestreo. Un valor de 1 significa que no se realizará submuestreo.
        self.channels = [1,2]              # Establece los canales de audio ([1] mono)
        # self.channels = [1]
        self.interval = 100               # Establece el intervalo de actualización del gráfico en milisegundos.
        
        # device_info =  sd.query_devices(self.device, 'input')
        # self.samplerate = device_info['default_samplerate']

        self.samplerate = 20         # tasa de muestreo a 44100 Hz (estándar)
        length  = int(self.window_length*self.samplerate/(1000*self.downsample))   # Cantidad de muestras
        sd.default.samplerate = self.samplerate
        
        # MATRIZ que almacena los datos de audio
        self.plotdata =  np.zeros((length,len(self.channels)))
        
        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval) #msec
        self.timer.timeout.connect(self.update_plot)
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
        
        
    # def getAudio(self):
    #     try:
    #         def audio_callback(indata,frames,time,status):
    #             self.q.put(indata[::self.downsample,[0]])
    #         stream  = sd.InputStream( device = self.device, channels = max(self.channels), samplerate =self.samplerate, callback  = audio_callback)
    #         with stream:
    #             input()
    #     except Exception as e:
    #         print("ERROR: ",e)
            
    def getData(self):
        try:
            # Conexión al cliente Modbus TCP (por defecto el primer dispositivo del diccionario)
            # ip_address = self.devices_list[0]
            client = ModbusTcpClient(self.device, port=502, timeout=3)
            client.connect()

            # Conexión al servidor Modbus TCP
            if not client.connect():
                print("Error: No se pudo conectar al dispositivo Modbus TCP:", self.device)
                return

            # Lectura de los registros de retención
            raw_values = client.read_holding_registers(address=15, count=2, unit=1)

            # Decodificación de los datos y emisión a la cola
            packed_value = struct.pack('>I', (raw_values.registers[0] << 16) | raw_values.registers[1])
            value = struct.unpack('!f', packed_value)[0]

            # Envío de los datos a la cola
            self.q.put(value)
            print(value)

            # Cierre de la conexión con el cliente Modbus TCP
            client.close()
        
        # try:
        #     # Conexión al servidor Modbus TCP
        #     if not client.connect():
        #         print("Error: No se pudo conectar al dispositivo Modbus TCP")
        #         return
        #     def dato_callback():
        #         raw_values = client.read_holding_registers(address=15, count=2, unit=1)
        #         packed_value = struct.pack('>I', (raw_values.registers[0] << 16) | raw_values.registers[1])
        #         value = struct.unpack('!f', packed_value)[0]
        #         print(value)
        #         self.q.put(value)
        #     dato_callback()
            
        except Exception as e:
            print("ERROR: ",e)

    def start_worker(self):
        worker = Worker(self.start_stream, )
        self.threadpool.start(worker)	

    def start_stream(self):
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.pushButton.setEnabled(False)
        # self.getAudio()
        self.getData()
        
    def update_now(self,value):
        print(value)
        self.device = self.devices_list.index(value)
        print('Device:',self.devices_list.index(value))

    def update_window_length(self,value):
        self.window_length = int(value)
        length  = int(self.window_length*self.samplerate/(1000*self.downsample))
        self.plotdata =  np.zeros((length,len(self.channels)))
        self.update_plot()

    def update_sample_rate(self,value):
        self.samplerate = int(value)
        sd.default.samplerate = self.samplerate
        length  = int(self.window_length*self.samplerate/(1000*self.downsample))
        self.plotdata =  np.zeros((length,len(self.channels)))
        self.update_plot()

    def update_down_sample(self,value):
        self.downsample = int(value)
        length  = int(self.window_length*self.samplerate/(1000*self.downsample))
        self.plotdata =  np.zeros((length,len(self.channels)))
        self.update_plot()

    def update_interval(self,value):
        self.interval = int(value)
        self.timer.setInterval(self.interval) #msec
        self.timer.timeout.connect(self.update_plot)
        # self.timer.timeout.connect(self.getData)
        self.timer.start()

    def update_plot(self):
        try:
            data=np.zeros((1,len(self.channels)))
            # print(data.shape)
            
            while True:
                try: 
                    data = self.q.get_nowait()
                    # print('data:')
                    # print(data)
                except queue.Empty:
                    break
                data = np.hstack((data, data + 0.3))
                shift = len(data)
                self.plotdata = np.roll(self.plotdata, -shift,axis = 0)
                self.plotdata[-shift:, :] = data
                
                self.ydata = self.plotdata[:]
                
                if not self.reference_plots:
                    for i, (key, val) in enumerate(data_dict_1.items()):
                        color = val['color']
                        self.reference_plots[key] = self.canvas.axes.plot(self.ydata[:, i], color=color, label=val['label'])[0]
                else:
                    for i, (key, val) in enumerate(data_dict_1.items()):
                        self.reference_plots[key].set_ydata(self.ydata[:, i])
            
            self.canvas.axes.yaxis.grid(True,linestyle='--')
            start, end = self.canvas.axes.get_ylim()
            self.canvas.axes.yaxis.set_ticks(np.arange(start, end, 0.1))
            self.canvas.axes.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
            self.canvas.axes.set_ylim( ymin=-0.5, ymax=1)
            self.canvas.axes.legend(loc='upper right')
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