import serial.tools.list_ports

def listar_puertos_disponibles():
    puertos = serial.tools.list_ports.comports()
    puertos_disponibles = []

    for puerto in puertos:
        info_puerto = {
            'device': puerto.device,
            'manufacturer': puerto.manufacturer,
        }
        puertos_disponibles.append(info_puerto)
    
    return puertos_disponibles

if __name__ == "__main__":
    puertos = listar_puertos_disponibles()
    
    if puertos:
        print("Información de puertos COM disponibles:")
        for puerto in puertos:
            print(f"Dispositivo: {puerto['device']}")
            print(f"  Fabricante: {puerto['manufacturer']}")
            print("\n")
    else:
        print("No se encontraron puertos COM disponibles.")
