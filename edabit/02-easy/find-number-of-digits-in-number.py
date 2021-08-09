"""
Find Number of Digits in Number
Create a function that will return an integer number corresponding to the amount of digits in the given integer num.

Examples
num_of_digits(1000) ➞ 4

num_of_digits(12) ➞ 2

num_of_digits(1305981031) ➞ 10

num_of_digits(0) ➞ 1
Notes
Try to solve this challenge without using strings!
"""

from edabit.Test import Test


def num_of_digits(num):
    return len(str(abs(num)))


if __name__ == '__main__':
    Test.assert_equals(num_of_digits(13124), 5)
    Test.assert_equals(num_of_digits(0), 1)
    Test.assert_equals(num_of_digits(-12381428), 8)
    Test.assert_equals(num_of_digits(12), 2)
    Test.assert_equals(num_of_digits(42), 2)
    Test.assert_equals(num_of_digits(1000), 4)
    Test.assert_equals(num_of_digits(136), 3)
    Test.assert_equals(num_of_digits(1000000000), 10)
    Test.assert_equals(num_of_digits(2147483647), 10)
    Test.assert_equals(num_of_digits(-2147483647), 10)
