class AudioEngine:
    def __init__(self, config):
        self.enabled = config.get('audio', {}).get('enabled', False)

    async def play_startup(self):
        pass

    async def play_ambiance(self):
        pass

    async def play_glitch(self):
        pass
