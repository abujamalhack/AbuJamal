import random

class NetworkSimulator:
    def get_darknet_status(self):
        relays = ["TOR-01", "I2P-42", "ZeroNet-88"]
        status = []
        for r in relays:
            status.append(f"🟢 {r} ACTIVE  {random.randint(50,200)}ms")
        status.append("🛰️ SAT UPLINK: STARLINK")
        return "\n".join(status)
