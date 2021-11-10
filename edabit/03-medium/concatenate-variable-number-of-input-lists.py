"""Concatenate Variable Number of Input Lists
Create a function that concatenates n input lists, where n is variable.

Examples
concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]

concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]

concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]
Notes
Lists should be concatenated in order of the arguments."""


from edabit.Test import Test


def concat(*args):
    new = []
    for i in args:
        new.extend(i)
    return new

Test.assert_equals(concat([1, 2, 3], [4, 5], [6, 7]), [1, 2, 3, 4, 5, 6, 7])
Test.assert_equals(concat([1], [2], [3], [4], [5], [6], [7]), [1, 2, 3, 4, 5, 6, 7])
Test.assert_equals(concat([1, 2], [3, 4]), [1, 2, 3, 4])
Test.assert_equals(concat([4, 4, 4, 4, 4]), [4, 4, 4, 4, 4])
Test.assert_equals(concat(['a'], ['b', 'c']), ['a', 'b', 'c'])