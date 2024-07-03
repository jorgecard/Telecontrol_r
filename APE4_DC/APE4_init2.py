from pymodbus.client.sync import ModbusTcpClient

# Configuración del equipo 63200A
ip_equipo = "192.168.222.59"  # Dirección IP del equipo 63200A
puerto_equipo = 80  # Puerto de comunicación del equipo 63200A

# Crear un objeto Modbus TCP
client = ModbusTcpClient(ip_equipo, puerto_equipo, timeout=1)
# client = ModbusTcpClient(ip_equipo, puerto_equipo, parity='N', stopbits=1, bytesize=8)
# parity – ‘E’ven, ‘O’dd or ‘N’one
# stopbits – Number of stop bits 1, 1.5, 2.

# Conectar al equipo
client.connect()

# Leer variables medidas del equipo
# lecturas = client.read_holding_registers(0x0000, 10)  # Leer 10 registros de 16 bits
lecturas = client.read_holding_registers(address= 1, count= 1, slave= 1)

# Mostrar las lecturas
print(lecturas)

# Cerrar la conexión
client.close()