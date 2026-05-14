#!/usr/bin/env python3
"""
KALI CYBER INTELLIGENCE TERMINAL – ULTRA CINEMATIC EDITION
Classification: [TOP SECRET // NOFORN // CYBERCOM // OMEGA]
Purpose: Visual simulation only – no actual hacking
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.engine import CyberIntelligenceEngine
from core.config import load_config


async def main():
    # إخفاء المؤشر وتنظيف الشاشة
    print("\033[?25l\033[2J\033[H")
    config = load_config()
    engine = CyberIntelligenceEngine(config)
    try:
        await engine.run()
    except KeyboardInterrupt:
        print("\033[?25h\033[2J\033[H")
        print("\n[SYSTEM SHUTDOWN] تم إنهاء الجلسة بأمر المشغل.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
