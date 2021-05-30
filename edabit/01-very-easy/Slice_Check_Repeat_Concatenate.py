"""
Front 3 - Slice Check Repeat Concatenate
Create a function that takes a string; we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.

Examples
front3("Python") ➞ "PytPytPyt"

front3("Cucumber") ➞ "CucCucCuc"

front3("bioshock") ➞ "biobiobio"
Notes
Don't forget to return the result.
"""

from edabit.Test import Test


def front3(txt):
    if len(txt) < 3:
        first3 = txt
    else:
        first3 = txt[:3]

    return (first3 + first3 + first3)


if __name__ == '__main__':
    Test.assert_equals(front3('Python'), 'PytPytPyt')
    Test.assert_equals(front3('Chocolate'), 'ChoChoCho')
    Test.assert_equals(front3('duh'), 'duhduhduh',)
    Test.assert_equals(front3('Sportsmanship'), 'SpoSpoSpo')
    Test.assert_equals(front3('ab'), 'ababab',)
    Test.assert_equals(front3('a'), 'aaa')
    Test.assert_equals(front3(''), '')

