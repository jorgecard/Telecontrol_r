# import minimalmodbus

# # Configuración del dispositivo
# instrument = minimalmodbus.Instrument('COM4', 1)
# instrument.serial.baudrate = 9600  # Velocidad de baudios
# instrument.serial.bytesize = 8  # Tamaño de los bytes
# instrument.serial.parity = minimalmodbus.serial.PARITY_NONE  # Paridad
# instrument.serial.stopbits = 1  # Bits de parada
# instrument.serial.timeout = 3  # Tiempo de espera

# # Lee un registro específico
# registro = 0x0000  # Registro a leer
# num_registros = 1  # Número de registros a leer

# # Lectura de registros
# datos = instrument.read_registers(registro, num_registros)

# print("Datos leídos:", datos)


#!/usr/bin/env python3

import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

client = ModbusClient(method='rtu', port="COM4", baudrate=9600, parity='N', timeout=3)
# connection = client.connect()

# print(connection)

client.connect()
print(client.connect())
client.close()
# read_vals  = client.read_holding_registers(2501, 2, unit=1) # start_address, count, slave_id
# print(read_vals)
# print(read_vals.registers)

# write registers
# write  = client.write_register(1,425,unit=1)# address = 1, value to set = 425, slave ID = 1