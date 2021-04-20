"""
Create a function that takes two numbers as arguments and return their sum.

Examples
addition(3, 2) ➞ 5

addition(-3, -6) ➞ -9

addition(7, 3) ➞ 10
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""

from edabit.Test import Test


def addition(a, b):
    return a + b


if __name__ == '__main__':
    Test.assert_equals(addition(2, 3), 5)
    Test.assert_equals(addition(-3, -6), -9)
    Test.assert_equals(addition(7, 3), 10)
