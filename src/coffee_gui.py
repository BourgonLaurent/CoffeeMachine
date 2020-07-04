# coffee_gui.py
# Taking care of the connection between UI and modules

import os
import sys
from typing import List
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtGui import QIntValidator

import coffee_interface_ui

from coffee_creator import CoffeeCreator

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))

VERSION = "v2.0.0b1"


class CoffeeMachine(QApplication):
    """## Tweaked QApplication for CoffeeMachine

    ### Methods:\n
      .exec_() -- Run the instance
    """

    def __init__(self, coffees: List[CoffeeCreator] = None):
        super().__init__()

        self.coffees: List[CoffeeCreator] = coffees if coffees else [
            CoffeeCreator('Regular', {'water': 200, 'milk': 20, 'beans': 5}, 6)]

        self.window: CoffeeWindow = CoffeeWindow(self)

        self.window.show()


class CoffeeWindow(QMainWindow):
    """## Tweak QMainWindow for CoffeeMachine

    ### Attributes:\n
      .ui -- GUI Elements set with Qt Designer
    """

    def __init__(self, parent: CoffeeMachine = None):
        super().__init__()
        self.setWindowTitle(f"CoffeeMachine - {VERSION}")

        self.ui = coffee_interface_ui.Ui_mainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = CoffeeMachine()
    sys.exit(app.exec_())
