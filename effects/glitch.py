import random
import asyncio

class GlitchEffect:
    async def apply_to_screen(self, app):
        original = app.screen.styles.background
        app.screen.styles.background = "red"
        app.refresh()
        await asyncio.sleep(0.05)
        app.screen.styles.background = original
        app.refresh()
        await asyncio.sleep(0.03)
        app.screen.styles.offset = (random.randint(-2, 2), 0)
        app.refresh()
        await asyncio.sleep(0.03)
        app.screen.styles.offset = (0, 0)
        app.refresh()
