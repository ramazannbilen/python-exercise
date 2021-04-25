"""
Proper Modulo Operator
Create a function which returns the Modulo of the two given numbers.

Examples
mod(-13, 64) ➞ 51

mod(50, 25) ➞ 0

mod(-6, 3) ➞ 0
Notes
All test cases contain valid numbers.
"""

from edabit.Test import Test


def mod(m, n):
    return m % n


if __name__ == '__main__':
    Test.assert_equals(mod(-13, 64), 51)
    Test.assert_equals(mod(50, 25), 0)
    Test.assert_equals(mod(-6, 3), 0)
    Test.assert_equals(mod(-45, 2), 1)
