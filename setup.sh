#!/bin/bash
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     KALI CYBER INTELLIGENCE TERMINAL - SETUP              ║"
echo "║     CLASSIFIED SIMULATION - NO REAL FUNCTIONALITY         ║"
echo "╚═══════════════════════════════════════════════════════════╝"

if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 غير موجود. قم بتثبيت Python 3.8+"
    exit 1
fi

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
mkdir -p logs
chmod +x launch.sh
echo "[✓] اكتمل الإعداد. قم بتشغيل ./launch.sh"
