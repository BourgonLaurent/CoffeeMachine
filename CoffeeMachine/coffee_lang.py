## coffee_lang.py - CoffeeMachine
# Language and words used by CoffeeMachine

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
