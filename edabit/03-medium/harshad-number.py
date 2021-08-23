"""Harshad Number
A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12

is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171

is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True
Notes
A recursive version of this challenge can be found in here.
"""
from edabit.Test import Test

def is_harshad(n):
    summ = 0
    for i in str(n):
        summ += int(i)
    if n%summ == 0:
        return True
    else:
        return False

num_vector, res_vector = [
  [75, 171, 481, 89, 516, 200, 209, 12345, 53, 27],
  [False, True, True, False, True, True, True, True, False, True]
]
for i, n in enumerate(num_vector):
    Test.assert_equals(is_harshad(n), res_vector[i])

