# coffee_lang.py
# Language and words used by CoffeeMachine

UNITS_MILLILITERS = "mL"
UNITS_GRAMS = "g"
UNITS_CUPS = "cups"

WORDS = {
    "coffee": f"coffees",
    "water": f"{UNITS_MILLILITERS} of water",
    "milk": f"{UNITS_GRAMS} of milk",
    "beans": f"{UNITS_GRAMS} of beans",
    "price": "$",
}

STATUS_EXCEEDING = "Error: Value overflow"
STATUS_LIMITING = "Limiting"


ICONS = {
    "coffee": "ui/assets/logo.svg",
    "water": "ui/assets/faucet-drip.svg",
    "milk": "ui/assets/cow.svg",
    "beans": "ui/assets/coffee-beans.svg",
    "price": "ui/assets/usd-square.svg",
}
