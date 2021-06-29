"""
Filter out Strings from an Array
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
Notes
Zero is a non-negative integer.
The given list only has integers and strings.
Numbers in the list should not repeat.
The original order must be maintained.
"""

from edabit.Test import Test
import types


def filter_list(lst):
    # for i in lst:
    #     if isinstance(i, int):   # my attempts
    #         i = i
    #     else:
    #         lst.remove(i)
    return [i for i in lst if isinstance(i, int)]               # do not forget to use isinstance() func. like that.


if __name__ == '__main__':
    Test.assert_equals(filter_list([1, 2, "a", "b"]), [1, 2])
    Test.assert_equals(filter_list([1, "a", "b", 0, 15]), [1, 0, 15])
    Test.assert_equals(filter_list([1, 2, "aasf", "1", "123", 123]), [1, 2, 123])
    Test.assert_equals(filter_list(["jsyt", 4, "yt", "6"]), [4])
    Test.assert_equals(filter_list(["r", 5, "y", "e", 8, 9]), [5, 8, 9])
    Test.assert_equals(filter_list(["a", "e", "i", "o", "u"]), [])
    Test.assert_equals(filter_list([4, "z", "f", 5]), [4, 5])
    Test.assert_equals(filter_list(["abc", 123]), [123])
    Test.assert_equals(filter_list(["$%^", 567, "&&&"]), [567])
    Test.assert_equals(filter_list(["w", "r", "u", 43, "s", "a", 76, "d", 88]), [43, 76, 88])
