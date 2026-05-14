import random

class DarkGridTelemetry:
    def get_metrics(self):
        return {"bandwidth": random.randint(10, 500), "latency": random.randint(20, 200)}
