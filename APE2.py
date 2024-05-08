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
ip = '192.168.222.136' # Coloca la dirección IP de tu multímetro
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

# Definir un diccionario para almacenar los datos
data_dict = {
  'Voltaje DC1': {'offset': 9, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC1', 'unit': ' [V]', 'graphic':1, 'factor':1/3.4},
#   'Voltaje DC2': {'offset': 13, 'reg': 1, 'color': '#9103A6', 'label': 'Voltaje DC2', 'unit': ' [V]','graphic':1, 'factor':1},
  'Voltaje AC': {'offset': 21, 'reg': 1, 'color': '#19A63C', 'label': 'Voltaje AC', 'unit': ' [V]','graphic':1,'factor':0.1},
  'Corriente DC': {'offset': 31, 'reg': 1, 'color': '#DF8905', 'label': 'Corriente DC', 'unit': ' [A]','graphic':2,'factor':1},
  'Potencia DC': {'offset': 29, 'reg': 1, 'color': '#54548D', 'label': 'Potencia DC', 'unit': ' [kW]','graphic':3,'factor':0.01},
  'THD': {'offset': 19, 'reg': 1, 'color': '#ADD8E6', 'label': 'THD', 'unit': ' [%]','graphic':4,'factor':0.01},
  'Energía Neta': {'offset': 33, 'reg': 1, 'color': '-w', 'label': 'Energía Neta', 'unit': ' [kWh]','graphic':5,'factor':1},
  'Frecuencia': {'offset': 23, 'reg': 1, 'color': '-w', 'label': 'Frecuencia', 'unit': ' [Hz]','graphic':5,'factor':1},
}

def getData():
  time.sleep(1)
  while (isRun):
    global isReceiving
    global value
    for key, val in data_dict.items():
    #   raw_value = client.read_holding_registers(address=val['offset'], count=val['reg'], unit = 1)
    #   packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1])
    #   value[key] = round(struct.unpack('!f', packed_value)[0], 2)
      raw_value = client.read_input_registers(address=val['offset'], count=val['reg'], unit = 1)
      value[key] = round(struct.unpack('<h', struct.pack('<H', raw_value.registers[0]))[0], 2)
    isReceiving = True

def onClosing():
    global isRun
    isRun = False
    thread.join()
    root.quit()
    root.destroy()

def plotData(self, lines, lineValueText, lineLabel):
    for key, val in data_dict.items():
        value_scaled = value[key] * val['factor']
        data[key].append(value_scaled)
        lines[key].set_data(range(Samples), data[key])
        # lineValueText[key].set_text(val['label'] +' = '+ str(value[key]) + val['unit'])
        lineValueText[key].set_text(f"{val['label']} = {value[key] * val['factor']:.2f}{val['unit']}")


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
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 6), facecolor='0.94')
# plt.subplots_adjust(hspace=0.4)
# plt.subplots_adjust(left=0.05, right=0.48, bottom=0.05, top=0.95, hspace=0.4)
plt.subplots_adjust(left=0.05, right=0.70, bottom=0.05, top=0.95, hspace=0.4)

# Primera subtrama
ax1.set_title('VOLTAJES')
ax1.grid()
ax1.set_xlabel('Muestras')
ax1.set_ylabel('Magnitud')
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(0, 400)

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
ax3.set_ylim(0, 2)

# Cuarta subtrama
ax4.set_title('THD')
ax4.grid()
ax4.set_xlabel('Muestras')
ax4.set_ylabel('Magnitud')
ax4.set_xlim(xmin, xmax)
ax4.set_ylim(0, 8)

lines = {}
lineValueText = {}

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for i, (key, val) in enumerate(data_dict.items()):
    if val['graphic'] == 1:
        ax = ax1
        count1 += 1
        count = count1
        x_space = 0.53
    elif val['graphic'] == 2:
        ax = ax2
        count2 += 1
        count = count2
        x_space = 0.53
    elif val['graphic'] == 3:
        ax = ax3
        count3 += 1
        count = count3
        x_space = 0.45
    elif val['graphic'] == 4:
        ax = ax4
        count4 += 1
        count = count4
        x_space = 0.65
    elif val['graphic'] == 5:
        ax = ax4
        count5 += 1
        count = count5
    if val['graphic'] != 5:
        lines[key], = ax.plot([], [], val['color'], label=val['label'])
        lineValueText[key] = ax.text(x_space, 0.95 - count * 0.065, '', transform=ax.transAxes)
    else:
        lines[key], = ax.plot([], [], val['color'], label=val['label'])
        lineValueText[key] = ax.text(1.2, 0.95 - count * 0.065, '', transform=ax.transAxes)

# Texto adicional en la interfaz gráfica
plt.figtext(0.85, 0.75, 'APE 2:\nMonitoreo en tiempo real\nProtocolo de Comunicación TCP-IP', ha='center', fontsize=15)
plt.figtext(0.85, 0.65, 'Docente: Ing. Edisson Villa A. MSc. PhD\nJorge Cárdenas B. & Augusto Rodas V.', ha='center', fontsize=15)

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