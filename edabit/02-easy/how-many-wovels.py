"""
How Many Vowels?
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
All test cases are one word and only contain letters.
"""

from edabit.Test import Test

wovels = ["a", "e", "i", "o", "u"]


def count_vowels(txt):
    count = 0
    for i in range(len(txt)): # every string is an array, do not forget it!
        if txt[i] in wovels:
            count += 1
    return count


if __name__ == '__main__':
    Test.assert_equals(count_vowels("Celebration"), 5)
    Test.assert_equals(count_vowels("Palm"), 1)
    Test.assert_equals(count_vowels("Prediction"), 4)
    Test.assert_equals(count_vowels("Suite"), 3)
    Test.assert_equals(count_vowels("Quote"), 3)
    Test.assert_equals(count_vowels("Portrait"), 3)
    Test.assert_equals(count_vowels("Steam"), 2)
    Test.assert_equals(count_vowels("Tape"), 2)
    Test.assert_equals(count_vowels("Nightmare"), 3)
    Test.assert_equals(count_vowels("Convention"), 4)
