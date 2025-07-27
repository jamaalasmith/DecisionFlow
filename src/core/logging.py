decision_log = []

def log_step(step: str, data: dict = None):
    entry = {
        "step": step,
        "data": data if data else {},
    }
    decision_log.append(entry)

def get_trace():
    return decision_log