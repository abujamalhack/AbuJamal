herefrom textual.widgets import Static
import asyncio
import random
import math
from datetime import datetime


class MatrixRain(Static):
    def __init__(self, speed=0.05):
        super().__init__("")
        self.speed = speed
        self.cols = 40
        self.rows = 20
        self.drops = [{'x': i, 'y': -i % 10, 'speed': random.randint(1, 3)} for i in range(self.cols)]
        self.chars = "01アイウエオカキクケコ"

    async def on_mount(self):
        asyncio.create_task(self.animate())

    async def animate(self):
        while True:
            grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
            for d in self.drops:
                y = int(d['y'])
                if 0 <= y < self.rows:
                    grid[y][d['x']] = random.choice(self.chars)
                d['y'] += d['speed']
                if d['y'] > self.rows:
                    d['y'] = -random.randint(1, 5)
            out = '\n'.join([''.join(row) for row in grid])
            self.update(f"[green]{out}[/]")
            await asyncio.sleep(self.speed)


class RadarWidget(Static):
    def __init__(self, speed=2.5):
        super().__init__("")
        self.speed = speed
        self.angle = 0

    async def on_mount(self):
        asyncio.create_task(self.rotate())

    async def rotate(self):
        while True:
            self.angle = (self.angle + 5) % 360
            self.update(self._render())
            await asyncio.sleep(self.speed / 36)

    def _render(self):
        size = 21
        center = 10
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        for r in [3, 6, 9]:
            for a in range(0, 360, 10):
                rad = math.radians(a)
                x = int(center + r * math.cos(rad))
                y = int(center + r * math.sin(rad))
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = 'o'
        rad = math.radians(self.angle)
        for r in range(1, 10):
            x = int(center + r * math.cos(rad))
            y = int(center + r * math.sin(rad))
            if 0 <= x < size and 0 <= y < size:
                grid[y][x] = '*'
        return '\n'.join([''.join(row) for row in grid])

class DigitalSkull(Static):
    def __init__(self):
        super().__init__("")
        self.frames = [
            "███████████████████████\n██▓▓▓▓▓░░░░░░░▓▓▓▓▓██\n██▓▓░░░░░░░░░░░▓▓██\n██▓░░░░░░░░░░░░░▓██\n███████████████████",
            "███████████████████████\n██▓▓▓▓▓░░░░░░░▓▓▓▓▓██\n██▓▓░░░░░░░░░░░▓▓██\n██▓▓░░░░░░░░░░░▓▓██\n███████████████████"
        ]
        self.frame = 0

    async def on_mount(self):
        asyncio.create_task(self.animate())

    async def animate(self):
        while True:
            color = random.choice(["red", "magenta", "bright_red"])
            self.update(f"[bold {color}]{self.frames[self.frame % 2]}[/]")
            self.frame += 1
            await asyncio.sleep(0.6)

