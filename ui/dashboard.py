from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static
from ui.widgets import MatrixRain, RadarWidget, DigitalSkull, ThreatPanel
import asyncio


class CyberDashboard(App):
    CSS_PATH = "styles.tcss"

    def __init__(self, config, theme_manager, telemetry, network_sim, glitch):
        super().__init__()
        self.config = config
        self.theme_manager = theme_manager
        self.telemetry = telemetry
        self.network_sim = network_sim
        self.glitch = glitch

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Container(id="app-grid"):
            with Container(id="warning-bar"):
                yield Static("⚠️ CLASSIFIED SYSTEM - AUTHORIZED ACCESS ONLY ⚠️")
            with Horizontal(id="main-content"):
                with Vertical(id="left-panel", classes="panel"):
                    yield DigitalSkull()
                    yield RadarWidget(speed=self.config['simulation']['radar_speed'])
                    yield Static("SIGNAL INTELLIGENCE")
                    yield Static(self.telemetry.get_signal_strength(), id="signal-display")
                with Vertical(id="center-panel", classes="panel"):
                    yield Static("THREAT ASSESSMENT")
                    yield ThreatPanel()
                with Vertical(id="right-panel", classes="panel"):
                    yield Static("ENCRYPTED DATA STREAM")
                    yield MatrixRain(speed=self.config['simulation']['matrix_rain_speed'])
                    yield Static("DARKNET RELAYS")
                    yield Static(self.network_sim.get_darknet_status(), id="darknet-status")
            with Container(id="status-bar"):
                yield Static(id="telemetry-status")
                yield Static(id="quantum-status")
        yield Footer()

    async def on_mount(self):
        self.set_interval(self.config['simulation']['telemetry_update_rate'], self.update_telemetry)
        self.set_interval(1.0, self.update_network)
        if self.config['simulation']['glitch_frequency'] > 0:
            self.set_interval(4.0, self.random_glitch)

    def update_telemetry(self):
        status = self.query_one("#telemetry-status", Static)
        if status:
            status.update(self.telemetry.get_telemetry_string())
        q = self.query_one("#quantum-status", Static)
        if q:
            q.update(f"🔐 QUANTUM LAYERS: {self.config['fake_modules']['quantum_encryption_layers']}")

    def update_network(self):
        dark = self.query_one("#darknet-status", Static)
        sig = self.query_one("#signal-display", Static)
        if dark:
            dark.update(self.network_sim.get_darknet_status())
        if sig:
            sig.update(self.telemetry.get_signal_strength())

    async def random_glitch(self):
        import random
        if random.random() < self.config['simulation']['glitch_frequency']:
            await self.glitch.apply_to_screen(self)
