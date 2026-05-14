import random

class SignalTraceEngine:
    def __init__(self):
        self.hops = random.randint(8, 15)

    def trace(self, target):
        return [f"Hop {i}: 10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}" for i in range(self.hops)]

