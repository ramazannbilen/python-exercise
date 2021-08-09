"""
Moving to the End
Write a function that moves all elements of one type to the end of the list.

Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
Notes
Keep the order of the un-moved items the same.
"""

from edabit.Test import Test


def move_to_end(lst, el):
    lst2 = [i for i in lst if i != el]
    el2 = lst.count(el)
    return lst2 + el2 * [el]


if __name__ == '__main__':
    Test.assert_equals(move_to_end([1, 3, 2, 4, 4, 1], 1), [3, 2, 4, 4, 1, 1])
    Test.assert_equals(move_to_end([7, 8, 9, 1, 2, 3, 4], 9), [7, 8, 1, 2, 3, 4, 9])
    Test.assert_equals(move_to_end([7, 7, 7, 6, 6, 6, 6], 7), [6, 6, 6, 6, 7, 7, 7])
    Test.assert_equals(move_to_end(["a", "c", "c", "c", "b", "c"], "b"), ["a", "c", "c", "c", "c", "b"])
    Test.assert_equals(move_to_end(["a", "c", "c", "c", "b", "c"], "c"), ["a", "b", "c", "c", "c", "c"])
    Test.assert_equals(move_to_end(["a", "a", "a", "b"], "a"), ["b", "a", "a", "a"])
