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

import time
import struct
from pymodbus.client.sync import ModbusTcpClient # Para la conexión
from pymodbus.exceptions import ModbusIOException

# Realizar la conexión
# ip = '192.168.222.136' # Ampere 502
ip = '192.168.222.136' # Coloca la dirección IP de tu dispositivo Modbus 80 Carga
# ip = '192.168.222.45' # Coloca la dirección IP de tu dispositivo Modbus
# ip = '192.168.222.60' # Coloca la dirección IP de tu dispositivo Modbus
port = 502
client = ModbusTcpClient(ip, port=port, timeout=3)
# client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

while True:
    for address in range(0, 200):  # Cambiar la dirección de 1 a 24
        try:
            # Intentar leer registros de entrada
            # try:
            #     raw_value = client.read_input_registers(address=address, count=1, unit=1)
            #     value = struct.unpack('<h', struct.pack('<H', raw_value.registers[0]))[0]
            #     print(f"Input Registers - Address: {address}   Value: {value}", end="\n")
            # except ModbusIOException as e:
            #     pass

            # Intentar leer registros de retención
            try:
                raw_value = client.read_holding_registers(address=address, count=1, unit=1)
                if len(raw_value.registers) >= 2:
                    packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1]) 
                    value = struct.unpack('!f', packed_value)[0]
                    print(f"Holding Registers - Address: {address}   Value: {value}", end="\n")
            except ModbusIOException as e:
                pass

            # # Intentar leer registros discretos de entrada
            # try:
            #     raw_value = client.read_discrete_inputs(address=address, count=1, unit=1)
            #     value = raw_value.bits[0]
            #     print(f"Discrete Inputs - Address: {address}   Value: {value}", end="\n")
            # except ModbusIOException as e:
            #     pass

        except ModbusIOException as e:
            print(f"Error de lectura en la dirección {address}: {e}")

    # Esperar un segundo antes de la siguiente solicitud
    print("\n--------- \n")
    time.sleep(2)

# Cerramos la conexión
client.close()