import serial
import time

# Configuración del puerto serial
s = serial.Serial(
    port='COM3',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=3
)

# Configurar terminador
s.newline = '\r'

# Esperar un momento para asegurarse de que el puerto esté listo
time.sleep(2)

# Intentar leer datos varias veces
max_attempts = 5
attempt = 0
data_received = False
full_data_string = ''

while attempt < max_attempts and not data_received:
    time.sleep(1)  # Esperar un segundo antes de intentar leer
    if s.in_waiting > 0:  # Comprobar si hay datos en el buffer
        dat = s.readline().decode('utf-8').strip()
        if len(dat) > 0:
            data_received = True
            print(f"Data received: {dat}")
            print(f"Length of data: {len(dat)}")
            print("Characters in the data:")
            for i, char in enumerate(dat):
                print(f"Char {i}: '{char}' (ASCII: {ord(char)})")
                full_data_string = full_data_string + str(char)
    else:
        print(f"No data received on attempt {attempt + 1}")
    attempt += 1

if not data_received:
    print("No data received after multiple attempts.")
else:
    print("Full data string:")
    print(full_data_string)

s.close()
