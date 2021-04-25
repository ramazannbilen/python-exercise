"""
Basketball Points
You are counting points for a basketball game, given the amount of 3-pointers scored and 2-pointers scored,
find the final points for the team and return that value
([2 -pointers scored, 3-pointers scored]).

Examples
points(1, 1) ➞ 5

points(7, 5) ➞ 29

points(38, 8) ➞ 100
"""

from edabit.Test import Test


def points(twopointers, threepointers):
    return twopointers * 2 + threepointers * 3


if __name__ == '__main__':
    Test.assert_equals(points(1, 1), 5)
    Test.assert_equals(points(1, 2), 8)
    Test.assert_equals(points(2, 1), 7)
    Test.assert_equals(points(2, 2), 10)
    Test.assert_equals(points(69, 420), 1398)
