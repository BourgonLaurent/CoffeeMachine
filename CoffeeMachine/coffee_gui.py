## coffee_gui.py - CoffeeMachine
# Taking care of the connection between UI and modules

# Librairies
import os
from typing import List
from PySide2.QtWidgets import QApplication

# Project
from . import __version__
from .coffee_creator import CoffeeCreator
from .coffee_window import CoffeeWindow

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))


class CoffeeMachine(QApplication):
    """## Tweaked QApplication for CoffeeMachine

    ### Methods:\n
    .exec_() -- Run the instance
    """

    def __init__(self, coffees: List[CoffeeCreator] = []):
        super().__init__([])  # Create the app
        self.setStyle("Fusion")  # Set the multi-platform theme

        # Set coffees, if they don't exists, use some defaults
        self.coffees: List[CoffeeCreator] = coffees if coffees else [
            CoffeeCreator("Regular", {"water": 200, "milk": 20, "beans": 5}, 6)
        ]

        self.window: CoffeeWindow = CoffeeWindow(self)
        self.window.setWindowTitle(f"CoffeeMachine - {__version__}")

        self.window.show()
