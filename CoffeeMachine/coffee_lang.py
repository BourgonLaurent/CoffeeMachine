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
