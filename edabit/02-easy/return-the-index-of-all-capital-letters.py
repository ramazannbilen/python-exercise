"""
Return the Index of All Capital Letters
Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]
Notes
Return an empty list if no uppercase letters are found in the string.
Special characters ($#@%) and numbers will be included in some test cases.
Assume all words do not have duplicate letters.
"""

from edabit.Test import Test


def index_of_caps(word):
    indexes = []
    for i in range(len(word)):
        if word[i].isupper() == True:
            indexes += [i]
    return indexes


if __name__ == '__main__':
    Test.assert_equals(index_of_caps("eDaBiT"), [1, 3, 5])
    Test.assert_equals(index_of_caps("eQuINoX"), [1, 3, 4, 6])
    Test.assert_equals(index_of_caps("determine"), [])
    Test.assert_equals(index_of_caps("STRIKE"), [0, 1, 2, 3, 4, 5])
    Test.assert_equals(index_of_caps("sUn"), [1])
    Test.assert_equals(index_of_caps("SpiDer"), [0, 3])
    Test.assert_equals(index_of_caps("accOmpAnY"), [3, 6, 8])
    Test.assert_equals(index_of_caps("@xCE#8S#i*$en"), [2, 3, 6])
    Test.assert_equals(index_of_caps("1854036297"), [])
    Test.assert_equals(index_of_caps("Fo?.arg~{86tUx=|OqZ!"), [0, 12, 16, 18])
