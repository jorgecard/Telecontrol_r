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
    'Voltage': {'offset': 1, 'reg': 2, 'color': 'b-', 'label': 'Voltaje', 'unit': ' [V]'},
    'Voltage2': {'offset': 3, 'reg': 2, 'color': '#ADD8E6', 'label': 'Voltaje2', 'unit': ' [V]'},
    'Current': {'offset': 13, 'reg': 2, 'color': 'r-', 'label': 'Corriente', 'unit': ' [A]'},
    'Current2': {'offset': 15, 'reg': 2, 'color': 'r-', 'label': 'Corriente', 'unit': ' [A]'}
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
