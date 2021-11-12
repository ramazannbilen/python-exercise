"""Letters Shared Between Two Words
Create a function that returns the number of characters shared between two words.

Examples
shared_letters("apple", "meaty") ➞ 2
# Since "ea" is shared between "apple" and "meaty".

shared_letters("fan", "forsook") ➞ 1

shared_letters("spout", "shout") ➞ 4
Notes
N/A"""

from edabit.Test import Test


def shared_letters(txt1, txt2):
    c= []
    for i in list(txt1):
        if i in txt2 and not i in c:
            c.append(i)
    return len(c)

Test.assert_equals(shared_letters("apple", "meaty"), 2)
Test.assert_equals(shared_letters("fan", "forsook"), 1)
Test.assert_equals(shared_letters("spout", "shout"), 4)
Test.assert_equals(shared_letters("took", "taken"), 2)
Test.assert_equals(shared_letters("mentor", "terminal"), 5,)
Test.assert_equals(shared_letters("class", "last"), 3)