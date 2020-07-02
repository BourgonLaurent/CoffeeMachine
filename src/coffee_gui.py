### coffee_gui.py
## Taking care of the connection between UI and modules

import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

import coffee_interface_ui

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))

VERSION = "v1.0.0"


class CoffeeMachine(QApplication):
    def __init__(self):
        super().__init__()

        self.window = MainWindow()
        self.window.show()

        sys.exit(self.exec_())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = coffee_interface_ui.Ui_mainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(f"CoffeeMachine - {VERSION}")


if __name__ == "__main__":
    app = CoffeeMachine()
