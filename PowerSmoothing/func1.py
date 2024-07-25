import os
import numpy as np

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
        Q = 1e-7  # Covarianza del ruido de proceso
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

def control_Kalman_Exponential(P_pv, P_pvc, SOC, P, alpha = 0.01):
    """
    Kalman Exponential
    """
    try:
        
        # Parámetros del filtro de Kalman
        A = 1  # Matriz de transición de estados
        H = 1  # Matriz de observación
        Q = 0.01  # Covarianza del ruido de proceso
        R = 0.1  # Covarianza del ruido de observación
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
        P_pvc = alpha * x + (1 - alpha) * P_pvc
        P_aux = P_pvc - P_pv[t]
        
        # SOC
        k = fac_SOC(SOC, P_aux)
        P_sc = P_aux * k
        
        return P_sc, P_pvc, P
    except Exception as e:
        print(f"Error en control1: {e}")
        return 0,0, 1

def control_Butterworth(P_pv, P_pvc, SOC, a, b, x_prev, y_prev, alpha=0.01):
    """
    Butterworth Filter with Exponential Smoothing
    """
    try:
        t = len(P_pv) - 1

        for t in range(len(P_pv)):
            P_pvc = (b[0] * P_pv[t] + b[1] * x_prev[0] + b[2] * x_prev[1] + b[3] * x_prev[2] + b[4] * x_prev[3] 
                              - a[1] * y_prev[0] - a[2] * y_prev[1] - a[3] * y_prev[2] - a[4] * y_prev[3]) / a[0]

            # Actualizar condiciones iniciales
            x_prev = np.roll(x_prev, 1)
            x_prev[0] = P_pv[t]
            y_prev = np.roll(y_prev, 1)
            y_prev[0] = P_pvc

            # Potencia Fotovoltaica Compensada con suavizado exponencial
            P_pvc = alpha * P_pv[t] + (1 - alpha) * P_pvc
            P_aux = P_pvc - P_pv[t]
            # SOC
            k = fac_SOC(SOC, P_aux)
            # Ajuste de la potencia de la batería para suavizar
            P_sc = P_aux * k

        return P_sc, P_pvc, a, b, x_prev, y_prev
    except Exception as e:
        print(f"Error en control_Butterworth: {e}")
        # return np.zeros_like(P_pv), 0, np.zeros_like(P_pv)