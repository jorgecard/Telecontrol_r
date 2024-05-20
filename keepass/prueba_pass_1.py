from pykeepass import PyKeePass
import os

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_db = dir_actual
name_db = "Interciclo_pass.kdbx"
ruta_db = os.path.join(dir_db, name_db)

master_password = 'Telecontrol_Telemando_2024'

kp = PyKeePass(ruta_db, password=master_password)

# Leer las entradas del archivo KeePass
kp_entries = [{'title': entry.title, 'username': entry.username, 'password': entry.password}
              for entry in kp.entries]
print(kp_entries)


username = 'Jorge Cardenas'
password = '.%u`B,s6m)v//?5jH=Ae5+<k)'

user_found = False

for entry in kp_entries:
    if entry['username'] == username:
        user_found = True
        if user_found == True:
            if entry['password'] == password:
                print('Contraseña correcta')
            else:
                print('Contraseña incorrecta')
            break

# Si el usuario no fue encontrado
if not user_found:
    print('Usuario no encontrado')