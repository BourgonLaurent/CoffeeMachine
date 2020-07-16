## CoffeeMachine.py: Launch CoffeeMachine with default coffees
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

from CoffeeMachine.coffee_creator import CoffeeCreator
import sys
from CoffeeMachine import coffee_gui

if __name__ == "__main__":
    app = coffee_gui.CoffeeMachine()
    sys.exit(app.exec_())
