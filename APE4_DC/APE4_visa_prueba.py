import pyvisa

def check_visa_backend():
    try:
        rm = pyvisa.ResourceManager()
        print(f"Using VISA backend: {rm.visalib}")
    except Exception as e:
        print(f"Error checking VISA backend: {e}")
