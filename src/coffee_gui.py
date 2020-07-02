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
    """## Tweaked QApplication for CoffeeMachine
    
    ### Methods:\n
      .exec_() -- Run the instance
    """

    def __init__(self):
        super().__init__()

        self.window = CoffeeWindow()
        self.ui = self.window.ui

        self.window.show()


class CoffeeWindow(QMainWindow):
    """## Tweak QMainWindow for CoffeeMachine
    
    ### Attributes:\n
      .ui -- GUI Elements set with Qt Designer
    """

    def __init__(self):
        super().__init__()

        self.ui = coffee_interface_ui.Ui_mainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(f"CoffeeMachine - {VERSION}")


if __name__ == "__main__":
    app = CoffeeMachine()
    sys.exit(app.exec_())
