import random

class SatelliteRelayCore:
    def __init__(self):
        self.satellites = ["STARLINK-001", "IRIDIUM-077", "GPS-BIIF-12", "GLONASS-K2"]

    def get_status(self):
        return {sat: random.randint(65, 100) for sat in self.satellites}

