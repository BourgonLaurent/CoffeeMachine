## coffee_customize_dialog.py - CoffeeMachine.ui
# Dialog to select the coffee types

from typing import List, Dict
from PySide2.QtWidgets import QDialog, QListWidgetItem, QLabel
from PySide2.QtCore import Qt

from ..coffee_lang import ICONS, WORDS
from ..coffee_creator import CoffeeCreator
from .coffee_customize_dialog_ui import Ui_coffeeSelectionDialog


class CoffeeCustomizeDialog(QDialog):
    coffees: List[CoffeeCreator]
    current_coffee: CoffeeCreator
    label: QLabel
    setFromCoffee = lambda x: x

    def __init__(self):
        super().__init__()
        self.ui = Ui_coffeeSelectionDialog()
        self.ui.setupUi(self)

        self.ui.coffeeListWidget.setFocusPolicy(Qt.NoFocus)  # type: ignore
        self.ui.coffeeListWidget.itemSelectionChanged.connect(self.selectionChanged)  # type: ignore

        self.wordToLabel: Dict[str, QLabel] = {
            "water": self.ui.waterLabel,
            "milk": self.ui.milkLabel,
            "beans": self.ui.beansLabel,
            "price": self.ui.priceLabel,
        }

        self._loadSvg()

    def _loadSvg(self):
        for svg, icon in {
            self.ui.waterSvg: ICONS["water"],
            self.ui.milkSvg: ICONS["milk"],
            self.ui.beansSvg: ICONS["beans"],
            self.ui.priceSvg: ICONS["price"],
        }.items():
            svg.load(icon)

    def selectionChanged(self):
        current_coffee_item = self.ui.coffeeListWidget.currentItem()

        if not current_coffee_item:
            return

        for coffee in self.coffees:
            if coffee.name == current_coffee_item.text():
                self.current_coffee = coffee
                break

        values = {
            **self.current_coffee.ingredients,
            "price": self.current_coffee.price,
        }

        for word, label in self.wordToLabel.items():
            label.setText(f"{values.get(word, 0)} {WORDS[word]}")

        self.label.setText(self.current_coffee.name)
        self.setFromCoffee(1)

    def openDialog(self):
        self.ui.coffeeListWidget.clear()

        self.ui.coffeeListWidget.addItems([c.name for c in self.coffees])

        current_coffee_item: QListWidgetItem = self.ui.coffeeListWidget.findItems(self.current_coffee.name, Qt.MatchExactly)[0]  # type: ignore
        self.ui.coffeeListWidget.setItemSelected(current_coffee_item, True)

        self.exec_()
