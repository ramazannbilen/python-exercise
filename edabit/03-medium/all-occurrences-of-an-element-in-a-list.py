"""All Occurrences of an Element in a List
Create a function that returns the indices of all occurrences of an item in the list.

Examples
get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]

get_indices([1, 5, 5, 2, 7], 7) ➞ [4]

get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]

get_indices([1, 5, 5, 2, 7], 8) ➞ []
Notes
If an element does not exist in a list, return [].
Lists are zero-indexed.
Values in the list will be value-types (don't need to worry about nested lists)."""

from edabit.Test import Test

def get_indices(lst, el):
    ind = []
    for i in range(len(lst)):
        if lst[i] == el:
            ind += [i]
        else:
            pass
    return ind


Test.assert_equals(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'), [0, 1, 3, 5])
Test.assert_equals(get_indices([1, 5, 5, 2, 7], 7), [4])
Test.assert_equals(get_indices([1, 5, 5, 2, 7], 5),[1, 2])
Test.assert_equals(get_indices([1, 5, 5, 2, 7], 8), [])
Test.assert_equals(get_indices([8, 8, 8, 8, 8], 8), [0, 1, 2, 3, 4])
Test.assert_equals(get_indices([8, 8, 7, 8, 8], 8), [0, 1, 3, 4])
Test.assert_equals(get_indices([True, False, True, False], True), [0, 2])
Test.assert_equals(get_indices([True, False, True, False], False), [1, 3])