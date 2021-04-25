"""
Return Something to Me!
Write a function that returns the string "something" joined with a space " " and the given argument a.

Examples
give_me_something("is better than nothing") ➞ "something is better than nothing"

give_me_something("Bob Jane") ➞ "something Bob Jane"

give_me_something("something") ➞ "something something"
Notes
Assume an input is given.
"""

from edabit.Test import Test


def give_me_something(a):
    gms = lambda a: "something "+a
    return gms(a)


if __name__ == '__main__':
    Test.assert_equals(give_me_something("a"), "something a")
    Test.assert_equals(give_me_something("is cooking"), "something is cooking")
    Test.assert_equals(give_me_something(" is cooking"), "something  is cooking")