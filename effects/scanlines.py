import asyncio

class ScanlineOverlay:
    def __init__(self, intensity=0.6):
        self.intensity = intensity

    async def sweep(self, console):
        for i in range(0, 24, 2):
            console.print(f"\033[{i};0H\033[47m" + " " * 80 + "\033[0m")
            await asyncio.sleep(0.02)
        console.clear()
