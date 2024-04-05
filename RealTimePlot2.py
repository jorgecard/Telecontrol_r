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
  'Tensión L1-N': {'offset': 1, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L1-N', 'unit': '[V]', 'graphic':1, 'factor':1},
  'Tensión L2-N': {'offset': 3, 'reg': 2, 'color': '#9103A6', 'label': 'Tension L2-N', 'unit': '[V]','graphic':1, 'factor':1},
  'Tensión L3-N': {'offset': 5, 'reg': 2, 'color': '#9103A6', 'label': 'Tensión L3-N', 'unit': '[V]','graphic':1,'factor':1},
  'Tensión L1-L2': {'offset': 7, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L1-L2', 'unit': '[V]','graphic':1,'factor':1},
  'Tensión L2-L3': {'offset': 9, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L2-L3', 'unit': '[V]','graphic':1,'factor':1},
  'Tensión L3-L1': {'offset': 11, 'reg': 2, 'color': '#19A63C', 'label': 'Tensión L3-L1', 'unit': '[V]','graphic':1,'factor':1},
  'I-L1': {'offset': 13, 'reg': 2, 'color': '#DF8905', 'label': 'I-L1', 'unit': '[A]','graphic':2,'factor':1},
  'I-L2': {'offset': 15, 'reg': 2, 'color': '#DF8905', 'label': 'I-L2', 'unit': '[A]','graphic':2,'factor':1},
  'I-L3': {'offset': 17, 'reg': 2, 'color': '#DF8905', 'label': 'I-L3', 'unit': '[A]','graphic':2,'factor':1},
  'E-S': {'offset': 63, 'reg': 2, 'color': '#54548D', 'label': 'E-S', 'unit': '[VA]','graphic':3,'factor':1},
  'E-P': {'offset': 65, 'reg': 2, 'color': '#558D54', 'label': 'E-P', 'unit': '[W]','graphic':3,'factor':1},
  'E-Q': {'offset': 63, 'reg': 2, 'color': '#547E8D', 'label': 'E-Q', 'unit': '[VAR]','graphic':3,'factor':1},
  'THD-V1': {'offset': 261, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V1', 'unit': '[%]','graphic':4,'factor':1},
  'THD-V2': {'offset': 263, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V2', 'unit': '[%]','graphic':4,'factor':1},
  'THD-V3': {'offset': 265, 'reg': 2, 'color': '#ADD8E6', 'label': 'THD-V3', 'unit': '[%]','graphic':4,'factor':1},
  'THD-I1': {'offset': 267, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I1', 'unit': '[%]','graphic':4,'factor':1},
  'THD-I2': {'offset': 269, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I2', 'unit': '[%]','graphic':4,'factor':1},
  'THD-I3': {'offset': 271, 'reg': 2, 'color': '#EF2110', 'label': 'THD-I3', 'unit': '[%]','graphic':4,'factor':1},
  'Energía Aparente': {'offset': 2817, 'reg': 2, 'color': '#A74CEE', 'label': 'Energía Aparente', 'unit': '[kVAh]','graphic':5,'factor':1}
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

# Crear gráficas -------------------------------------------------------
# fig, ((ax1, ax2, ax3), (ax4, ax5, _)) = plt.subplots(2, 3, figsize=(12, 6), facecolor='0.94')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 6), facecolor='0.94')

# Primera subtrama
ax1.set_title('VOLTAJES')
ax1.grid()
ax1.set_xlabel('Muestras')
ax1.set_ylabel('Magnitud')
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(0, 300)

# Segunda subtrama
ax2.set_title('CORRIENTES')
ax2.grid()
ax2.set_xlabel('Muestras')
ax2.set_ylabel('Magnitud')
ax2.set_xlim(xmin, xmax)
ax2.set_ylim(0, 5)

# Tercera subtrama
ax3.set_title('POTENCIAS')
ax3.grid()
ax3.set_xlabel('Muestras')
ax3.set_ylabel('Magnitud')
ax3.set_xlim(xmin, xmax)
ax3.set_ylim(0, 800)

# Cuarta subtrama
ax4.set_title('THD')
ax4.grid()
ax4.set_xlabel('Muestras')
ax4.set_ylabel('Magnitud')
ax4.set_xlim(xmin, xmax)
ax4.set_ylim(0, 5.5)

lines = {}
lineValueText = {}

count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i, (key, val) in enumerate(data_dict.items()):
    if val['graphic'] == 1:
        ax = ax1
        count1 += 1
        count = count1
    elif val['graphic'] == 2:
        ax = ax2
        count2 += 1
        count = count2
    elif val['graphic'] == 3:
        ax = ax3
        count3 += 1
        count = count3
    elif val['graphic'] == 4:
        ax = ax4
        count4 += 1
        count = count4
    lines[key], = ax.plot([], [], val['color'], label=val['label'])
    lineValueText[key] = ax.text(0.65, 0.95 - count * 0.05, '', transform=ax.transAxes)
    # lineValueText[key] = ax.text(0.30, 0.95 - count * 0.05, '', transform=ax.transAxes)

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