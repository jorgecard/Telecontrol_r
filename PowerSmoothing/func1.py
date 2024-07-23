import os
import pandas as pd
import scipy.signal as signal

def get_unique_filename(base_path, base_name, extension):
    i = 0
    while True:
        filename = f"{base_name}{'(' + str(i) + ')' if i > 0 else ''}.{extension}"
        full_path = os.path.join(base_path, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1
         
def fac_SOC(SOC, P_aux):
    if (SOC > 80) and (P_aux > 0):
        k =1
    elif (SOC > 80) and (P_aux <= 0):
        k = 0.1
    elif (SOC >= 20) and (SOC <= 80):
        k = 1
    elif (SOC < 20) and (P_aux > 0):
        k = 0.1
    elif (SOC < 20) and (P_aux <= 0):
        k = 1
    else:
        k = 0
    return k

def control_rr(P_pv, P_pvc, SOC, rr):
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
        P_pvc = P_pvc + roc
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0,0

def control_e(P_pv, P_pvc, SOC, alpha):
    """
    Exponential Method.
    """
    try:
        t = len(P_pv) - 1
        
        # Compensated Photovoltaic Solar Power
        P_pvc = alpha * P_pv[t] + (1 - alpha) * P_pvc
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0,0

def control_staggered(P_pv, P_pvc, SOC, rampa_base, factor_dinamico):
    """
    Staggered Method.
    """
    try:
        t = len(P_pv) - 1

        # Calcular la media móvil
        mean_P_pv = sum(P_pv) / len(P_pv)
        
        roc = P_pv[t] - P_pv[t - 1]  # Cambio en la potencia del panel solar
        # Calcular rampa dinámica
        rr = rampa_base + factor_dinamico * abs(P_pv[t] - mean_P_pv)
        
        # Aplicación del control de rampa
        if abs(roc) > rr:
            if roc > 0:
                roc = rr
            else:
                roc = -rr
        
        # Compensated Photovoltaic Solar Power
        P_pvc = P_pvc + roc
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0,0

def control_Kalman(P_pv, P_pvc, SOC, P):
    """
    Kalman Filter.
    """
    try:
        
        # Parámetros del filtro de Kalman
        A = 1  # Matriz de transición de estados
        H = 1  # Matriz de observación
        Q = 1e-6  # Covarianza del ruido de proceso
        R = 1e-2  # Covarianza del ruido de observación
        x = P_pvc  # Estado inicial
        # P = 1  # Error inicial de covarianza
        
        t = len(P_pv) - 1

        # Predicción
        x_pred = A * x
        P_pred = A * P * A + Q
        # Actualización
        K = P_pred * H / (H * P_pred * H + R)  # Ganancia de Kalman
        x = x_pred + K * (P_pv[t] - H * x_pred)
        P = (1 - K * H) * P_pred
        
        # Compensated Photovoltaic Solar Power
        P_pvc = x
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc, P
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0,0, 1
    
def control_Wiener(P_pv, P_pvc, SOC):
    """
    Wiener Filter.
    """
    try:
        t = len(P_pv) - 1
        
        # Aplicar el filtro de Wiener a la ventana de tiempo
        smoothed_window = signal.wiener(P_pv, mysize=len(P_pv))
        
        # Compensated Photovoltaic Solar Power
        P_pvc = smoothed_window[-1]
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0,0
    
def control_Gaussian(P_pv, P_pvc, SOC, sigma = 10):
    """
    Gaussian Filter.
    """
    try:
        t = len(P_pv) - 1
        
        # Aplicar el filtro Gaussiano a la ventana de tiempo
        smoothed_window = signal.gaussian(len(P_pv), std=sigma)
        smoothed_window = signal.convolve(P_pv, smoothed_window/sum(smoothed_window), mode='same')
        
        # Compensated Photovoltaic Solar Power
        P_pvc = smoothed_window[-1]
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc
    except Exception as e:
        print(f"Error en control_Gaussian: {e}")
        return 0, 0