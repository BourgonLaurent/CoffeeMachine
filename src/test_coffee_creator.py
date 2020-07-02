import unittest
from coffee_creator import CoffeeCreator


class TestCoffeeCreator(unittest.TestCase):
    coffee = CoffeeCreator("Coffee1", {"water": 30, "milk": "25", "cocoa": 5}, 6.00)

    def test_init(self):
        # Test if conversions to string and ints was correct
        self.assertEqual(self.coffee.name, "Coffee1")
        self.assertEqual(self.coffee.ingredients, {"water": 30, "cocoa": 5})
        self.assertEqual(self.coffee.price, 6)

    def test_str(self):
        # Check the string output
        self.assertEqual(
            str(self.coffee), "Coffee1 - 6$:\twater - 30 mL | cocoa - 5 mL"
        )

    def test_final_cost(self):
        # Test if integer works
        self.assertEqual(self.coffee.final_cost(2), 6 * 2)
        # Test if float works
        self.assertEqual(self.coffee.final_cost(3.5), 6 * 3)

    def test_ingredients_needed(self):
        # Test if integer works
        self.assertEqual(
            self.coffee.ingredients_needed(2), {"water": 30 * 2, "cocoa": 5 * 2}
        )
        # Test if float works
        self.assertEqual(
            self.coffee.ingredients_needed(3.5), {"water": 30 * 3, "cocoa": 5 * 3}
        )

    def test_coffees_possible(self):
        # Test if integer works
        self.assertEqual(self.coffee.coffees_possible_ingredient("water", 30 * 2), 2)
        self.assertEqual(self.coffee.coffees_possible_ingredient("cocoa", 5 * 2), 2)
        # Test if float works
        self.assertEqual(self.coffee.coffees_possible_ingredient("water", 30 * 3.5), 3)

    def test_limiting_ingredients(self):
        # Test normally
        self.assertEqual(
            self.coffee.limiting_ingredient({"water": 30, "cocoa": 30}), (1, {"water"})
        )
        # Test if one is under
        self.assertEqual(
            self.coffee.limiting_ingredient({"water": 30, "cocoa": 0}), (0, {"cocoa"})
        )
        # Check if adding something not in the recipe works
        self.assertEqual(
            self.coffee.limiting_ingredient({"water": 30, "milk": 0, "cocoa": 50}),
            (1, {"water"}),
        )
        # Check if balanced recipe works
        self.assertEqual(
            self.coffee.limiting_ingredient({"water": 30, "milk": 0, "cocoa": 5}),
            (1, {"water", "cocoa"}),
        )

