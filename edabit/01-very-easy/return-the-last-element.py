"""
Return the Last Element in a List
Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.

Examples
get_last_item([1, 2, 3]) ➞ 3

get_last_item(["cat", "dog", "duck"]) ➞ "duck"

get_last_item([True, False, True]) ➞ True

get_last_item([7, "String", False]) ➞ False
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test


def get_last_item(lst):
    return lst[-1]

if __name__ == '__main__':
    Test.assert_equals(get_last_item(['Cat', 'Dog', 'Duck']), 'Duck')
    Test.assert_equals(get_last_item([1, 2, 3]), 3)
    Test.assert_equals(get_last_item([True, False, False, True]), True)
    Test.assert_equals(get_last_item([7, 'String', False]), False)
    Test.assert_equals(get_last_item([False]), False)
    Test.assert_equals(get_last_item([1, 2, 3, 56, 87, 23, 65, 45]), 45)
    Test.assert_equals(get_last_item(['Apple', 'Orange']), 'Orange')
    Test.assert_equals(get_last_item([True, False, 'Apple']), 'Apple')
    Test.assert_equals(get_last_item([1]), 1)

