"""Check If Lines Are Parallel
Given two lines, determine whether or not they are parallel.

Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ False
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ True
# Lines are parallel to themselves.
Notes
Two lines are parallels if they have the same slope. If the slopes are different, the lines are not parallel.
All test cases use valid input (no lists of the wrong size, for example).
All coefficients will be integers (whole numbers)."""

from edabit.Test import Test


def lines_are_parallel(l1, l2):
    if l1[1] != 0 and l2[1] != 0:
        if l1[0] / l1[1] == l2[0] / l2[1]:
            return True
        else:
            return False
    else:
        if l1[0] / l2[0] == l1[1] / l2[1]:
            return True
        else:
            return False


Test.assert_equals(lines_are_parallel([1, 2, 3], [1, 2, 4]), True)
Test.assert_equals(lines_are_parallel([2, 4, 1], [4, 2, 1]), False)
Test.assert_equals(lines_are_parallel([0, 1, 5], [0, 1, 5]), True)
Test.assert_equals(lines_are_parallel([2, 5, 0], [20, 50, 10]), True)
Test.assert_equals(lines_are_parallel([2, 5, 0], [-200, -500, 10]), True)
Test.assert_equals(lines_are_parallel([400000, 1, 0], [400000, 2, 0]), False)
Test.assert_equals(lines_are_parallel([800, 20, 0], [40, 20, 0]), False)
Test.assert_equals(lines_are_parallel([400000, 1, 0], [800000, 2, 100000]), True)
Test.assert_equals(lines_are_parallel([-5, 7, 100000], [5, -7, -200000]), True)
