# https://github.com/suyashb95/SoftwareOscilloscope

# Modificar la clase BasePlot para aceptar un QWidget como contenedor del gráfico.

import serial, sys
from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np
# import signal

class BasePlot(object):
    def __init__(self, stream, parent=None, **kwargs):
        self.stream = stream
        self.parent = parent
        try:
            self.app = QtWidgets.QApplication([])
        except RuntimeError:
            self.app = QtWidgets.QApplication.instance()
            
        self.view = pg.GraphicsView()
        self.layout = pg.GraphicsLayout(border=(100,100,100))
        self.view.closeEvent = self.handle_close_event
        self.layout.closeEvent = self.handle_close_event
        self.view.setCentralItem(self.layout)
        
        if self.parent:
            self.parent.layout().addWidget(self.view)
        else:
            self.view.show()
            self.view.setWindowTitle('Software Oscilloscope')
            self.view.resize(800,600)
        
        self.plot_list = []
        self.legends = []

    def open_stream(self):
        print("Opening Stream")
        self.stream.open()
        
    def close_stream(self):
        if hasattr(self.stream, 'flushInput'):
            self.stream.flushInput()
        if hasattr(self.stream, 'flushOutput'):
            self.stream.flushOutput()
        self.stream.close()
        print("Stream closed")
        
    def handle_close_event(self, event):
        self.close_stream()
        self.app.exit()

    # Inicialización de Gráficos
    def plot_init(self):
        # Lee algunas líneas iniciales de datos para determinar el número de líneas de datos
        for _ in range(20):
            trial_data = self.stream.readline().decode('utf-8').rstrip().split(',')
        # Para cada línea de datos, crea un nuevo gráfico (addPlot), inicializa con datos cero y agrega una leyenda.
        for i in range(len(trial_data[0].split())):
            new_plot = self.layout.addPlot()
            # new_plot.setBackground('w')  # Fondo blanco para cada gráfico
            plot_data_item = new_plot.plot(np.zeros(250), name=f'Line {i+1}')
            self.plot_list.append(plot_data_item)
            legend = new_plot.addLegend()
            legend.addItem(plot_data_item, f'Line {i+1}')
            self.legends.append(legend)
            # Mueve el cursor del diseño a la siguiente fila para el próximo gráfico.
            self.layout.nextRow()
    
    # Actualiza los gráficos con nuevos datos
    def update(self):
        # Lee una línea de datos del flujo, la decodifica y divide en elementos individuales
        stream_data = self.stream.readline().decode('utf-8').rstrip().split(',')
        for data, line in zip(stream_data[0].split(), self.plot_list):
            y_data = line.yData
            y_data = np.roll(y_data, -1)
            y_data[-1] = float(data)
            x_data = np.arange(len(y_data))
            line.setData(x=x_data, y=y_data)
            # print(data)
    
    # Inicio de la Aplicación
    def start(self):
        self.open_stream()
        self.plot_init()
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(0)   
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            self.app.exec_()   

class SerialPlot(BasePlot):
    def __init__(self, com_port, baud_rate, parent=None, **kwargs):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = baud_rate
        self.serial_port.port = com_port
        super().__init__(self.serial_port, parent=parent, **kwargs)
        # super(SerialPlot, self).__init__(self.serial_port, **kwargs)

# class GenericPlot(BasePlot):
#     def __init__(self, stream, **kwargs):
#         if hasattr(stream, 'open') \
#         and hasattr(stream, 'close') \
#         and hasattr(stream, 'readline'):
#             super(GenericPlot, self).__init__(stream, **kwargs)
#         else:
#             raise AttributeError("One of the open/close/readline attributes is missing")
