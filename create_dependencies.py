from os import chdir, path
from subprocess import CompletedProcess, run
from typing import Dict, List, Text

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
chdir(path.realpath(__file__).replace(path.basename(__file__), ""))

BASE_FOLDER: Text = path.join("./", "CoffeeMachine", "ui")
FILES: List[str] = ["window", "customize_dialog"]
SUCCESS: Dict[str, Dict[str, CompletedProcess]] = {"qrc": {}, "ui": {}}

for f in FILES:
    qrc: Text = path.join(BASE_FOLDER, f"coffee_{f}_resources.qrc")
    qrc_py: Text = path.join(BASE_FOLDER, f"coffee_{f}_resources_rc.py")
    if path.exists(qrc):
        SUCCESS["qrc"][f] = run(["pyside2-rcc", qrc, "-o", qrc_py,])

    ui: Text = path.join(BASE_FOLDER, f"coffee_{f}_ui.ui")
    ui_py: Text = path.join(BASE_FOLDER, f"coffee_{f}_ui.py")
    if path.exists(ui):
        SUCCESS["ui"][f] = run(["pyside2-uic", ui, "--from-imports", "-o", ui_py,])

for tool, success_dict in SUCCESS.items():
    print(f"[+] {tool}:")
    for f, cmd in success_dict.items():
        if not cmd.returncode:
            print(f"\t[+] {cmd.args[-1]}")
