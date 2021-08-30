"""Two Distinct Elements
In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

Examples
return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
Notes
Keep the same ordering in the output."""

from edabit.Test import Test


def return_unique(lst):
    once = []
    for i in lst:
        if lst.count(i) == 1:
            once.append(i)
        else:
            continue
    return once

Test.assert_equals(return_unique([1, 9, 8, 8, 7, 6, 1, 6]), [9, 7])
Test.assert_equals(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]), [2, 1])
Test.assert_equals(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]), [5, 6])
Test.assert_equals(return_unique([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4]), [3, 2])
Test.assert_equals(return_unique([44, 44, 44, 2, 55, 55, 55, 0, 66, 66, 66]), [2, 0])
Test.assert_equals(return_unique([-9, -9, -9, 7, -9, -9, 1]), [7, 1])
Test.assert_equals(return_unique([2, 2, -19, 2, 7, 7, 4, 9, 9, 0, 0, 3, 3, 3]), [-19, 4])
