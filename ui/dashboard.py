from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, Grid
from textual.widgets import Header, Footer, Static
from ui.widgets import (
    MatrixRain, RadarWidget, DigitalSkull, ThreatPanel,
    GeoLocationTracker, SatelliteSyncPanel, SignalStrengthGraph,
    BiometricScanner, DarknetRelayMonitor, EncryptedTunnelStatus,
    AIConfidenceScore, ThreatProbabilityChart, OperationTimer,
    TacticalHUD, ClassifiedDocumentViewer, CyberSkullAnimation
)
import asyncio


class CyberDashboard(App):
    CSS_PATH = "styles.tcss"

    def __init__(self, config, theme_manager, modules, glitch, scanlines, bloom, pulse, audio):
        super().__init__()
        self.config = config
        self.theme_manager = theme_manager
        self.modules = modules
        self.glitch = glitch
        self.scanlines = scanlines
        self.bloom = bloom
        self.pulse = pulse
        self.audio = audio

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Container(id="app-grid"):
            # شريط التحذير العلوي
            with Container(id="warning-bar"):
                yield Static("⚠️ [TOP SECRET // OMEGA CLEARANCE REQUIRED] ⚠️")
            
            # الشبكة الرئيسية 3x3
            with Grid(id="main-grid"):
                # الصف الأول
                yield DigitalSkull()                      # (0,0)
                yield RadarWidget(self.config['simulation']['radar_speed'])  # (0,1)
                yield GeoLocationTracker()                # (0,2)
                
                # الصف الثاني
                yield SatelliteSyncPanel()                # (1,0)
                yield ThreatPanel()                       # (1,1)
                yield SignalStrengthGraph()               # (1,2)
                
                # الصف الثالث
                yield BiometricScanner()                  # (2,0)
                yield DarknetRelayMonitor()               # (2,1)
                yield EncryptedTunnelStatus()             # (2,2)
                
                # الصف الرابع
                yield AIConfidenceScore()                 # (3,0)
                yield ThreatProbabilityChart()            # (3,1)
                yield OperationTimer()                    # (3,2)
                
                # الصف الخامس
                yield TacticalHUD()                       # (4,0)
                yield ClassifiedDocumentViewer()          # (4,1)
                yield CyberSkullAnimation()               # (4,2)
                
                # خلفية المطر الرقمي (يمتد على كامل الشاشة لكنه في الخلفية)
                yield MatrixRain(speed=self.config['simulation']['matrix_rain_speed'])
        
        yield Footer()

    async def on_mount(self):
        # تحديثات دورية
        self.set_interval(self.config['simulation']['telemetry_update_rate'], self.update_all_telemetry)
        self.set_interval(1.0, self.update_network_modules)
        if self.config['simulation']['glitch_frequency'] > 0:
            self.set_interval(3.0, self.random_glitch)
        if self.config['display']['bloom_enabled']:
            self.set_interval(0.5, self.update_bloom)

    async def update_all_telemetry(self):
        # تحديث بيانات التليمتري لجميع الوحدات
        for widget_id in ["geo-tracker", "satellite-panel", "signal-graph", "biometric", "darknet-monitor", "tunnel-status"]:
            widget = self.query_one(f"#{widget_id}", Static)
            if widget:
                # محاكاة تحديث البيانات عبر الوحدات
                pass

    async def update_network_modules(self):
        # تحديث حالة الشبكات المزيفة
        pass

    async def random_glitch(self):
        import random
        if random.random() < self.config['simulation']['glitch_frequency']:
            await self.glitch.apply_to_screen(self)

    async def update_bloom(self):
        if self.bloom.enabled:
            await self.bloom.apply(self)
