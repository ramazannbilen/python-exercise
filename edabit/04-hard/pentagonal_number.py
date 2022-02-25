"""
Pentagonal Number
Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.

alt text

Return the number of dots that exist in the whole pentagon on the Nth iteration.

Examples
pentagonal(1) ➞ 1

pentagonal(2) ➞ 6

pentagonal(3) ➞ 16

pentagonal(8) ➞ 141
Notes
N/A
"""

from edabit.Test import Test

def pentagonal(num):
    if num == 1:
        return 1
    else:
        total = 0
        for i in range(num-1):
            total += (i+1)*5
        return total + 1


Test.assert_equals(pentagonal(1), 1)
Test.assert_equals(pentagonal(3), 16)
Test.assert_equals(pentagonal(8), 141)
Test.assert_equals(pentagonal(10), 226)
Test.assert_equals(pentagonal(15), 526)
Test.assert_equals(pentagonal(33), 2641)
Test.assert_equals(pentagonal(43), 4516)
Test.assert_equals(pentagonal(13), 391)
Test.assert_equals(pentagonal(50), 6126)
Test.assert_equals(pentagonal(62), 9456)
Test.assert_equals(pentagonal(21), 1051)