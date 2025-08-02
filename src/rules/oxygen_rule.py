
from .base_rule import BaseRule

class OxygenRule(BaseRule):
    """
    Flags low oxygen saturation.
    Triggers alert if oxygen < 95%, citical below 90%.
    """

    def check(self, patient):
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
    
    def explain(self):
        return "Flags patients with oxygen satuuration below 95%, especially critical below 90%"