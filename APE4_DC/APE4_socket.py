import socket

def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Establece un tiempo de espera de 1 segundo
        try:
            sock.connect((ip, port))
            return True, "Open"
        except socket.timeout:
            return False, "Timeout"
        except socket.error as e:
            return False, str(e)

ip = '192.168.222.57'
start_port = 503
end_port = 2102

open_ports = []

for port in range(start_port, end_port + 1):
    is_open, status = check_port(ip, port)
    if is_open:
        print(f"Puerto {port} en la dirección {ip} está abierto ----------------.")
        open_ports.append(port)
    else:
        print(f"Puerto {port} NO: {status}")

if open_ports:
    print(f"Puertos abiertos: {open_ports}")
else:
    print("No se encontraron puertos abiertos en el rango especificado.")
