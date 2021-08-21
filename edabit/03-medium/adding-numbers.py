"""
Adding Numbers
Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"
Notes
If any input is "" or None, return "Invalid Operation".
"""

from edabit.Test import Test


def add(n1, n2):
    # if n1 == "" or n1 == None or n1 == None or n2 == "":
    #     return "Invalid Operation"
    # else:
    #     summ = int(n1) + int(n2)
    #     return str(summ)

    try:
        summ = int(n1) + int(n2)
        return str(summ)
    except:
        return "Invalid Operation"


if __name__ == '__main__':
    Test.assert_equals(add("91", "19"), "110")
    Test.assert_equals(add("123456789", "987654322"), "1111111111")
    Test.assert_equals(add("9999999", "1"), "10000000")
    Test.assert_equals(add("300", "3000"), "3300")
    Test.assert_equals(add("1000", "6200"), "7200")
    Test.assert_equals(add("-10", "-20"), "-30")
    Test.assert_equals(add("-100", "100"), "0")
    Test.assert_equals(add("0", "6200"), "6200")
    Test.assert_equals(add("", "6"), "Invalid Operation")
    Test.assert_equals(add("", None), "Invalid Operation")
    Test.assert_equals(add(None, "23"), "Invalid Operation")
    Test.assert_equals(add("", "20"), "Invalid Operation")
