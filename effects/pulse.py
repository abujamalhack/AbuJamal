import asyncio

class PulseEffect:
    async def red_pulse(self, console):
        for _ in range(3):
            console.print("\033[41m" + " " * 80 + "\033[0m")
            await asyncio.sleep(0.1)
            console.clear()
            await asyncio.sleep(0.1)
