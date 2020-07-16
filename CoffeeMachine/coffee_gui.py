## coffee_gui.py - CoffeeMachine: Taking care of the connection between UI and modules
# GPLv3 (c) 2020 Laurent Bourgon
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
            CoffeeCreator("Regular", {"water": 200, "milk": 20, "beans": 5}, 2),
            CoffeeCreator("Espresso", {"water": 250, "beans": 16}, 4),
            CoffeeCreator("Cappuccino", {"water": 200, "milk": 100, "beans": 12}, 6),
            CoffeeCreator("Latte", {"water": 350, "milk": 75, "beans": 20}, 7),
        ]

        self.window: CoffeeWindow = CoffeeWindow(self.coffees)
        self.window.setWindowTitle(f"CoffeeMachine - {__version__}")

        self.window.show()
