"""
Return the Factorial
Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

Examples
factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800
Notes
Assume all inputs are greater than or equal to 0.
"""

from edabit.Test import Test


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

if __name__ == '__main__':
    Test.assert_equals(factorial(2), 2)
    Test.assert_equals(factorial(6), 720)
    Test.assert_equals(factorial(3), 6)
    Test.assert_equals(factorial(12), 479001600)
    Test.assert_equals(factorial(5), 120)
