"""Sum of Missing Numbers
Create a function that returns the sum of missing numbers from the given list.

Examples
sum_missing_numbers([4, 3, 8, 1, 2]) ➞ 18
# 5 + 6 + 7 = 18

sum_missing_numbers([17, 16, 15, 10, 11, 12]) ➞ 27
# 13 + 14 = 27

sum_missing_numbers([1, 2, 3, 4, 5]) ➞ 0
# No Missing Numbers (i.e. all numbers in [1, 5] are present in the list)
Notes
The numerical range to consider when searching for the missing numbers in the list is the sequence of consecutive numbers between the minimum and maximum of the numbers (inclusive)."""

from edabit.Test import Test


def sum_missing_numbers(lst):
    maxi = max(lst)
    mini = min(lst)
    no_item = 0
    for i in range(mini, (maxi + 1)):
        if i in lst:
            pass
        else:
            no_item += i

    return no_item


Test.assert_equals(sum_missing_numbers([1, 2, 3, 4, 5]), 0)
Test.assert_equals(sum_missing_numbers([4, 3, 8, 1, 2]), 18)
Test.assert_equals(sum_missing_numbers([17, 16, 15, 10, 11, 12]), 27)
Test.assert_equals(sum_missing_numbers([-1, -4, -3, -2, -6, -8]), -12)
