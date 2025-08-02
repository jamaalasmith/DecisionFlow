from src.core.logging import log_step, get_trace
from src.rules.oxygen_rule import OxygenRule

def main():
   print("🚀 DecisionFlow core initialized")

   log_step("Engine initialized")
   log_step("Sample input recieved", {"event": "anomaly detected", "severity": "high"})

   trace = get_trace()

   print("Decision Trace:")
   for entry in trace:
      print(entry)

   sample = {"patient_id": "X01", "oxygen_saturation": 87}
   rule = OxygenRule()
   alert, reason = rule.check(sample)
   if alert:
      print(f"🚨 ALERT for {sample['patient_id']}: {reason}")
   else:
      print(f"✅ {sample['patient_id']}: {reason}")
      
# only run if this file is executed directly (Not imported)
if __name__ == "__main__":
   main()