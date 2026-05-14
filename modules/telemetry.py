import random

class TelemetryGenerator:
    def __init__(self):
        self.cpu = random.randint(10, 90)
    def update(self):
        self.cpu += random.randint(-10, 10)
        self.cpu = max(0, min(100, self.cpu))
    def get_telemetry_string(self):
        self.update()
        bar = '█' * (self.cpu // 5) + '░' * (20 - self.cpu // 5)
        return f"⚡ CPU: [{self.cpu:3d}%] {bar}"
    def get_signal_strength(self):
        s = random.randint(40, 100)
        return f"📶 SIGNAL: {s}%"
