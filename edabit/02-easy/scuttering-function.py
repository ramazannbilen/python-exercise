"""
Stuttering Function
Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"
Notes
Assume all input is in lower case and at least two characters long.
"""

from edabit.Test import Test


def stutter(word):
    def first2(s):
        return s[:2]    #this method gets first two(choicable) character of the string.

    str1 = first2(word)
    str2 = "... "
    word = str1 + str2 + str1 + str2 + word + "?"
    return word


if __name__ == '__main__':
    actual_param, expected_param = [
                                       "increasing", "adventures", "enticing", "unacceptable", "accountable",
                                       "incredible", "exquisite",
                                       "am", "enduring", "outstanding", "astonishing", "astounding", "impressive",
                                       "revolutionize",
                                       "recurring", "recollection", "so", "gorgeous", "captivating"
                                   ], [
                                       "in... in... increasing?", "ad... ad... adventures?", "en... en... enticing?",
                                       "un... un... unacceptable?",
                                       "ac... ac... accountable?", "in... in... incredible?", "ex... ex... exquisite?",
                                       "am... am... am?",
                                       "en... en... enduring?", "ou... ou... outstanding?", "as... as... astonishing?",
                                       "as... as... astounding?",
                                       "im... im... impressive?", "re... re... revolutionize?",
                                       "re... re... recurring?", "re... re... recollection?",
                                       "so... so... so?", "go... go... gorgeous?", "ca... ca... captivating?",
                                   ]
    for i, w in enumerate(actual_param):
        Test.assert_equals(stutter(w), expected_param[i])
