from themes.themes import THEMES

class ThemeManager:
    def __init__(self, config):
        self.active = config['themes']['active']
    def get_active_theme(self):
        return THEMES.get(self.active, THEMES['crimson'])
