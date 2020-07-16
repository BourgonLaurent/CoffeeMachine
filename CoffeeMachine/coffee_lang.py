## coffee_lang.py - CoffeeMachine: Language and words used by CoffeeMachine
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

from typing import Dict

UNITS_MILLILITERS: str = "mL"
UNITS_GRAMS: str = "g"
UNITS_CUPS: str = "cups"
UNITS_CURRENCY: str = "$"

WORDS: Dict[str, str] = {
    "coffee": f"coffees",
    "water": f"{UNITS_MILLILITERS} of water",
    "milk": f"{UNITS_MILLILITERS} of milk",
    "beans": f"{UNITS_GRAMS} of beans",
    "price": f"{UNITS_CURRENCY}",
}

STATUS_EXCEEDING: str = "Error: Value overflow"
STATUS_LIMITING: str = "Limiting"


ICONS: Dict[str, str] = {
    "coffee": "ui/assets/logo.svg",
    "water": "ui/assets/faucet-drip.svg",
    "milk": "ui/assets/cow.svg",
    "beans": "ui/assets/coffee-beans.svg",
    "price": "ui/assets/usd-square.svg",
}
