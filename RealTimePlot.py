import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from tkinter import *
from threading import Thread
import sys

import struct # Para decodificar los datos
from pymodbus.client.sync import ModbusTcpClient # Para la conexión

import time

# Realizar la conexión
ip = '192.168.0.76' # Coloca la dirección IP de tu multímetro
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

# Definir un diccionario para almacenar los datos
data_dict = {
  'Tensión L1-N': {'offset': 1, 'reg': 2, 'color': 'b-', 'label': 'Tensión L1-N', 'unit': '[V]'},
  'Tensión L2-N': {'offset': 3, 'reg': 2, 'color': 'b-', 'label': 'Tension L2-N', 'unit': '[V]'},
  'Tensión L3-N': {'offset': 5, 'reg': 2, 'color': 'b-', 'label': 'Tensión L3-N', 'unit': '[V]'},
  'Tensión L1-L2': {'offset': 7, 'reg': 2, 'color': 'b-', 'label': 'Tensión L1-L2', 'unit': '[V]'},
  'Tensión L2-L3': {'offset': 9, 'reg': 2, 'color': 'b-', 'label': 'Tensión L2-L3', 'unit': '[V]'},
  'Tensión L3-L1': {'offset': 11, 'reg': 2, 'color': 'b-', 'label': 'Tensión L3-L1', 'unit': '[V]'},
  'I-L1': {'offset': 13, 'reg': 2, 'color': '#ADD8E6', 'label': 'I-L1', 'unit': '[A]'},
  'I-L2': {'offset': 15, 'reg': 2, 'color': '#ADD8E6', 'label': 'I-L2', 'unit': '[A]'},
  'I-L3': {'offset': 17, 'reg': 2, 'color': '#ADD8E6', 'label': 'I-L3', 'unit': '[A]'},
  'E-S': {'offset': 63, 'reg': 2, 'color': '#ADD8E6', 'label': 'E-S', 'unit': '[kVA]'},
  'E-P': {'offset': 65, 'reg': 2, 'color': '#ADD8E6', 'label': 'E-P', 'unit': '[kW]'},
  'E-Q': {'offset': 63, 'reg': 2, 'color': '#ADD8E6', 'label': 'E-Q', 'unit': '[kVAR]'},
  'THD-V1': {'offset': 261, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': '[%]'},
  'THD-V2': {'offset': 263, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V2', 'unit': '[%]'},
  'THD-V3': {'offset': 265, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V3', 'unit': '[%]'},
  'THD-I1': {'offset': 267, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-I1', 'unit': '[%]'},
  'THD-I2': {'offset': 269, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-I2', 'unit': '[%]'},
  'THD-I3': {'offset': 271, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-I3', 'unit': '[%]'},
  'Energía Aparente': {'offset': 849, 'reg': 4, 'color': '#ADD8E6', 'label': 'Energía Aparente', 'unit': '[kVAh]'}
}

def getData():
  time.sleep(1)
  while (isRun):
    global isReceiving
    global value
    for key, val in data_dict.items():
      raw_value = client.read_holding_registers(address=val['offset'], count=val['reg'], unit = 1)
      packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1])
      value[key] = round(struct.unpack('!f', packed_value)[0], 2)
    isReceiving = True

def onClosing():
  global isRun
  isRun = False
  thread.join()
  root.quit()
  root.destroy()

def plotData(self, lines, lineValueText, lineLabel):
  for key, val in data_dict.items():
    data[key].append(value[key])
    lines[key].set_data(range(Samples), data[key])
    lineValueText[key].set_text(val['label'] +' = '+ str(value[key]) + val['unit'])

# Plot Parameters -----------------
Samples = 100
sampleTime = 100  #Tiempo de muestreo / Sample Time
value = {}
data = {}
isReceiving = False
isRun = True

for key, val in data_dict.items():
  data[key] = collections.deque([0]*Samples, maxlen=Samples)
  value[key] = 0

# Limites de los ejes / Axis limit
xmin = 0
xmax = Samples
ymin = 0
ymax = 260

# Crear grafica -------------------------------------------------------
fig = plt.figure(facecolor='0.94')
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
plt.title('Monitoreo en tiempo real')
plt.grid()
ax.set_xlabel('Muestras')
ax.set_ylabel('Magnitud')

lines = {}
lineValueText = {}

for i, (key, val) in enumerate(data_dict.items()):
    lines[key], = ax.plot([], [], val['color'], label=val['label'])
    lineValueText[key] = ax.text(0.65, 0.90 - i * 0.05, '', transform=ax.transAxes)

########## Recibir datos en segundo plano ##################
thread = Thread(target=getData)
thread.start()

while isReceiving != True:
  print('iniciando recepcion de datos')
  time.sleep(0.1)

################## Interfaz grafica ##################
root = Tk()
root.protocol('WM_DELETE_WINDOW', onClosing)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=0, column=0)

anim = animation.FuncAnimation(fig, plotData, fargs=(lines, lineValueText, data_dict), interval=sampleTime)

root.mainloop()
