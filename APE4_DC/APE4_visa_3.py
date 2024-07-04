import pyvisa

# Crear el gestor de recursos
rm = pyvisa.ResourceManager()

# Conectar al instrumento usando la dirección IP y puerto (59 Carga programable)
instrument = rm.open_resource('TCPIP0::192.168.222.59::2101::SOCKET')

# Configurar el tiempo de espera a 5000 ms (5 segundos)
instrument.timeout = 100

# Asegurar la terminación correcta
instrument.write_termination = '\n'
instrument.read_termination = '\n'

# Comando para setear la potencia a 5 W
# potencia_deseada = 5  # Valor de potencia deseada (500 W)
# instrument.write(f'SOUR:POW {potencia_deseada}')

# Enviar el comando de medición
instrument.write('MEAS:VOLT?')
# instrument.write('LOAD:ID?') # (ID de la carga)
# instrument.write('MEAS:CURR?')
# instrument.write('MEAS:POW?')

# Leer la respuesta del instrumento
try:
    response = instrument.read()
    print(f": {response}")
except pyvisa.errors.VisaIOError as e:
    print(f"Error de lectura: {e}")

# Cerrar la conexión
instrument.close()
