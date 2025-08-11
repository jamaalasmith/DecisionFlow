from src.core.logging import log_step, get_trace
from src.rules.oxygen_rule import OxygenRule
from src.rules.high_severity_rule import HighSeverityRule

def main():
   print("🚀 DecisionFlow core initialized")

   # Log the startup sequence
   log_step("Engine initialized")
   log_step("Sample input recieved", {"event": "anomaly detected", "severity": "high"})

   trace = get_trace()

   # Retrieve all log steps for traceability
   print("Decision Trace:")
   for entry in trace:
      print(entry)

   # Define a sample event to evaluate
   sample = {"patient_id": "X01", "oxygen_saturation": 87, "severity": "high"}

   # Apply both rules
   oxygen_rule = OxygenRule()
   severity_rule = HighSeverityRule()

   oxygen_alert, oxygen_reason = oxygen_rule.check(sample)
   severity_alert, severity_reason = severity_rule.check(sample)

   # Combine results for comprehensive alerting

   if oxygen_alert and severity_alert:
      print(f"🚨🔴  CRITICAL ALERT for {sample['patient_id']}: {oxygen_reason} + {severity_reason}")
   elif oxygen_alert:
      print(f"🚨 OXYGEN ALERT for {sample['patient_id']}: {oxygen_reason}")
   elif severity_alert:
      print(f"🔴 SEVERITY ALERT for {sample['patient_id']}: {severity_reason}")
   else:
      print(f"✅ {sample['patient_id']}: {oxygen_reason} + {severity_reason}")
      
# Only run if this file is executed directly (Not imported as a module)
if __name__ == "__main__":
   main()