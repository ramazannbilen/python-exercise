"""
Find ASCII Charcode of Inverse Case Character
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65
Notes
The argument will always be a single character.
Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.
"""

from edabit.Test import Test


def counterpartCharCode(char):
    return ord(char.swapcase()) #swapcase changes the upper to the lower and vise versa :)


if __name__ == '__main__':
    ## Normal letters
    Test.assert_equals(counterpartCharCode('a'), 65)
    Test.assert_equals(counterpartCharCode('A'), 97)
    Test.assert_equals(counterpartCharCode('l'), 76)
    Test.assert_equals(counterpartCharCode('L'), 108)
    Test.assert_equals(counterpartCharCode('z'), 90)
    Test.assert_equals(counterpartCharCode('Z'), 122)

    ## These don't have a counterpart, you should return the input's char code
    Test.assert_equals(counterpartCharCode('5'), 53)
    Test.assert_equals(counterpartCharCode('$'), 36)
