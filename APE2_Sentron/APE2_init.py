# # --------------------------------------------------------------------------- # 
# # Obtener datos del multímetro SENTRON PAC3200 de Siemens mediante modbus TCP con Python.
# # - Analizador: https://w5.siemens.com/spain/web/es/ic/building_technologies/sp_baja_tension/analizadores_sentron/SENTRONPAC3200/Pages/PAC3200.aspx
# # - Datasheet: https://www.automation.siemens.com/cd-static/material/info/e20001-a112-l300-x-7800.pdf
# # - Manual de Producto: https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf
# # --------------------------------------------------------------------------- # 

# # --------------------------------------------------------------------------- #
# # Librerías:
# # - struct: https://docs.python.org/3/library/struct.html
# # - comando instalación: pip install pymodbus==2.5.3
# # - pymodbus instalación: https://pypi.org/project/pymodbus/
# # - pymodbus: https://pymodbus.readthedocs.io/en/latest/
# # --------------------------------------------------------------------------- # 

# # prueba de registros -------------------------------------------

# import struct # Para decodificar los datos
# import time
# from pymodbus.client.sync import ModbusTcpClient # Para la conexión

# # Realizar la conexión
# ip = '192.168.222.136' # Coloca la dirección IP de tu dispositivo Modbus
# client = ModbusTcpClient(ip, port=502, timeout=3)
# client.connect()

# for address in range(2, 100):  # Cambiar la dirección de 2 a 18
#     # Descargar datos de registros de entrada con una instrucción 0x04
#     raw_value = client.read_input_registers(address=address, count=1, unit=1)

#     # VALOR DE 16 BITS ----------------------------
#     # valor está almacenado en dos registros y está en formato entero de 16 bits
#     # value = raw_value.registers[0]  # Obtener el valor del primer registro

#     # VALOR DE 32 BITS ---------------------------
#     # Combinar los registros para formar un valor de 32 bits
#     value = (raw_value.registers[1] << 16) | raw_value.registers[0]
#     # Si el valor es un número con signo (por ejemplo, int32), puedes convertirlo así
#     if value & 0x80000000:  # Comprobación del bit de signo
#         value -= 1 << 32  # Convertir a número negativo si es necesario
#     # # Si el valor es mayor a 32767 (se considera un número negativo en int16), convertirlo
#     # if value > 32767:
#     #     value -= 65536  # Restar 2^16 (65536) para obtener el valor negativo en int16
        
#     # decodificamos: -----------------------------
#     # packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1]) 
#     # value = struct.unpack('!f', packed_value)[0]
    
#     # decodificamos: -----------------------------
#     # packed_value = struct.pack('>Q',(raw_value.registers[0]<<48)|(raw_value.registers[1]<<32)|(raw_value.registers[2]<<16)|raw_value.registers[3])
#     # value = struct.unpack('!d', value)[0]
    
#     print("Address:", address, "Value:", value)

#     # Esperar un segundo antes de la siguiente solicitud
#     time.sleep(1)

# # # Descargar datos de registros de entrada con una instrucción 0x04
# # raw_value = client.read_input_registers(address=15, count=2, unit=1)

# # # Si el valor está almacenado en dos registros y está en formato entero de 16 bits
# # # decodificamos:
# # value = raw_value.registers[0]  # Obtener el valor del primer registro
# # # Si necesitas más registros para formar el valor completo, puedes combinarlos adecuadamente.

# # print(value)

# # Cerramos la conexión
# client.close()



# ------------- 

# import time
# from pymodbus.client.sync import ModbusTcpClient # Para la conexión

# # Realizar la conexión
# ip = '192.168.222.136' # Coloca la dirección IP de tu dispositivo Modbus
# client = ModbusTcpClient(ip, port=502, timeout=3)
# client.connect()

# while(1):
#     for address in range(1, 25):  # Cambiar la dirección de 2 a 18
#         # Descargar datos de un solo registro de entrada con una instrucción 0x04
#         raw_value = client.read_input_registers(address=address, count=1, unit=1)

#         # Si el valor es un número de tipo uint16, no es necesario combinar registros
#         value = raw_value.registers[0]

#         print("Address:", address, "Value:", value)

#     # Esperar un segundo antes de la siguiente solicitud
#     time.sleep(1)

# # Cerramos la conexión
# client.close()


import time
import struct
from pymodbus.client.sync import ModbusTcpClient # Para la conexión

# Realizar la conexión
ip = '192.168.222.136' # Coloca la dirección IP de tu dispositivo Modbus
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

while True:
    for address in range(0, 20):  # Cambiar la dirección de 1 a 24
        # Descargar datos de un solo registro de entrada con una instrucción 0x04
        raw_value = client.read_input_registers(address=address, count=1, unit=1)

        # Convertir el valor uint16 a su equivalente con signo
        value = struct.unpack('<h', struct.pack('<H', raw_value.registers[0]))[0]

        # print("Address:", address, "Value:", value)
        # Imprimir la dirección y el valor en tres columnas
        if address % 4 == 0:  # Imprimir un salto de línea cada tres direcciones
            print("")
        if value != 0:
            print(f"Address: {address}   Value: {value}", end="\t \t")  # Usar tabulación para separar las columnas

    # Esperar un segundo antes de la siguiente solicitud
    print("--------- \n")
    time.sleep(2)

# Cerramos la conexión
client.close()
