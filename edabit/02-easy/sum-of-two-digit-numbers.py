"""
Sum of Two Digit Numbers
For this challenge, you are supposed to find the sum of the digits of a two-digit number. Sounds easy, right? But for this challenge, I expect you to find the sum of the digits mathematically.

Sure, you can convert the number into a string and then manipulate it so it returns the sum of the digits, but the point of this challenge is to see if you know how to return the sum of the digits of a two-digit number mathematically.

Examples
two_digit_sum(45) ➞ 9

two_digit_sum(38) ➞ 11

two_digit_sum(67) ➞ 13
Notes
% //
"""

from edabit.Test import Test

def two_digit_sum(n):
    ss = [int(i) for i in str(n)]
    summ = 0
    for a in ss:
        summ += a
    return summ


if __name__ == '__main__':
    Test.assert_equals(two_digit_sum(45), 9)
    Test.assert_equals(two_digit_sum(65), 11)
    Test.assert_equals(two_digit_sum(85), 13)
    Test.assert_equals(two_digit_sum(52), 7)

    Test.assert_equals(two_digit_sum(15), 6)
    Test.assert_equals(two_digit_sum(48), 12)
    Test.assert_equals(two_digit_sum(33), 6)
    Test.assert_equals(two_digit_sum(29), 11)

    Test.assert_equals(two_digit_sum(81), 9)
    Test.assert_equals(two_digit_sum(10), 1)
    Test.assert_equals(two_digit_sum(40), 4)
    Test.assert_equals(two_digit_sum(66), 12)

    Test.assert_equals(two_digit_sum(19), 10)
    Test.assert_equals(two_digit_sum(38), 11)
    Test.assert_equals(two_digit_sum(67), 13)
    Test.assert_equals(two_digit_sum(96), 15)