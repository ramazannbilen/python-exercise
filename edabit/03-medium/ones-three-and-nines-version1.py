"""Ones, Threes and Nines (Version #1)
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0

n1.ones ➞ 5

n1.threes ➞ 1
Notes
Do not use the math module.
See version #2 of this series."""

from edabit.Test import Test


# very important for learning claases

class ones_threes_nines:
    def __init__(self, num):
        self.ones = num / 1
        self.threes = num // 3
        self.nines = num // 9


n1 = ones_threes_nines(0)
Test.assert_equals(n1.ones, 0)
n2 = ones_threes_nines(1)
Test.assert_equals(n2.threes, 0)
n3 = ones_threes_nines(2)
Test.assert_equals(n3.nines, 0)
n4 = ones_threes_nines(3)
Test.assert_equals(n4.ones, 3)
n5 = ones_threes_nines(4)
Test.assert_equals(n5.threes, 1)
n6 = ones_threes_nines(10)
Test.assert_equals(n6.nines, 1)
n7 = ones_threes_nines(13)
Test.assert_equals(n7.ones, 13)
n8 = ones_threes_nines(15)
Test.assert_equals(n8.threes, 5)
n9 = ones_threes_nines(17)
Test.assert_equals(n9.nines, 1)
n10 = ones_threes_nines(20)
Test.assert_equals(n10.nines, 2)
