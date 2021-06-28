"""
Shuffle the Name
Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

Examples
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"
Notes
There will be exactly one space between the first and last name.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test


def name_shuffle(txt):
    txt2 = txt.split()
    fn = txt2[0]
    ln = txt2[1]
    space = " "
    return ln + " " + fn


if __name__ == '__main__':
    Test.assert_equals(name_shuffle("Donald Trump"), "Trump Donald")
    Test.assert_equals(name_shuffle("Rosie O'Donnel"), "O'Donnel Rosie")
    Test.assert_equals(name_shuffle("Seymour Butts"), "Butts Seymour")
    Test.assert_equals(name_shuffle("Ebony Greene"), "Greene Ebony")
    Test.assert_equals(name_shuffle("Ken Kennedy"), "Kennedy Ken")
    Test.assert_equals(name_shuffle("Allison Gonzalez"), "Gonzalez Allison")
    Test.assert_equals(name_shuffle("Albert Frazier"), "Frazier Albert")
    Test.assert_equals(name_shuffle("Eloise Hopkins"), "Hopkins Eloise")
    Test.assert_equals(name_shuffle("Donnie Welch"), "Welch Donnie")
    Test.assert_equals(name_shuffle("Vernon Thomas"), "Thomas Vernon")
