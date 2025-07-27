from src.core.logging import log_step, get_trace

def main():
   print("🚀 DecisionFlow core initialized")

   log_step("Engine initialized")
   log_step("Sample input recieved", {"event": "anomaly detected", "severity": "high"})

   trace = get_trace()

   print("Decision Trace:")
   for entry in trace:
      print(entry)
      
# only run if this file is executed directly (Not imported)
if __name__ == "__main__":
   main()