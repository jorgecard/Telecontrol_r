import struct
from pymodbus.client.sync import ModbusTcpClient

def read_modbus_data(ip_address, port, address, count):
    try:
        client = ModbusTcpClient(ip_address, port=port, timeout=3)
        client.connect()

        raw_value = client.read_holding_registers(address=address, count=count, unit=1)

        if raw_value.isError():
            print("Error:", raw_value)
            return None
        else:
            packed_value = struct.pack('>I', (raw_value.registers[0] << 16) | raw_value.registers[1])
            value = struct.unpack('!f', packed_value)[0]
            return value

    except Exception as e:
        print("Error:", e)
        return None

    finally:
        client.close()

ip_address = '192.168.222.136'
port = 502

count = 10

voltage = read_modbus_data(ip_address, port, 2, count)
current = read_modbus_data(ip_address, port, 13, count)

if voltage is not None and current is not None:
    print("Voltage:", voltage)
    print("Current:", current)
else:
    print("Failed to read data.")
