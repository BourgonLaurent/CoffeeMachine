# coffee_gui.py
# Taking care of the connection between UI and modules

# Librairies
import os
from typing import List, Dict
from PySide2.QtWidgets import QApplication, QCheckBox, QLineEdit, QMainWindow

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
        self.wordToSelector: Dict[str, QLineEdit] = {
            "coffee": self.ui.coffeeSelector,
            "water": self.ui.waterSelector,
            "milk": self.ui.milkSelector,
            "beans": self.ui.beansSelector,
            "price": self.ui.priceSelector,
        }
        self.wordToInfinity: Dict[str, QCheckBox] = {
            "coffee": self.ui.coffeeInfinityCheckBox,
            "water": self.ui.waterInfinityCheckBox,
            "milk": self.ui.milkInfinityCheckBox,
            "beans": self.ui.beansInfinityCheckBox,
            "price": self.ui.priceInfinityCheckBox,
        }

        self._loadSVG()
        self._enableConnections()
        self.setFromCoffee(1)

    def _loadSVG(self):
        for svg, asset in {
            self.ui.coffeeSelectionSvg: "assets/logo.svg",
            self.ui.waterSelectionSvg: "assets/faucet-drip.svg",
            self.ui.milkSelectionSvg: "assets/cow.svg",
            self.ui.beansSelectionSvg: "assets/coffee-beans.svg",
            self.ui.priceSelectionSvg: "assets/usd-square.svg",
        }.items():
            svg.load(asset)

    def _enableConnections(self):
        self.ui.coffeeSelector.textEdited.connect(self.setFromCoffee)

        self.ui.waterSelector.textEdited.connect(self.setFromIngredients)
        self.ui.milkSelector.textEdited.connect(self.setFromIngredients)
        self.ui.beansSelector.textEdited.connect(self.setFromIngredients)

        self.ui.priceSelector.textEdited.connect(self.setFromPrice)

    def setFromCoffee(self, number_of_coffees: int):
        if not number_of_coffees:
            number_of_coffees = 0

        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["price"] = self.current_coffee.final_cost(number_of_coffees)

        for word, selector in self.wordToSelector.items():
            if word == "price":
                selector.setText(str(ingredients[word]))
            elif not word == "coffee":
                selector.setText(str(ingredients[word]))

        for word, checkbox in self.wordToInfinity.items():
            checkbox.setChecked(not word == "coffee")

    def setFromIngredients(self):
        pass

    def setFromPrice(self, money: int):
        if not money:
            money = 0

        number_of_coffees = self.current_coffee.coffees_possible_cost(money)
        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["coffee"] = number_of_coffees
        for word, selector in self.wordToSelector.items():
            if word == "coffee":
                selector.setText(str(ingredients[word]))
            elif not word == "price":
                selector.setText(str(ingredients[word]))

        for word, checkbox in self.wordToInfinity.items():
            checkbox.setChecked(not word == "price")
