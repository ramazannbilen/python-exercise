"""
Hamming Distance
Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.

Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
Notes
Both strings will have the same length.
"""

from edabit.Test import Test


def hamming_distance(txt1, txt2):
    diffs=0
    for i,j in zip(txt1,txt2):      # I can use to parameter in for loop as an array or a tuple.
        if i != j:                  # Also zip() method collect the elements of series that has same index one by one as a tuple.
            diffs += 1
    return diffs


if __name__ == '__main__':
    Test.assert_equals(hamming_distance("abcde", "bcdef"), 5)
    Test.assert_equals(hamming_distance("abcde", "abcde"), 0)
    Test.assert_equals(hamming_distance("strong", "strung"), 1)
