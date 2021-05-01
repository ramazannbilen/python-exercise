"""
Curzon Numbers
In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29
"""

from edabit.Test import Test


def is_curzon(num):
    cur1 = 2 ** num + 1
    cur2 = 2 * num + 1
    if cur1 % cur2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(is_curzon(5), True)
    Test.assert_equals(is_curzon(10), False)
    Test.assert_equals(is_curzon(14), True)
    Test.assert_equals(is_curzon(86), True)
    Test.assert_equals(is_curzon(90), True)
    Test.assert_equals(is_curzon(115), False)
    Test.assert_equals(is_curzon(120), False)
    Test.assert_equals(is_curzon(194), True)
    Test.assert_equals(is_curzon(293), True)
