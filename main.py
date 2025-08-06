from src.core.logging import log_step, get_trace
from src.rules.oxygen_rule import OxygenRule

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
   sample = {"patient_id": "X01", "oxygen_saturation": 87}

   # Apply the oxygen rule to check if this triggers an alert
   rule = OxygenRule()
   alert, reason = rule.check(sample)

   # Output the result to console
   if alert:
      print(f"🚨 ALERT for {sample['patient_id']}: {reason}")
   else:
      print(f"✅ {sample['patient_id']}: {reason}")
      
# Only run if this file is executed directly (Not imported as a module)
if __name__ == "__main__":
   main()