class ThreatPanel(Static):
    def __init__(self):
        super().__init__("")
        self.threats = ["APT-41", "Sandworm", "Lazarus", "DarkHotel"]
        self.scores = [random.randint(45, 98) for _ in self.threats]

    async def on_mount(self):
        asyncio.create_task(self.update_threats())

    async def update_threats(self):
        while True:
            for i in range(len(self.scores)):
                self.scores[i] += random.randint(-5, 5)
                self.scores[i] = max(0, min(100, self.scores[i]))
            lines = []
            for name, score in zip(self.threats, self.scores):
                bar = '█' * (score // 5) + '░' * (20 - score // 5)
                color = "red" if score > 70 else "yellow"
                lines.append(f"[{color}]{name:<12} [{score:3d}%] {bar}[/]")
            self.update('\n'.join(lines))
            await asyncio.sleep(2)

class GeoLocationTracker(Static):
    def __init__(self):
        super().__init__("")
        self.lat = random.uniform(-90, 90)
        self.lon = random.uniform(-180, 180)

    async def on_mount(self):
        asyncio.create_task(self.update_location())

    async def update_location(self):
        while True:
            self.lat += random.uniform(-0.5, 0.5)
            self.lon += random.uniform(-0.5, 0.5)
            self.update(f"[cyan]📍 GEO TRACKING\nLAT: {self.lat:.4f}\nLON: {self.lon:.4f}\nACCURACY: {random.randint(3,15)}m[/]")
            await asyncio.sleep(1)


class SatelliteSyncPanel(Static):
    def __init__(self):
        super().__init__("")
        self.satellites = ["STARLINK-42", "IRIDIUM-7", "GPS-BIIF", "GLONASS-K"]

    async def on_mount(self):
        asyncio.create_task(self.update_sync())

    async def update_sync(self):
        while True:
            lines = [f"🛰️ {sat} {random.randint(60,100)}%" for sat in self.satellites]
            self.update("[magenta]SATELLITE SYNC\n" + "\n".join(lines) + "[/]")
            await asyncio.sleep(2)


class SignalStrengthGraph(Static):
    def __init__(self):
        super().__init__("")
        self.signal = 85

    async def on_mount(self):
        asyncio.create_task(self.animate_signal())

    async def animate_signal(self):
        while True:
            self.signal += random.randint(-10, 10)
            self.signal = max(20, min(100, self.signal))
            bar = "█" * (self.signal // 5) + "░" * (20 - self.signal // 5)
            self.update(f"[green]📡 SIGNAL STRENGTH\n{bar} {self.signal}%[/]")
            await asyncio.sleep(0.8)


class BiometricScanner(Static):
    async def on_mount(self):
        asyncio.create_task(self.scan())

    async def scan(self):
        while True:
            self.update("[red]🔬 BIOMETRIC SCAN\nFINGERPRINT: MATCH\nRETINAL: CLEAR\nVOICE: VERIFIED[/]")
            await asyncio.sleep(4)
            self.update("[red]🔬 BIOMETRIC SCAN\nFINGERPRINT: SCANNING...[/]")
            await asyncio.sleep(1)


class DarknetRelayMonitor(Static):
    async def on_mount(self):
        asyncio.create_task(self.update_relays())

    async def update_relays(self):
        relays = ["TOR-OBFS4", "I2P-DARK", "ZERONET-88", "FREENET-01"]
        while True:
            lines = []
            for r in relays:
                status = "🟢" if random.random() > 0.2 else "🔴"
                lines.append(f"{status} {r}  {random.randint(40,300)}ms")
            self.update("[purple]🌑 DARKNET RELAYS\n" + "\n".join(lines) + "[/]")
            await asyncio.sleep(1.5)


class EncryptedTunnelStatus(Static):
    async def on_mount(self):
        asyncio.create_task(self.update_tunnel())

    async def update_tunnel(self):
        layers = ["AES-256", "CHACHA20", "SERPENT", "TWOFISH"]
        while True:
            status = "\n".join([f"🔐 {l} : ACTIVE" for l in layers])
            self.update(f"[cyan]🚇 ENCRYPTED TUNNEL\n{status}[/]")
            await asyncio.sleep(2.5)


class AIConfidenceScore(Static):
    async def on_mount(self):
        asyncio.create_task(self.update_confidence())

    async def update_confidence(self):
        while True:
            score = random.randint(65, 99)
            bar = "█" * (score // 5) + "░" * (20 - score // 5)
            self.update(f"[magenta]🧠 AI CONFIDENCE\n{bar} {score}%[/]")
            await asyncio.sleep(1.2)


class ThreatProbabilityChart(Static):
    async def on_mount(self):
        asyncio.create_task(self.update_chart())

    async def update_chart(self):
        threats = ["APT41", "Sandworm", "Lazarus", "DarkHotel"]
        while True:
            lines = [f"{t}: {random.randint(20,95)}%" for t in threats]
            self.update("[red]📊 THREAT PROBABILITY\n" + "\n".join(lines) + "[/]")
            await asyncio.sleep(2)


class OperationTimer(Static):
    def __init__(self):
        super().__init__("")
        self.start = datetime.now()

    async def on_mount(self):
        asyncio.create(self.update_timer())

    async def update_timer(self):
        while True:
            elapsed = datetime.now() - self.start
            self.update(f"[yellow]⏱️ OPERATION ELAPSED\n{str(elapsed).split('.')[0]}[/]")
            await asyncio.sleep(1)


class TacticalHUD(Static):
    async def on_mount(self):
        asyncio.create_task(self.update_hud())

    async def update_hud(self):
        while True:
            hud = """
┌─────────────────────┐
│ TACTICAL STATUS     │
│ WEAPON SYSTEM: SAFE │
│ ECM: ACTIVE         │
│ COUNTERMEASURES: ON │
│ STEALTH: ENGAGED    │
└─────────────────────┘
            """
            self.update(f"[bold cyan]{hud}[/]")
            await asyncio.sleep(3)


class ClassifiedDocumentViewer(Static):
    async def on_mount(self):
        asyncio.create_task(self.update_docs())

    async def update_docs(self):
        docs = [
            "[TOP SECRET] TARGET PROFILE UPDATED",
            "[NOFORN] SIGNATURE MATCH 99.7%",
            "[OMEGA] EXECUTION ORDER RECEIVED"
        ]
        while True:
            self.update("[white]📄 CLASSIFIED DOCS\n" + random.choice(docs) + "[/]")
            await asyncio.sleep(5)


class CyberSkullAnimation(Static):
    async def on_mount(self):
        asyncio.create_task(self.animate())

    async def animate(self):
        skulls = ["💀", "☠️", "💀", "☠️"]
        i = 0
        while True:
            self.update(f"[red]{skulls[i % len(skulls)]} CYBER SKULL ACTIVE {skulls[(i+1)%len(skulls)]}[/]")
            i += 1
            await asyncio.sleep(0.5)
