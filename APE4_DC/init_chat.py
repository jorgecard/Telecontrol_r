from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException

# Configuración del equipo 63200A
ip_equipo = "192.168.222.59"  # Dirección IP del equipo 63200A
puerto_equipo = 23 # Puerto de comunicación Modbus TCP (típicamente 502)

# Crear un objeto Modbus TCP
client = ModbusTcpClient(ip_equipo, port=puerto_equipo, timeout=3)

# Conectar al equipo
connection = client.connect()
if not connection:
    print("No se pudo conectar al equipo.")
else:
    print("Conexión exitosa al equipo.")

    # Leer variables medidas del equipo
    try:
        lecturas = client.read_holding_registers(address=0, count=1, unit=1)  # Leer 10 registros de 16 bits
        if isinstance(lecturas, ModbusIOException):
            print(f"Error de IO al leer los registros: {lecturas}")
        elif lecturas.isError():
            print(f"Error al leer los registros: {lecturas}")
        else:
            print(f"Lecturas: {lecturas.registers}")
    except Exception as e:
        print(f"Excepción al leer los registros: {e}")

    # Cerrar la conexión
    client.close()