"""
Basic Calculator
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
Notes
If the input tries to divide by 0, return: "Can't divide by 0!"
"""

from edabit.Test import Test

def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2


if __name__ == '__main__':
    Test.assert_equals(calculator(2, '/', 2), 1)
    Test.assert_equals(calculator(10, '-', 7), 3)
    Test.assert_equals(calculator(2, '*', 16), 32)
    Test.assert_equals(calculator(2, '-', 2), 0)
    Test.assert_equals(calculator(15, '+', 26), 41)
    Test.assert_equals(calculator(2, '+', 2), 4)
    Test.assert_equals(calculator(2, "/", 0), "Can't divide by 0!")
