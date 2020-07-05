# coffee_gui.py
# Taking care of the connection between UI and modules

# Librairies
import os
import sys
from typing import List, Dict
from PySide2.QtWidgets import QApplication, QLineEdit, QMainWindow

# Project
from . import __version__
from .coffee_interface_ui import Ui_mainWindow
from .coffee_creator import CoffeeCreator

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))


class CoffeeMachine(QApplication):
    """## Tweaked QApplication for CoffeeMachine

    ### Methods:\n
    .exec_() -- Run the instance
    """

    def __init__(self, coffees: List[CoffeeCreator] = None):
        # qInitResources()
        super().__init__()

        self.coffees: List[CoffeeCreator] = coffees if coffees else [
            CoffeeCreator("Regular", {"water": 200, "milk": 20, "beans": 5}, 6)
        ]

        self.window: CoffeeWindow = CoffeeWindow(self)
        self.window.setWindowTitle(f"CoffeeMachine - {__version__}")

        self.window.show()


class CoffeeWindow(QMainWindow):
    """## Tweak QMainWindow for CoffeeMachine

    ### Attributes:\n
    .ui -- GUI Elements set with Qt Designer
    """

    def __init__(self, parent: CoffeeMachine):
        super().__init__()

        self.parent: CoffeeMachine = parent

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.current_coffee: CoffeeCreator = self.parent.coffees[0]

        self._enableConnections()

        self.wordToSelector: Dict[str, QLineEdit] = {
            "water": self.ui.waterSelector,
            "milk": self.ui.milkSelector,
            "beans": self.ui.beansSelector,
            "price": self.ui.priceSelector,
        }

        self.ui.coffeeSelectionSvg.load("assets/logo.svg")
        self.ui.waterSelectionSvg.load("assets/faucet-drip.svg")
        self.ui.milkSelectionSvg.load("assets/cow.svg")
        self.ui.beansSelectionSvg.load("assets/coffee-beans.svg")
        self.ui.priceSelectionSvg.load("assets/usd-square.svg")

    def _enableConnections(self):
        self.ui.coffeeSelector.textChanged.connect(self.setFromCoffee)

    def setFromCoffee(self, number_of_coffees: int):
        if not number_of_coffees:
            number_of_coffees = 0

        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["price"] = self.current_coffee.final_cost(number_of_coffees)

        for word, selector in self.wordToSelector.items():
            selector.setText(str(ingredients[word]).zfill(3))
