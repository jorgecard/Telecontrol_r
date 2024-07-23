import os
import pandas as pd

def get_unique_filename(base_path, base_name, extension):
    i = 0
    while True:
        filename = f"{base_name}{'(' + str(i) + ')' if i > 0 else ''}.{extension}"
        full_path = os.path.join(base_path, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1
         
         
def control_rr(rr, P_pv):
    """
    RR Method.
    """
    try:
        t = len(P_pv) - 1

        roc = P_pv[t] - P_pv[t - 1]  # Cambio en la potencia del panel solar
        
        # Aplicación del control de rampa
        if abs(roc) > rr:
            if roc > 0:
                roc = rr
            else:
                roc = -rr
        
        # Compensated Photovoltaic Solar Power
        P_pvc = P_pv[t - 1] + roc
        P_aux = P_pvc - P_pv[t]
        
        # print(f"Media móvil (últimos {window} valores): {mean_P_pv}")
        # print(f"Rampa dinámica: {rr}")
        print(f"Power Change: {roc}")
        # print(f"Compensated Photovoltaic Solar Power: {P_pvc}")
        print(f"P_sc_aux: {P_aux}")
        
        return P_aux
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0
    
def control1(window,rampa_base,factor_dinamico, data_array):
    """
    Calcular la media móvil de los últimos valores en data_array.
    """
    try:
        print(f'data_array: {data_array}')
        
        # Calcular la media móvil
        if len(data_array) < window:
            mean_P_pv = sum(data_array) / len(data_array)  # Media de los disponibles si no hay suficientes datos
        else:
            mean_P_pv = sum(data_array[-window:]) / window  # Media de los últimos 'window' valores
        
        t = len(data_array) - 1
        P_pv_t = data_array[t]
        P_pv_t_minus_1 = data_array[t - 1]
        roc = P_pv_t - P_pv_t_minus_1  # Cambio en la potencia del panel solar
        
        # Calcular rampa dinámica
        rr = rampa_base + factor_dinamico * abs(P_pv_t - mean_P_pv)
        
        # Aplicación del control de rampa
        if abs(roc) > rr:
            if roc > 0:
                roc = rr
            else:
                roc = -rr
        
        # Compensated Photovoltaic Solar Power
        P_pvc = P_pv_t_minus_1 + roc
        P_aux = P_pvc - P_pv_t
        
        print(f"Media móvil (últimos {window} valores): {mean_P_pv}")
        print(f"Rampa dinámica: {rr}")
        print(f"Power Change: {roc}")
        print(f"Compensated Photovoltaic Solar Power: {P_pvc}")
        print(f"P_sc_aux: {P_aux}")
        
        return P_aux
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0
