
def check_oxygen(patient):
    """
    Flags low oxygen saturation
    Returns a tuple: (boolean, reason)
    """
    oxy = patient.get('oxygen_saturation')

    try:
        oxy = float(oxy)
    except (TypeError, ValueError):
        return False, "Missing or invalid oxygen data"
    
    if oxy < 90:
        return True, f"Critical oxygen level detected: {oxy}%" 
    elif oxy < 95: 
        return True, f"Critical oxygen level detected: {oxy}%"
    else:
        return False, "Oxygen normal"