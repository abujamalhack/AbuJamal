import random

class SignalTraceEngine:
    def __init__(self):
        self.hops = random.randint(8, 15)
        self.current_trace = []

    def trace(self, target):
        # محاكاة تتبع الإشارة
        self.current_trace = [f"Hop {i}: {random.randint(10,999)}. {random.randint(100,999)}.{random.randint(1,254)}" for i in range(self.hops)]
        return self.current_trace
