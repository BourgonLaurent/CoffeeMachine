# coffee_creator.py
# CREATE A COFFEE


class Coffee:
    """## Basic Coffee Class

    ### Arguments:\n
        \tname {str} -- Name of the coffee
        \tingredients {dict} -- Dictionary of the ingredients in format {ingredients: amount}
        \tprice {int} -- Price of the coffee
    """

    def __init__(self, name: str, ingredients: dict, price: int):
        self.name = str(name)
        self.ingredients = {
            ingredient: int(amount)
            for ingredient, amount in ingredients.items()
            if isinstance(amount, int)
        }
        self.price = int(price)

    def __str__(self) -> str:
        return f"{self.name} - {self.price}$:\t{' | '.join([f'{ingredient} - {amount} mL' for ingredient, amount in self.ingredients.items()])}"


class CoffeeCreator(Coffee):
    """## `Coffee` Sub-Class with Additional Features

    ### Arguments:\n
        \tname {str} -- Name of the coffee
        \tingredients {dict} -- Dictionary of the ingredients in format {ingredient: amount}
        \tprice {int} -- Price of the coffee
    """

    def __init__(self, name: str, ingredients: dict, price: int):
        super().__init__(name, ingredients, price)

    def final_cost(self, number_of_coffees: int) -> int:
        """Return the total price of the number of coffees specified"""
        return self.price * int(number_of_coffees)

    def ingredients_needed(self, number_of_coffees: int) -> dict:
        """Return how many ingredients will be needed for the number of coffees specified"""
        return {
            ingredient: amount * int(number_of_coffees)
            for ingredient, amount in self.ingredients.items()
        }

    def coffees_possible_cost(self, price: int) -> int:
        """Return the maximum number of coffees you could get for a certain price"""
        return int(price) // self.price

    def coffees_possible_ingredient(self, ingredient: str, amount: int) -> int:
        """Return the maximum number of coffees you could make for one ingredient"""
        return int(amount) // self.ingredients.get(ingredient)

    def limiting_ingredient(self, limited_ingredients: dict) -> tuple:
        """## Return the maximum number of coffees you can make

        ### Arguments:\n
            \tlimitedingredients {dict} -- Dictionary of ingredients in format {ingredient: amount}

        ### Returns:\n
            \t{tuple} -- 0 {int}: Maximum number of coffees - 1 {set}: Limiters
        """
        amount_of_coffees = {
            ingredient: self.coffees_possible_ingredient(ingredient, amount)
            for ingredient, amount in limited_ingredients.items()
            if ingredient in self.ingredients
        }

        possible_ingredients = {}
        for ingredient, amount in amount_of_coffees.items():
            possible_ingredients.setdefault(amount, set()).update([ingredient])
        max_possible = min(possible_ingredients.keys())

        return (max_possible, possible_ingredients[max_possible])
