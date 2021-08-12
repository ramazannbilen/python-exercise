"""
Alphabet Soup
Create a function that takes a string and returns a string with its letters in alphabetical order.

Examples
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"
Notes
You can assume numbers and punctuation symbols won't be included in test cases. You'll only have to deal with single word, alphabetic characters.
"""

from edabit.Test import Test


def alphabet_soup(txt):
    alp = ""
    return alp.join(sorted(txt))


if __name__ == '__main__':
    Test.assert_equals(alphabet_soup("hello"), "ehllo")
    Test.assert_equals(alphabet_soup("edabit"), "abdeit")
    Test.assert_equals(alphabet_soup("hacker"), "acehkr")
    Test.assert_equals(alphabet_soup("geek"), "eegk")
    Test.assert_equals(alphabet_soup("javascript"), "aacijprstv")
    Test.assert_equals(alphabet_soup("credibility"), "bcdeiiilrty")
    Test.assert_equals(alphabet_soup("apostrophe"), "aehoopprst")
    Test.assert_equals(alphabet_soup("determination"), "adeeiimnnortt")
    Test.assert_equals(alphabet_soup("win"), "inw")
    Test.assert_equals(alphabet_soup("synthesis"), "ehinsssty")
