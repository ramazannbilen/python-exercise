"""Emphasise the Words
The challenge is to recreate the functionality of the title() method into a function called emphasise(). The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.

Examples
emphasise("hello world") ➞ "Hello World"

emphasise("GOOD MORNING") ➞ "Good Morning"

emphasise("99 red balloons!") ➞ "99 Red Balloons!"
Notes
You won't run into any issues when dealing with numbers in strings.
Please don't use the title() method directly :("""

from edabit.Test import Test


def emphasise(txt):
    liste = txt.split()
    lst = [i.capitalize() for i in liste]
    son = " ".join(lst)
    return son


Test.assert_equals(emphasise("hello world"), "Hello World")
Test.assert_equals(emphasise("GOOD MORNING"), "Good Morning")
Test.assert_equals(emphasise("99 red balloons!"), "99 Red Balloons!")
Test.assert_equals(emphasise("1 2 3 4 5 6 7 8 9"), "1 2 3 4 5 6 7 8 9")
Test.assert_equals(emphasise(""), "")
Test.assert_equals(emphasise("joshua senoron"), "Joshua Senoron")
