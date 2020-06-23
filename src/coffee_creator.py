### COFFEE CREATOR
## CREATE A COFFEE

class Coffee:
    def __init__(self, name: str, ingredients: dict, price: int):
        self.name = str(name)
        self.ingredients = {ingredient: int(amount) for ingredient, amount in ingredients.items() if isinstance(amount, int)}
        self.price = int(price)
    
    def __str__(self):
        return f"{self.name} - {self.price}$:\t{' | '.join([f'{ingredient} - {amount} mL' for ingredient, amount in self.ingredients.items()])}"
    
    def final_cost(self, number_of_coffees: int):
        return self.price * int(number_of_coffees)
    
    def ingredients_needed(self, number_of_coffees: int):
        return {ingredient: amount * int(number_of_coffees) for ingredient, amount in self.ingredients.items()}
    
    def coffees_possible_cost(self, price: int):
        return int(price) // self.price

    def coffees_possible_ingredient(self, ingredient: str, amount: int):
        return int(amount) // self.ingredients.get(ingredient)

    def limiting_ingredient(self, limited_ingredients: dict):
        amount_of_coffees = {ingredient: self.coffees_possible_ingredient(ingredient, amount) for ingredient, amount in limited_ingredients.items() if ingredient in self.ingredients}

        possible_ingredients = {}
        for ingredient, amount in amount_of_coffees.items():
            possible_ingredients.setdefault(amount, set()).update([ingredient])
        max_possible = min(possible_ingredients.keys())

        return {max_possible: possible_ingredients[max_possible]}

if __name__ == "__main__":
    regular = Coffee('Regular', {'water': 200, 'milk': 20, 'cocoa': 5}, 6)

    print(regular)
    regular.limiting_ingredient({'water': 200, 'milk': 20})