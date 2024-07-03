from pykeepass import PyKeePass
import os
from datetime import datetime
import pandas as pd

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_db = dir_actual
name_db = "Interciclo_pass.kdbx"
ruta_db = os.path.join(dir_db, name_db)

master_password = 'Telecontrol_Telemando_2024'

kp = PyKeePass(ruta_db, password=master_password)

# Leer las entradas del archivo KeePass
kp_entries = [{'title': entry.title, 'username': entry.username, 'password': entry.password, 'group': entry.group.name}
              for entry in kp.entries]

# print(kp_entries)

def getGroup(username, password):
    message = 'Usuario no identificado'
    for entry in kp_entries:
        if entry['username'] == username:
            if entry['password'] == password:
                message = entry["group"]
                # print('Contraseña correcta')
            else:
                message = 'Contraseña incorrecta'
                # print('Contraseña incorrecta')
            break
    writeLogs(username, password, message)
    # if not user_found:
    #     print('Usuario no encontrado')
    return message

nombre_archivotxt = "archivo_texto.txt"
ruta_archivotxt = os.path.join(dir_actual, nombre_archivotxt)

def writeLogs(username, password, message):
    fecha_hora_actual = datetime.now()
    formato_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.read_csv('registros.csv')
    reg = [(formato_fecha_hora, username, password, message)]
    df1 = pd.DataFrame(reg, columns=['Time','Username','Password','Message'])
    df = pd.concat([df, df1], ignore_index=True)
    eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
    df.drop(eliminar_colum, axis='columns', inplace=True)
    df.to_csv('registros.csv')