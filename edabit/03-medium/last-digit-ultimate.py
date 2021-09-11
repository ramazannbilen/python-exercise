"""Last Digit Ultimate
Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the last digit of c. Check the examples below for an explanation.

Examples
last_dig(25, 21, 125) ➞ True
# The last digit of 25 is 5, the last digit of 21 is 1, and the last
# digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# to the last digit of 125(5).

last_dig(55, 226, 5190) ➞ True
# The last digit of 55 is 5, the last digit of 226 is 6, and the last
# digit of 5190 is 0, and the last digit of 5*6 = 30 is 0, which is
# equal to the last digit of 5190(0).

last_dig(12, 215, 2142) ➞ False
# The last digit of 12 is 2, the last digit of 215 is 5, and the last
# digit of 2142 is 2, and the last digit of 2*5 = 10 is 0, which is
# not equal to the last digit of 2142(2).
Notes
Numbers can be negative."""

from edabit.Test import Test


def last_dig(a, b, c):
    # if str(int(str(a)[-1]) * int(str(b)[-1]))[-1] == str(c)[-1]:
    #     return True
    # else:
    #     return False

    if ((a % 10) * (b % 10)) % 10 == c % 10:  # better than first
        return True
    else:
        return False


Test.assert_equals(last_dig(1, 1, 1), True)
Test.assert_equals(last_dig(12, 15, 10), True)
Test.assert_equals(last_dig(15228, 9209, 72162), True)
Test.assert_equals(last_dig(15, 1, 1), False)
Test.assert_equals(last_dig(123, 15, 10), False)
Test.assert_equals(last_dig(5213, 99219, 6165), False)
Test.assert_equals(last_dig(1523, 513, 512), False)
Test.assert_equals(last_dig(-15, 1, 1), False)
Test.assert_equals(last_dig(123, -15, 10), False)
Test.assert_equals(last_dig(-12, 15, -10), True)
Test.assert_equals(last_dig(15228, -9209, -72162), True)
