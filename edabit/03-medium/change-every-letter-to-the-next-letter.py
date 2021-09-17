"""
Change Every Letter to the Next Letter
Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
Examples
move("hello") ➞ "ifmmp"

move("bye") ➞ "czf"

move("welcome") ➞ "xfmdpnf"
Notes
There will be no z's in the tests.
"""

from edabit.Test import Test


def move(word):
    letters = "abcdefghijklmnopqrstuvxyzw"
    a = [letters.index(i) for i in word]
    b = [i + 1 for i in a]
    c = [letters[i] for i in b]
    return "".join(c)


Test.assert_equals(move("hello"), "ifmmp")
Test.assert_equals(move("lol"), "mpm")
Test.assert_equals(move("bye"), "czf")
