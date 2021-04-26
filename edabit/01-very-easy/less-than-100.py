"""
Less Than 100?
Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.

Examples
less_than_100(22, 15) ➞ True
# 22 + 15 = 37

less_than_100(83, 34) ➞ False
# 83 + 34 = 117

less_than_100(3, 77) ➞ true
"""

from edabit.Test import Test


def less_than_100(a, b):
    if a + b < 100:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(less_than_100(5, 57), True)
    Test.assert_equals(less_than_100(77, 30), False)
    Test.assert_equals(less_than_100(0, 59), True)
    Test.assert_equals(less_than_100(78, 35), False)
    Test.assert_equals(less_than_100(63, 11), True)
    Test.assert_equals(less_than_100(37, 99), False)
    Test.assert_equals(less_than_100(52, 11), True)
    Test.assert_equals(less_than_100(82, 95), False)
    Test.assert_equals(less_than_100(17, 44), True)
    Test.assert_equals(less_than_100(74, 53), False)
    Test.assert_equals(less_than_100(3, 77), True)
    Test.assert_equals(less_than_100(25, 80), False)
    Test.assert_equals(less_than_100(59, 28), True)
    Test.assert_equals(less_than_100(69, 87), False)
    Test.assert_equals(less_than_100(10, 45), True)
    Test.assert_equals(less_than_100(43, 58), False)
    Test.assert_equals(less_than_100(50, 44), True)
    Test.assert_equals(less_than_100(74, 89), False)
    Test.assert_equals(less_than_100(3, 27), True)
    Test.assert_equals(less_than_100(21, 79), False)
