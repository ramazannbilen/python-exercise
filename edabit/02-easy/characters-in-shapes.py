"""
Characters in Shapes
Create a function to calculate how many characters in total are needed to make up the shape. You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).

Examples
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9

count_characters([
  "22222222",
  "22222222",
]) ➞ 16

count_characters([
  "------------------"
]) ➞ 18

count_characters([]) ➞ 0

count_characters(["", ""]) ➞ 0
Notes
Return 0 if the given list is empty.
"""

from edabit.Test import Test


def count_characters(lst):
    ch = 0
    for i in lst:                   # just focus on algoritm that you need.
        ch += len(i)
    return ch


if __name__ == '__main__':
    Test.assert_equals(count_characters([
        '###',
        '###',
        '###'
    ]), 9)

    Test.assert_equals(count_characters([
        '22222222',
        '22222222',
    ]), 16)

    Test.assert_equals(count_characters([
        '------------------'
    ]), 18)

    Test.assert_equals(count_characters([]), 0)
    Test.assert_equals(count_characters([
        '',
        '']), 0)
