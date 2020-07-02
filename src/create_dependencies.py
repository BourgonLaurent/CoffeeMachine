import sys
import os
import subprocess

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))

qrc = subprocess.run(
    [
        "pyside2-rcc",
        "coffee_interface_resources.qrc",
        "-o",
        "coffee_interface_resources_rc.py",
    ]
)

ui = subprocess.run(
    ["pyside2-uic", "coffee_interface_ui.ui", "-o", "coffee_interface_ui.py"]
)

for cmd in (qrc, ui):
    if not cmd.returncode:  # Success
        print(f"[x] {cmd.args[-1]} created")
