"""
Concatenating Two Integer Lists
Create a function to concatenate two integer lists.

Examples
concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]
Notes
Don't forget to return the result.
See Resources tab for more info.
"""

from edabit.Test import Test


def concat(lst1, lst2):
    lst3 = lst1 + lst2
    return lst3


if __name__ == '__main__':
    Test.assert_equals(concat([1, 3, 5], [2, 6, 8]), [1, 3, 5, 2, 6, 8])
    Test.assert_equals(concat([7, 8], [10, 9, 1, 1, 2]), [7, 8, 10, 9, 1, 1, 2])
    Test.assert_equals(concat([4, 5, 1], [3, 3, 3, 3, 3]), [4, 5, 1, 3, 3, 3, 3, 3])
