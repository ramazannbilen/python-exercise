"""
Vowel Replacer
Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
Notes
All characters will be in lower case.
"""

from edabit.Test import Test


def replace_vowels(txt, ch):
    wovels = ["a", "A", "e", "E", "o", "O", "u", "U", "i", "I"]
    for i in range(len(txt)):
        if txt[i] in wovels:
            txt = txt.replace(txt[i], ch)   #do not forget replace() method again :(
    return txt


if __name__ == '__main__':
    Test.assert_equals(replace_vowels("the aardvark", "#"), "th# ##rdv#rk")
    Test.assert_equals(replace_vowels("minnie mouse", "?"), "m?nn?? m??s?")
    Test.assert_equals(replace_vowels("shakespeare", "*"), "sh*k*sp**r*")
    Test.assert_equals(replace_vowels("all is fair in love and war", "<"), "<ll <s f<<r <n l<v< <nd w<r")
