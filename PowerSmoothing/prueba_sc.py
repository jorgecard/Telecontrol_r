import struct
import time
from pymodbus.client.sync import ModbusTcpClient  # Para la conexión

# Realizar la conexión
ip = '192.168.222.14'  # IP batería de litio
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

# Puedes comprobar la conexión con
# print(client.connected)

# while True:
#     for address in range(0, 50):
#     # for address in range(23, 47):
#         # Descargar datos de un solo registro de entrada con una instrucción 0x04
#         raw_value = client.read_holding_registers(address=address, count=1, unit=1)

#         # Convertir el valor uint16 a su equivalente con signo
#         value = struct.unpack('<h', struct.pack('<H', raw_value.registers[0]))[0]
#         if address % 4 == 0:
#             print("")
#         print(f"Address: {address}   Value: {value}", end="\t")  # Usar tabulación para separar las columnas

#     # Esperar un segundo antes de la siguiente solicitud
#     print("--------- \n")
#     time.sleep(2)

value = -5
# value = 0
unsigned_value = struct.unpack('H', struct.pack('h', value))[0]
client.write_register(address = 38, value = unsigned_value, unit=1)  # Escribir en el registro 39

# Cerramos la conexión
client.close()