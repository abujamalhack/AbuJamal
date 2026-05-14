from textual.widgets import Static
import asyncio
import random
import math
from datetime import datetime


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
