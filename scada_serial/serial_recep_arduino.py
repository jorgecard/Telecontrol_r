import serial

# Configura el puerto serial
ser = serial.Serial(
    port='COM7',         # Puerto serial
    baudrate=9600,       # Velocidad en baudios
    timeout=1            # Tiempo de espera para la lectura
)

if ser.is_open:
    print("Conectado al puerto COM7")

    try:
        while True:
            # Leer línea desde el puerto serial
            line = ser.readline().decode('ascii', errors='ignore').strip()
            if line:
                print(f"Datos recibidos: {line}")                
    except KeyboardInterrupt:
        print("Lectura interrumpida por el usuario")
    finally:
        ser.close()
else:
    print("No se pudo conectar al puerto COM7")
