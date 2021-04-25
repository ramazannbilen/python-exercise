"""Two Makes Ten
Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.

Examples
makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True
Notes
Don't forget to return the result.
"""

from edabit.Test import Test


def makes10(a, b):
    """ This Method calculates in params!.. """
    if a or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(makes10(9, 10), True)
    Test.assert_equals(makes10(9, 9), False)
    Test.assert_equals(makes10(1, 9), True)
    Test.assert_equals(makes10(10, 1), True)
    Test.assert_equals(makes10(10, 10), True)
    Test.assert_equals(makes10(8, 2), True)
    Test.assert_equals(makes10(8, 3), False)
    Test.assert_equals(makes10(10, 42), True)
    Test.assert_equals(makes10(12, -2), True)
