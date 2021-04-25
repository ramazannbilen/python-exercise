"""
Return the First Element in a List
Create a function that takes a list containing only numbers and return the first element.

Examples
get_first_value([1, 2, 3]) ➞ 1

get_first_value([80, 5, 100]) ➞ 80

get_first_value([-500, 0, 50]) ➞ -500
Notes
The first element in a list always has an index of 0.
"""

from edabit.Test import Test


def get_first_value(number_list):
    return number_list[0]

if __name__ == '__main__':
    Test.assert_equals(get_first_value([1, 2, 3]), 1)
    Test.assert_equals(get_first_value([80, 5, 100]), 80)
    Test.assert_equals(get_first_value([-500, 0, 50]), -500)
    Test.assert_equals(get_first_value([5, 2, 3]), 5)
    Test.assert_equals(get_first_value([75675, 5, 100]), 75675)
    Test.assert_equals(get_first_value([-52320, 0, 50]), -52320)
