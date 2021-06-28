"""
Xs and Os, Nobody Knows
Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

Return a boolean value (True or False).
Return True if the amount of x's and o's are the same.
Return False if they aren't the same amount.
The string can contain any character.
When "x" and "o" are not in the string, return True.
Examples
XO("ooxx") ➞ True

XO("xooxx") ➞ False

XO("ooxXm") ➞ True
# Case insensitive.

XO("zpzpzpp") ➞ True
# Returns True if no x and o.

XO("zzoo") ➞ False
Notes
Remember to return True if there aren't any x's or o's.
Must be case insensitive.
"""

from edabit.Test import Test


def XO(txt):
    # count1 = 0
    # count2 = 0
    # for i in range(len(txt)):
    #     if txt[i] == "o" or "O":          #it is my first attempt. I cant get why It failed :???
    #         count1 += 1
    #
    # for i in range(len(txt)):
    #     if txt[i] == "x" or "X":
    #         count2 += 1
    oo = "o"
    OO = "O"
    xx = "x"
    XX = "X"
    counto = txt.count(oo) + txt.count(OO)
    countx = txt.count(xx) + txt.count(XX)
    if countx == counto:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(XO("ooxx"), True)
    Test.assert_equals(XO("xooxx"), False)
    Test.assert_equals(XO("ooxXm"), True)
    Test.assert_equals(XO("zpzpzpp"), True)
    Test.assert_equals(XO("zzoo"), False)
    Test.assert_equals(XO("Xo"), True)
    Test.assert_equals(XO("x"), False)
    Test.assert_equals(XO("o"), False)
    Test.assert_equals(XO("xxxoo"), False)
    Test.assert_equals(XO(""), True)
