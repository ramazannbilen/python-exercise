"""
Repeating Letters
Create a function that takes a string and returns a string in which each character is repeated once.

Examples
double_char("String") ➞ "SSttrriinngg"

double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

double_char("1234!_ ") ➞ "11223344!!__  "
Notes
All test cases contain valid strings. Don't worry about spaces, special characters or numbers. They're all considered valid characters.
"""

from edabit.Test import Test


def double_char(txt):
    # txt2 = ""
    # for i in txt:
    #     txt2 += 2 * i
    # return txt2
    return "".join(i * 2 for i in txt)


if __name__ == '__main__':
    Test.assert_equals(double_char("1234!_ "), "11223344!!__  ")
    Test.assert_equals(double_char("Hello World!"), "HHeelllloo  WWoorrlldd!!")
    Test.assert_equals(double_char("##^&%%*&%%$#@@!"), "####^^&&%%%%**&&%%%%$$##@@@@!!")
    Test.assert_equals(double_char("scandal"), "ssccaannddaall")
    Test.assert_equals(double_char("String"), "SSttrriinngg")
    Test.assert_equals(double_char("economics"), "eeccoonnoommiiccss")
    Test.assert_equals(double_char(" "), "  ")
    Test.assert_equals(double_char("_______"), "______________")
    Test.assert_equals(double_char("equip gallon read"), "eeqquuiipp  ggaalllloonn  rreeaadd")
    Test.assert_equals(double_char("baby increase"), "bbaabbyy  iinnccrreeaassee")
