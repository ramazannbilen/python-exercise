"""
Date Format
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"
Notes
Return value should be a string.
"""

from edabit.Test import Test


def format_date(date):
    date2 = date.split("/")
    date2.reverse()
    last = ""
    for i in date2:
        last += i
    return last


if __name__ == '__main__':
    Test.assert_equals(format_date("11/12/2019"), "20191211")
    Test.assert_equals(format_date("12/31/2019"), "20193112")
    Test.assert_equals(format_date("01/15/2019"), "20191501")
