from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='rtu',port="COM4",stopbits=1,bytesize=8,parity='N',baudrate=9600, timeout=3, strict=False)
import time

connection = client.connect()
if connection == True:
    print('Conexión Exitosa')
else:
    print('Falla en la Conexión')
time.sleep(3)

value = client.read_input_registers(3000,83,unit=1)
# date = [value.registers[74],value.registers[73],value.registers[72]]
# tt = [value.registers[75],value.registers[76],value.registers[77]]
# print('Fecha: '+str(date[0])+'/'+str(date[1])+'/'+str(date[2])+' |  Hora: '+str(tt[0])+':'+str(tt[1])+':'+str(tt[2]))
# print('----------------------')

# voltaje=value.registers[21]*0.1
# print('Voltaje DC: '+str(round(voltaje,1))+' [V]')

if value is not None and hasattr(value, 'registers'):
    voltaje = value.registers[21] * 0.1
    print('Voltaje DC: ' + str(round(voltaje, 1)) + ' [V]')
else:
    print('No se pudo leer correctamente los registros')

import struct # Para decodificar los datos
raw_value = client.read_input_registers(3000,83,unit=1)
packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1]) 
value = struct.unpack('!f', packed_value)[0] 
print(value)

client.close()