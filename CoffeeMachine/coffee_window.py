# coffee_window.py
# Main Window of coffee_gui

# Librairies
from typing import Dict
from PySide2.QtWidgets import QCheckBox, QLineEdit, QMainWindow, QLabel
from PySide2.QtCore import Slot

# Project
from .coffee_window_ui import Ui_mainWindow
from .coffee_creator import CoffeeCreator
from .coffee_lang import STATUS_EXCEEDING, STATUS_LIMITING, WORDS


class CoffeeWindow(QMainWindow):
    """## Tweak QMainWindow for CoffeeMachine

    ### Attributes:\n
    .ui -- GUI Elements set with Qt Designer
    """

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

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
        self.wordToStatus: Dict[str, QLabel] = {
            "coffee": self.ui.coffeeStatusLabel,
            "water": self.ui.waterStatusLabel,
            "milk": self.ui.milkStatusLabel,
            "beans": self.ui.beansStatusLabel,
            "price": self.ui.priceStatusLabel,
        }

        self._loadSVG()
        self._setLang()
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

    def checkAndSetExceeding(self, word: str, value: int):
        print(
            f"{len(str(value))} > {len(str(self.wordToSelector[word].inputMask()))} ({self.wordToSelector[word].inputMask()})"
        )
        if len(str(value)) > len(str(self.wordToSelector[word].inputMask())):
            self.wordToStatus[word].setText(STATUS_EXCEEDING)

        self.wordToSelector[word].setText(str(value))

    @Slot()  # type: ignore
    def setFromCoffee(self, number_of_coffees: int):
        self.cleanup()
        if not number_of_coffees:
            number_of_coffees = 0

        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["price"] = self.current_coffee.final_cost(number_of_coffees)

        for word, selector in self.wordToSelector.items():
            if not word == "coffee":
                self.checkAndSetExceeding(word, ingredients[word])

        for word, checkbox in self.wordToInfinity.items():
            checkbox.setCheckable(True)
            checkbox.setChecked(not word == "coffee")

    @Slot()  # type: ignore
    def setFromIngredients(self, ingredient_changed: str = "", component: str = ""):
        print(ingredient_changed, component)

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
                self.checkAndSetExceeding(ingredient, min_ingredient[ingredient])
                # self.wordToSelector[ingredient].setText(str(min_ingredient[ingredient]))
            else:
                for limiting_ingredient in limited_coffees[1]:
                    self.wordToStatus[limiting_ingredient].setText(STATUS_LIMITING)

        self.checkAndSetExceeding("coffee", limited_coffees[0])
        self.checkAndSetExceeding("price", cost)

        # self.wordToSelector["coffee"].setText(str(limited_coffees[0]))
        # self.wordToSelector["price"].setText(str(cost))

        for word, selector in self.wordToInfinity.items():
            if word not in ("water", "milk", "beans"):
                selector.setChecked(True)

    @Slot()  # type: ignore
    def setFromPrice(self, money: int):
        self.cleanup()
        if not money:
            money = 0

        number_of_coffees = self.current_coffee.coffees_possible_cost(money)
        ingredients = self.current_coffee.ingredients_needed(number_of_coffees)
        ingredients["coffee"] = number_of_coffees
        for word, selector in self.wordToSelector.items():
            if word == "coffee":
                selector.setText(str(ingredients.get(word, 0)))
            elif not word == "price":
                selector.setText(str(ingredients.get(word, 0)))

        for word, checkbox in self.wordToInfinity.items():
            checkbox.setCheckable(True)
            checkbox.setChecked(not word == "price")

