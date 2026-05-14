import yaml
from pathlib import Path

def load_config(config_path="config.yaml"):
    if not Path(config_path).exists():
        return {
            "system": {"name": "CITADEL-CORE", "version": "7.6.2-ALPHA"},
            "themes": {"active": "crimson"},
            "simulation": {"radar_speed": 2.5, "matrix_rain_speed": 0.05,
                           "telemetry_update_rate": 0.3, "glitch_frequency": 0.15},
            "display": {"fullscreen": True, "fps": 30},
            "audio": {"enabled": False},
            "fake_modules": {"darknet_relays": 7, "satellite_links": 3,
                             "quantum_encryption_layers": 5, "active_threats": 12}
        }
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
