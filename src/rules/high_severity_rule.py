from rules.base_rule import BaseRule

class HighSeverityRule(BaseRule):
    def apply(self, event) -> dict:
        """Decide based on severity field in the event input."""
        result = {
            "rule": "HighSeverityRule",
            "decision": "FLAG" if event.get("severity", "").lower() == "high" else "PASS",
            "reason": "Event marked as high severity" if event.get("severity", "").lower() == "high" else "Severity not high"
        }
        return result
