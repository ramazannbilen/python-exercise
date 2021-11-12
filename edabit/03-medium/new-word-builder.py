"""New Word Builder
Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the word).

Examples
word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"

word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"

word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit"
Notes
The elements in the second list are indexes of the elements in the first list."""

from edabit.Test import Test


def word_builder(ltr, pos):
    lst = [0] * len(ltr)
    for i in range(len(pos)):
        lst[pos[i]] = ltr[i]
    word = "".join(lst)
    return word


Test.assert_equals(word_builder(["g", "e", "o"], [1, 0, 2]), 'ego')
Test.assert_equals(word_builder(["t", "t", "s", "e"], [3, 0, 2, 1]), 'test')
Test.assert_equals(word_builder(["b", "e", "t", "i", "d", "a"], [3, 0, 5, 4, 1, 2]), 'edabit')
Test.assert_equals(word_builder(["l", "e", "l", "n", "c", "h", "a", "e", "g"], [3, 5, 4, 6, 0, 1, 2, 8, 7]),
                   'challenge')
Test.assert_equals(word_builder(["s", "o", "r", "t", "e", "d"], [0, 1, 2, 3, 4, 5]), 'sorted')
