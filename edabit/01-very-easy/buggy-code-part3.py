"""
Buggy Code (Part 3)
Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.

Examples
sum_lst([1, 2, 3, 4, 5]) ➞ 15

sum_lst([-1, 0, 1]) ➞ 0

sum_lst([0, 4, 8, 12]) ➞ 24
Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.
"""

from edabit.Test import Test


# written codes
# def sum_lst(lst):
#     total
#     for i in range(0, lst):
#         total += lst[i]
#     return total

# that is first choice
# def sum_lst(lst):
#     return sum(lst)

# and the second
def sum_lst(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i - 1]
    return total


if __name__ == '__main__':
    Test.assert_equals(sum_lst([1, 2, 3, 4, 5]), 15)
    Test.assert_equals(sum_lst([-1, 0, 1]), 0)
    Test.assert_equals(sum_lst([0, 4, 8, 12]), 24)
