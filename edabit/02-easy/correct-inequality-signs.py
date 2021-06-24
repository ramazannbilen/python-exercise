"""
Correct Inequality Signs
Create a function that returns True if a given inequality expression is correct and False otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
Notes
N/A
"""

from edabit.Test import Test


def correct_signs(txt):
    return eval(txt)  # eval() converts strings to expression as same as in math


if __name__ == '__main__':
    Test.assert_equals(correct_signs("3 < 7 < 11"), True)
    Test.assert_equals(correct_signs("13 > 44 > 33 > 1"), False)
    Test.assert_equals(correct_signs("1 < 2 < 6 < 9 > 3"), True)
    Test.assert_equals(correct_signs("4 > 3 > 2 > 1"), True)
    Test.assert_equals(correct_signs("5 < 7 > 1"), True)
    Test.assert_equals(correct_signs("5 > 7 > 1"), False)
    Test.assert_equals(correct_signs("9 < 9"), False)
