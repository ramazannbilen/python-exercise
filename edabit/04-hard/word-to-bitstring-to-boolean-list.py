"""Word to Bitstring to Boolean List
Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

Locate the position of the letter in the English alphabet (from 1 to 26).
Odd positions will be represented as 1 and even positions will be represented as 0.
Convert the represented positions to boolean values, 1 for True and 0 for False.
Store the conversions into an array.
Examples
to_boolean_list("deep") ➞ [False, True, True, False]
# deep converts to 0110
# d is the 4th alphabet - 0
# e is the 5th alphabet - 1
# e is the 5th alphabet - 1
# p is the 16th alphabet - 0

to_boolean_list("loves") ➞ [False, True, False, True, True]

to_boolean_list("tesh") ➞ [False, True, True, False]
Notes
The letter A is at position 1 and Z at 26.
All input strings are in lowercase letters of the English alphabet."""

from edabit.Test import Test

def to_boolean_list(word):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    res = []
    for i in word:
        if alp.index(i) % 2 == 1:
            res.append(False) #alphabet first letter starts with 0
        else:
            res.append(True)
    return res


actual_param = [
  "charming", "exquisite", "admire", "deep", "loves", "tesh",
  "xavier", "adores", "tesha", "esquire", "randomize", "exotic"
]
expected_param = [
  [True, False, True, False, True, True, False, True],
  [True, False, True, True, True, True, True, False, True],
  [True, False, True, True, False, True],
  [False, True, True, False],
  [False, True, False, True, True],
  [False, True, True, False],
  [False, True, False, True, True, False],
  [True, False, True, False, True, True],
  [False, True, True, False, True],
  [True, True, True, True, True, False, True],
  [False, True, False, False, True, True, True, False, True],
  [True, False, True, False, True, True]
]
for i, x in enumerate(actual_param): Test.assert_equals(to_boolean_list(x), expected_param[i])