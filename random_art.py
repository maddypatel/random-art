import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


class Expression:
    def __init__(self):
        self.functions = []

    def __str__(self):
        return str(self.functions)

    def evaluate(self, x, y):
        value = 2

        for (function, coordinate) in self.functions:
            if function == "sin" and coordinate == "x":
                value *= math.pi * math.sin(math.cos(get_avg(math.sinh(x), get_avg(x, math.tanh(math.e ** 2)))))
            elif function == "sin" and coordinate == "y":
                value *= math.pi * math.sin(math.cos(get_avg(math.sinh(y), get_avg(y, math.tanh(math.e ** 2)))))
            elif function == "cos" and coordinate == "x":
                value *= math.pi * math.cos(math.exp(math.cos(math.tan(math.tan(math.e * x)))))
            elif function == "cos" and coordinate == "y":
                value *= math.pi * math.cos(math.exp(math.cos(math.tan(math.tan(math.e * y)))))
            elif function == "tan" and coordinate == "x":
                value = math.tan(math.tanh(get_avg(math.atan(y), get_avg(y, math.tan(y ** 2)))))
            elif function == "tan" and coordinate == "y":
                value = math.tan(math.tanh(get_avg(math.atan(y), get_avg(y, math.tan(y ** 2)))))

        return value


def get_avg(a, b):
    return (a + b) / 2


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = Expression()
    for _ in range(5):
        if random.random() < 0.33:
            trigfunc = "sin"
        elif random.random() < 0.66:
            trigfunc = "cos"
        else:
            trigfunc = "tan"

        if random.random() > 0.5:
            coordinate = "x"
        else:
            coordinate = "y"

        expr.functions.append([trigfunc, coordinate])
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
