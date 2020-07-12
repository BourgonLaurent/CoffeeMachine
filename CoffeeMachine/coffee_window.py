## coffee_window.py - CoffeeMachine
# Main Window of coffee_gui

# Librairies
from typing import Dict, List
from PySide2.QtWidgets import QMainWindow, QLabel

# Project
from .ui.coffee_window_ui import Ui_mainWindow
from .coffee_creator import CoffeeCreator
from .coffee_lang import STATUS_LIMITING, WORDS, ICONS
from .ui.IngredientWidgets import IngredientInfinity, IngredientSelector
from .ui.coffee_customize_dialog import CoffeeCustomizeDialog


class CoffeeWindow(QMainWindow):
    """## Tweak QMainWindow for CoffeeMachine

    ### Attributes:\n
    .ui -- GUI Elements set with Qt Designer
    """

    def __init__(self, coffees: List[CoffeeCreator]):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.coffeeSelectionLabel.dialog.current_coffee = coffees[0]
        self.ui.coffeeSelectionLabel.dialog.coffees = coffees
        self.ui.coffeeSelectionLabel.dialog.label = self.ui.coffeeSelectionLabel

        self.current_coffee = self.ui.coffeeSelectionLabel.dialog.current_coffee

        self._setDefinitions()
        self._loadSVG()
        self._setLang()
        self._enableConnections()

        self.setFromCoffee(1)

    def _setDefinitions(self):
        self.wordToSelector: Dict[str, IngredientSelector] = {
            "coffee": self.ui.coffeeSelector,
            "water": self.ui.waterSelector,
            "milk": self.ui.milkSelector,
            "beans": self.ui.beansSelector,
            "price": self.ui.priceSelector,
        }
        self.wordToInfinity: Dict[str, IngredientInfinity] = {
            "coffee": self.ui.coffeeInfinityCheckBox,
            "water": self.ui.waterInfinityCheckBox,
            "milk": self.ui.milkInfinityCheckBox,
            "beans": self.ui.beansInfinityCheckBox,
            "price": self.ui.priceInfinityCheckBox,
        }
        self.wordToStatus: Dict[str, QLabel] = {
            "coffee": self.ui.coffeeStatusLabel,
            "water": self.ui.waterStatusLabel,
            "milk": self.ui.milkStatusLabel,
            "beans": self.ui.beansStatusLabel,
            "price": self.ui.priceStatusLabel,
        }

    def _loadSVG(self):
        for svg, asset in {
            self.ui.coffeeSelectionSvg: ICONS["coffee"],
            self.ui.waterSelectionSvg: ICONS["water"],
            self.ui.milkSelectionSvg: ICONS["milk"],
            self.ui.beansSelectionSvg: ICONS["beans"],
            self.ui.priceSelectionSvg: ICONS["price"],
        }.items():
            svg.load(asset)

    def _setLang(self):
        wordToSuffix: Dict[str, QLabel] = {
            "coffee": self.ui.coffeeSelectorSuffix,
            "water": self.ui.waterSelectorSuffix,
            "milk": self.ui.milkSelectorSuffix,
            "beans": self.ui.beansSelectorSuffix,
            "price": self.ui.priceSelectorSuffix,
        }
        for word, lang in WORDS.items():
            wordToSuffix[word].setText(lang)

    def _enableConnections(self):
        self.ui.coffeeSelector.textEdited.connect(self.setFromCoffee)

        self.ui.waterSelector.textEdited.connect(
            lambda: self.setFromIngredients("water", "lineedit")
        )
        self.ui.milkSelector.textEdited.connect(
            lambda: self.setFromIngredients("milk", "lineedit")
        )
        self.ui.beansSelector.textEdited.connect(
            lambda: self.setFromIngredients("beans", "lineedit")
        )

        self.ui.waterInfinityCheckBox.clicked.connect(
            lambda: self.setFromIngredients("water", "checkbox")
        )
        self.ui.milkInfinityCheckBox.clicked.connect(
            lambda: self.setFromIngredients("milk", "checkbox")
        )
        self.ui.beansInfinityCheckBox.clicked.connect(
            lambda: self.setFromIngredients("beans", "checkbox")
        )

        self.ui.priceSelector.textEdited.connect(self.setFromPrice)

    def cleanup(self):
        for label in self.wordToStatus.values():
            label.setText("")

    def setFromCoffee(self, number_of_coffees: int):
        self.cleanup()
        if not number_of_coffees:
            number_of_coffees = 0

        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["price"] = self.current_coffee.final_cost(number_of_coffees)

        for word, selector in self.wordToSelector.items():
            if not word == "coffee":
                selector.setSafeText(ingredients[word])

        for word, checkbox in self.wordToInfinity.items():
            checkbox.setCheckable(True)
            checkbox.setChecked(not word == "coffee")

    def setFromIngredients(self, ingredient_changed: str = "", component: str = ""):
        self.cleanup()
        if ingredient_changed and component == "lineedit":
            self.wordToInfinity[ingredient_changed].setChecked(False)

        limited_ingredients: Dict[str, int] = dict()

        for word, selector in self.wordToSelector.items():
            if word not in ("coffee", "price"):
                s_text = selector.text().strip()
                limited_ingredients[word] = int(s_text if s_text else 0)

        infinity_checked = {
            word: checkbox.isChecked()
            for word, checkbox in self.wordToInfinity.items()
            if word not in ("coffee", "price")
        }

        limited = {
            word: isChecked
            for word, isChecked in infinity_checked.items()
            if not isChecked
        }

        if len(limited) < 1:
            for infinity in self.wordToInfinity.values():
                infinity.setCheckable(True)
            self.wordToInfinity[ingredient_changed].setCheckable(False)

        for word in limited_ingredients:
            if infinity_checked[word]:
                limited_ingredients[word] = -1

        limited_coffees = self.current_coffee.limiting_ingredient(limited_ingredients)
        min_ingredient = self.current_coffee.ingredients_needed(limited_coffees[0])
        cost = self.current_coffee.final_cost(limited_coffees[0])

        for ingredient, isChecked in infinity_checked.items():
            if isChecked:
                self.wordToSelector[ingredient].setSafeText(min_ingredient[ingredient])
            else:
                for limiting_ingredient in limited_coffees[1]:
                    self.wordToStatus[limiting_ingredient].setText(STATUS_LIMITING)

        self.ui.coffeeSelector.setSafeText(limited_coffees[0])
        self.ui.priceSelector.setSafeText(cost)

        for word, selector in self.wordToInfinity.items():
            if word not in ("water", "milk", "beans"):
                selector.setChecked(True)

    def setFromPrice(self, money: int):
        self.cleanup()
        if not money:
            money = 0

        number_of_coffees = self.current_coffee.coffees_possible_cost(money)
        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["coffee"] = number_of_coffees
        for word, selector in self.wordToSelector.items():
            if word != "price":
                selector.setSafeText(ingredients.get(word, 0))

        for word, checkbox in self.wordToInfinity.items():
            checkbox.setCheckable(True)
            checkbox.setChecked(not word == "price")
