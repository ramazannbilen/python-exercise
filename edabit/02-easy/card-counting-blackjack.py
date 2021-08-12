"""
Card Counting (BlackJack)
In BlackJack, cards are counted with -1, 0, 1 values:

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the list of cards provided.

Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
Notes
String inputs will always be upper case.
You do not need to consider case sensitivity.
If the argument is empty, return 0.
No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
"""

from edabit.Test import Test


def count(deck):
    plus1 = [2,3,4,5,6]
    zero = [7,8,9]
    minus1 = [10,"J","Q","K","A"]
    allsum = 0
    for i in deck:
        if i in plus1:
            allsum += 1
        elif i in zero:
            allsum+=0
        elif i in minus1:
            allsum -= 1
    return allsum



if __name__ == '__main__':
    Test.assert_equals(count([5, 9, 10, 3, 'J', 'A', 4, 8, 5]), 1)
    Test.assert_equals(count(['A', 'A', 'K', 'Q', 'Q', 'J']), -6)
    Test.assert_equals(count(['A', 5, 5, 2, 6, 2, 3, 8, 9, 7]), 5)
    Test.assert_equals(count([2, 2, 2, 2, 2, 2, 2, 2]), 8)
    Test.assert_equals(count([]), 0)
    Test.assert_equals(count(['A', 'A', 'A', 'A', 'A', 'A', 'A']), -7)
    Test.assert_equals(count(['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]), 0)
