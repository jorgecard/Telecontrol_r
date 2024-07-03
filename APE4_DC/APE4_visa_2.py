import pyvisa
import time

# Crear el gestor de recursos
rm = pyvisa.ResourceManager()

# Conectar al instrumento usando la dirección IP y puerto
instrument = rm.open_resource('TCPIP0::192.168.222.59::2101::SOCKET')

# Configurar el tiempo de espera a 5000 ms (5 segundos)
instrument.timeout = 5000

# Asegurar la terminación correcta
instrument.write_termination = '\n'
instrument.read_termination = '\n'

# Comando para setear la potencia a 5 W
potencia_deseada = 5  # Valor de potencia deseada (500 W)
instrument.write(f'SOUR:POW {potencia_deseada}')

# Comando para setear la corriente a 1 A
corriente_deseada = 1.0  # Valor de corriente deseada (1 A)
instrument.write(f'SOUR:CURR {corriente_deseada}')

# Mantener la potencia y la corriente y mostrar los valores de voltaje, corriente y potencia durante 10 segundos
start_time = time.time()
duration = 10  # Duración en segundos

try:
    while time.time() - start_time < duration:
        # Medir el voltaje
        instrument.write('MEAS:VOLT?')
        voltaje = instrument.read()
        
        # Medir la corriente
        instrument.write('MEAS:CURR?')
        corriente = instrument.read()
        
        # Medir la potencia
        instrument.write('MEAS:POW?')
        potencia = instrument.read()
        
        # Mostrar los valores
        print(f"Voltaje: {voltaje} V, Corriente: {corriente} A, Potencia: {potencia} W")
        
        # Esperar un breve momento antes de la siguiente medición
        time.sleep(1)
except pyvisa.errors.VisaIOError as e:
    print(f"Error de lectura: {e}")

# Detener la potencia y la corriente (ajustar a 0)
instrument.write('SOUR:POW 1')
instrument.write('SOUR:CURR 1')

# Confirmar que la potencia y la corriente se han detenido
instrument.write('MEAS:POW?')
instrument.write('MEAS:CURR?')

try:
    potencia_detenida = instrument.read()
    corriente_detenida = instrument.read()
    print(f"Potencia detenida: {potencia_detenida} W, Corriente detenida: {corriente_detenida} A")
except pyvisa.errors.VisaIOError as e:
    print(f"Error de lectura: {e}")

# Cerrar la conexión
instrument.close()
