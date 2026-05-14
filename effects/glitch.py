import random
import asyncio

class GlitchEffect:
    async def simulate_glitch(self, console):
        for _ in range(random.randint(3, 7)):
            console.print("".join(random.choice(["█","▓","▒","░"]) for _ in range(80)), style="red", end="")
            await asyncio.sleep(0.03)
        await asyncio.sleep(0.1)

    async def fullscreen_glitch(self, console):
        for _ in range(5):
            console.print("\033[41m" + " " * 80 + "\033[0m")
            await asyncio.sleep(0.05)
        console.clear()

    async def apply_to_screen(self, app):
        # تطبيق glitch على واجهة Textual
        original = app.screen.styles.background
        app.screen.styles.background = "red"
        app.refresh()
        await asyncio.sleep(0.05)
        app.screen.styles.background = original
        app.refresh()
        await asyncio.sleep(0.03)
        app.screen.styles.offset = (random.randint(-3,3), 0)
        app.refresh()
        await asyncio.sleep(0.03)
        app.screen.styles.offset = (0,0)
        app.refresh()
