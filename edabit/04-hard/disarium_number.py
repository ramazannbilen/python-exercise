"""
Disarium Number
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True
Notes
Position of the digit is 1-indexed.
A recursive version of this challenge can be found via this link.
"""

from edabit.Test import Test

def is_disarium(n):
    total = 0
    for i in range(len(str(n))):
        total += int(str(n)[i])**(i+1)
    if total >= n:
        return True
    else:
        return False


num_vector, res_vector = [
  [6, 75, 135, 466, 372, 175, 1, 696, 876, 89, 518, 598],
  [True, False, True, False, False, True, True, False, False, True, True, True]
]
for i, n in enumerate(num_vector): Test.assert_equals(is_disarium(n), res_vector[i])