"""
Sum of Evenly Divisible Numbers from a Range
Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
Notes
Return 0 if there is no number between a and b that can be evenly divided by c.
"""

from edabit.Test import Test


def evenly_divisible(a, b, c):
    count = 0
    for i in range(a, b + 1):
        if i % c == 0:
            count += i
        else:
            count += 0
    return count


if __name__ == '__main__':
    Test.assert_equals(evenly_divisible(1, 10, 2), 30)
    Test.assert_equals(evenly_divisible(1, 10, 3), 18)
    Test.assert_equals(evenly_divisible(0, 12, 3), 30)
    Test.assert_equals(evenly_divisible(-10, -1, 2), -30)
    Test.assert_equals(evenly_divisible(-10, -1, 3), -18)
    Test.assert_equals(evenly_divisible(1, 10, 20), 0)
    Test.assert_equals(evenly_divisible(-10, 10, 2), 0)
