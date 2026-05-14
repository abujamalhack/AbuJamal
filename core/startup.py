import asyncio
import random
from rich.text import Text
from rich.panel import Panel
from assets.ascii_art import OMEGA_LOGO, DIGITAL_SKULL_LARGE

async def cinematic_boot_sequence(console, glitch, scanlines, bloom, pulse):
    """تسلسل بدء تشغيل سينمائي طويل ومبهر"""
    # 1. وميض RGB و glitch
    await glitch.fullscreen_glitch(console)
    await asyncio.sleep(0.3)
    
    # 2. شعار OMEGA العملاق
    console.clear()
    console.print(Text(OMEGA_LOGO, style="bold red"), justify="center")
    await asyncio.sleep(1.5)
    
    # 3. خطوط المسح الضوئي
    await scanlines.sweep(console)
    
    # 4. تدفقات مشفرة عشوائية
    for _ in range(5):
        console.print(f"[magenta]>>> 0x{random.randint(1000,9999):04X}  ::  {random.randint(100000,999999)}  ENCRYPTED[/magenta]")
        await asyncio.sleep(0.2)
    
    # 5. تهيئة الذكاء الاصطناعي
    console.print("\n[bold cyan]INITIALIZING AI CORE...[/]")
    for i in range(1, 101, 10):
        console.print(f"[cyan]► QUANTUM NEURAL NETWORK: {i}%[/]", end="\r")
        await asyncio.sleep(0.05)
    console.print("\n[green]✓ AI CORE ONLINE[/]")
    await asyncio.sleep(0.8)
    
    # 6. المصادقة المشفرة المزيفة
    console.print("[bold red]⚠️ CLASSIFIED AUTHENTICATION REQUIRED ⚠️[/]")
    await asyncio.sleep(1)
    console.print("[yellow]🔑 BIOMETRIC SCAN: PASSED[/]")
    await asyncio.sleep(0.5)
    console.print("[yellow]🖥️ RETINAL SCAN: CLEARED[/]")
    await asyncio.sleep(0.5)
    console.print("[green]✅ OMEGA ACCESS GRANTED[/]")
    await asyncio.sleep(1)
    
    # 7. تأثير النبض والوميض
    await pulse.red_pulse(console)
    
    # 8. جمجمة رقمية متحركة
    console.print(Text(DIGITAL_SKULL_LARGE, style="bold magenta"), justify="center")
    await asyncio.sleep(1.5)
    
    # 9. شريط التحميل التكتيكي
    for width in range(10, 81, 5):
        bar = "█" * (width//2) + "░" * (40 - width//2)
        console.print(f"[red]LOADING TACTICAL OVERLAYS [{bar}] {width*1.25:.0f}%[/]", end="\r")
        await asyncio.sleep(0.05)
    console.print("\n[green]✓ ALL SYSTEMS OPERATIONAL[/]")
    await asyncio.sleep(1)
    
    # 10. تأثيرات البلوم والإضاءة
    await bloom.apply(console)
    
    console.clear()
    console.print(Panel("[bold red]SYSTEM READY[/]", border_style="red"))
    await asyncio.sleep(1.2)
