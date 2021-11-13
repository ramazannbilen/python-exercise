"""Intersecting Intervals
Create a function that takes in a list of intervals and returns how many intervals overlap with a given point.

An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).

To illustrate:

count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
Examples
count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0

count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2

count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2
Notes
Each interval is represented as a list with a start point and an endpoint.
Intervals count as intersecting even if they only intersect at one point, i.e. [2, 3] and [3, 4] both intersect at point 3.
If it's helpful, you can draw these intervals on a line on a piece of paper."""

from edabit.Test import Test

def count_overlapping(intervals, point):
    counter = 0
    for i in intervals:
        if point >= i[0] and point <= i[1]:
            counter += 1
        else:
            continue
    return counter

Test.assert_equals(count_overlapping([[1, 2], [2, 3], [3, 4]], 5),0)
Test.assert_equals(count_overlapping([[1, 2], [5, 6], [5, 7]], 5),2)
Test.assert_equals(count_overlapping([[1, 2], [5, 8], [6, 9]], 7),2)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 5), 5)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 6), 2)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 2), 2)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 1), 1)