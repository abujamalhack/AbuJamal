import asyncio
import random
from rich.console import Console
from textual.app import App
from ui.dashboard import CyberDashboard
from themes.theme_manager import ThemeManager
from modules.telemetry import TelemetryGenerator
from modules.network import NetworkSimulator
from effects.glitch import GlitchEffect


class CyberIntelligenceEngine:
    def __init__(self, config):
        self.config = config
        self.console = Console()
        self.theme_manager = ThemeManager(config)
        self.telemetry = TelemetryGenerator()
        self.network_sim = NetworkSimulator()
        self.glitch = GlitchEffect()

    async def run(self):
        await self._startup_sequence()
        app = CyberDashboard(
            config=self.config,
            theme_manager=self.theme_manager,
            telemetry=self.telemetry,
            network_sim=self.network_sim,
            glitch=self.glitch
        )
        await app.run_async()

    async def _startup_sequence(self):
        startup_art = """
        ╔══════════════════════════════════════════════════════════════════╗
        ║     ▄████████  ▄█   ▄█          ▄████████ ████████▄     ▄████████ ║
        ║    ███    ███ ███  ███         ███    ███ ███   ▀███   ███    ███ ║
        ║    ███    █▀  ███▌ ███         ███    ███ ███    ███   ███    █▀  ║
        ║    ███        ███▌ ███        ▄███▄▄▄▄██▀ ███    ███  ▄███▄▄▄     ║
        ║  ▀███████████ ███▌ ███       ▀▀███▀▀▀▀▀   ███    ███ ▀▀███▀▀▀     ║
        ║           ███ ███  ███         ███    ███ ███    ███   ███    █▄  ║
        ║     ▄█    ███ ███  ███▌    ▄   ███    ███ ███   ▄███   ███    ███ ║
        ║   ▄████████▀  █▀   █████▄▄██   ██████████ ████████▀    ██████████ ║
        ║                      ▀                                            ║
        ║           CYBER INTELLIGENCE TERMINAL // CLASSIFIED              ║
        ╚══════════════════════════════════════════════════════════════════╝
        """
        self.console.print(startup_art, style="bold red")
        await asyncio.sleep(2)
        msgs = [
            ("[>] AI Core Online", "cyan"),
            ("[>] Quantum Entropy Active", "magenta"),
            ("[>] Darknet Handshake Complete", "green"),
            ("[>] Threat Analysis Engine Ready", "red")
        ]
        for msg, color in msgs:
            self.console.print(f"[{color}]{msg}[/{color}]")
            await asyncio.sleep(0.5)
        await asyncio.sleep(1)
        self.console.clear()
