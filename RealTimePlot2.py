import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from tkinter import *
from threading import Thread
import sys
import struct
from pymodbus.client.sync import ModbusTcpClient
import time

# Realizar la conexión
ip = '192.168.0.76'
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

# Definir diccionarios para almacenar los datos
data_dict_1 = {
    'Voltage': {'offset': 1, 'reg': 2, 'color': 'b-', 'label': 'Voltaje', 'unit': ' [V]'},
    'Voltage2': {'offset': 3, 'reg': 2, 'color': '#ADD8E6', 'label': 'Voltaje2', 'unit': ' [V]'}
}

data_dict_2 = {
    'Current': {'offset': 13, 'reg': 2, 'color': 'r-', 'label': 'Corriente', 'unit': ' [A]'},
    'Current2': {'offset': 15, 'reg': 2, 'color': 'r-', 'label': 'Corriente2', 'unit': ' [A]'}
}

def getData(data_dict):
    time.sleep(1)
    while isRun:
        global isReceiving
        global value
        for key, val in data_dict.items():
            raw_value = client.read_holding_registers(address=val['offset'], count=val['reg'], unit=1)
            packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1])
            value[key] = round(struct.unpack('!f', packed_value)[0], 2)
        isReceiving = True

def onClosing():
    global isRun
    isRun = False
    thread.join()
    root.quit()
    root.destroy()

def plotData(self, lines, lineValueText, data_dict):
    for key, val in data_dict.items():
        data[key].append(value.get(key, 0))  # Obtener el valor o 0 si la clave no está presente
        lines[key].set_data(range(Samples), data[key])
        lineValueText[key].set_text(val['label'] + ' = ' + str(value.get(key, 0)) + val['unit'])

# Plot Parameters -----------------
Samples = 100
sampleTime = 100  # Tiempo de muestreo / Sample Time
value = {key: 0 for key in data_dict_1.keys()}  # Inicializar todas las claves con el valor 0
data = {key: collections.deque([0] * Samples, maxlen=Samples) for key in data_dict_1.keys()}
isReceiving = False
isRun = True

# Crear graficas -------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), facecolor='0.94')

axes = [ax1, ax2]
data_dicts = [data_dict_1, data_dict_2]

for ax, data_dict in zip(axes, data_dicts):
    ax.grid()
    ax.set_xlabel('Muestras')
    ax.set_ylabel('Magnitud')

    lines = {}
    lineValueText = {}

    for i, (key, val) in enumerate(data_dict.items()):
        lines[key], = ax.plot([], [], val['color'], label=val['label'])
        lineValueText[key] = ax.text(0.65, 0.90 - i * 0.05, '', transform=ax.transAxes)

# Iniciar hilo para obtener los datos
thread = Thread(target=getData, args=(data_dict_1,))
thread.start()

# Esperar hasta que se reciban los datos
while not isReceiving:
    print('Iniciando recepcion de datos')
    time.sleep(0.1)

# Interfaz grafica
root = Tk()
root.protocol('WM_DELETE_WINDOW', onClosing)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=0, column=0)

# Animate
anim = animation.FuncAnimation(fig, plotData, fargs=(lines, lineValueText, data_dict_1), interval=sampleTime)

root.mainloop()
