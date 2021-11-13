"""Oddish vs. Evenish
Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.

Examples
oddish_or_evenish(43) ➞ "Oddish"
# 4 + 3 = 7
# 7 % 2 = 1

oddish_or_evenish(373) ➞ "Oddish"
# 3 + 7 + 3 = 13
# 13 % 2 = 1

oddish_or_evenish(4433) ➞ "Evenish"
# 4 + 4 + 3 + 3 = 14
# 14 % 2 = 0
Notes
N/A"""

from edabit.Test import Test


def oddish_or_evenish(num):
    c = 0
    for i in list(str(num)):
        c += int(i)
    if c % 2 == 0:
        return "Evenish"
    else:
        return "Oddish"

Test.assert_equals(oddish_or_evenish(43), "Oddish")
Test.assert_equals(oddish_or_evenish(373), "Oddish")
Test.assert_equals(oddish_or_evenish(55551), "Oddish")
Test.assert_equals(oddish_or_evenish(694), "Oddish")
Test.assert_equals(oddish_or_evenish(4433), "Evenish")
Test.assert_equals(oddish_or_evenish(11), "Evenish")
Test.assert_equals(oddish_or_evenish(211112), "Evenish")
