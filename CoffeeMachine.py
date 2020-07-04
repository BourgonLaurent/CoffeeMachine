import sys
from CoffeeMachine import coffee_gui

if __name__ == "__main__":
    app = coffee_gui.CoffeeMachine()
    sys.exit(app.exec_())
