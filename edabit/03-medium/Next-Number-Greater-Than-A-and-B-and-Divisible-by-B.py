"""
Next Number Greater Than A and B and Divisible by B
You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.

Examples
divisible_by_b(17, 8) ➞ 24

divisible_by_b(98, 3) ➞ 99

divisible_by_b(14, 11) ➞ 22
Notes
a will always be greater than b.
"""

from edabit.Test import Test


def divisible_by_b(a, b):
    n = 1
    x = 0
    while x == 0:
        if (a + n) % b == 0:
            x = 1
            return a + n
        else:
            n += 1


Test.assert_equals(divisible_by_b(17, 8), 24)
Test.assert_equals(divisible_by_b(98, 3), 99)
Test.assert_equals(divisible_by_b(14, 11), 22)
Test.assert_equals(divisible_by_b(11, 8), 16)
Test.assert_equals(divisible_by_b(450, 36), 468)
Test.assert_equals(divisible_by_b(1019, 13), 1027)
