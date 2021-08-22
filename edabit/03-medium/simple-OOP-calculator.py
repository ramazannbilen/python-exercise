"""
Simple OOP Calculator
Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.
Examples
calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2
Notes
The methods should return the result of the calculation.
Don't worry about needing to handle division by zero errors.
See the Resources tab for some helpful tutorials on Python classes.
"""

from edabit.Test import Test


class Calculator:
    # Write methods to add(), subtract(), multiply() and divide()
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


if __name__ == '__main__':
    calculator = Calculator()
    Test.assert_equals(calculator.add(5, 5), 10)
    Test.assert_equals(calculator.add(20, 5), 25)
    Test.assert_equals(calculator.subtract(30, 5), 25)
    Test.assert_equals(calculator.subtract(100, 5), 95)
    Test.assert_equals(calculator.multiply(5, 5), 25)
    Test.assert_equals(calculator.multiply(100, 5), 500)
    Test.assert_equals(calculator.divide(10, 5), 2)
    Test.assert_equals(calculator.divide(100, 5), 20)
