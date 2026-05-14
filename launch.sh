#!/bin/bash
if [ ! -d "venv" ]; then
    echo "[!] البيئة الافتراضية غير موجودة. قم بتشغيل ./setup.sh أولاً"
    exit 1
fi
source venv/bin/activate
clear
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     تشغيل محاكاة الطرفية الإلكترونية العسكرية            ║"
echo "╚═══════════════════════════════════════════════════════════╝"
sleep 2
python3 main.py
deactivate
