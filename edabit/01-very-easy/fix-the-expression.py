"""
Fix the Expression
Fix the code in the Code tab so the function returns true if and only if x is equal to 7. Try to debug code and pass all the tests.

Examples
is_seven(4) ➞ False

is_seven(9) ➞ False

is_seven(7) ➞ True
Notes
The bug can be hard to find, so look closely!
"""

from edabit.Test import Test


def is_seven(x):
    if x == 7:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(is_seven(4), False)
    Test.assert_equals(is_seven(9), False)
    Test.assert_equals(is_seven(7), True)
    Test.assert_equals(is_seven(10), False)
    Test.assert_equals(is_seven(20), False)
    Test.assert_equals(is_seven(7), True)
