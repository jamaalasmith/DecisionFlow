from rules.base_rule import BaseRule

class HighSeverityRule(BaseRule):
    def check(self, event: dict):
        severity = event.get("severity", "").lower()
        should_alert = severity == "high"
        reason = "Event marked as high severity" if should_alert else "Severity not high"
        return should_alert, reason