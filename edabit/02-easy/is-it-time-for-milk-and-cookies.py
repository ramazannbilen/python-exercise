"""
Is it Time for Milk and Cookies?
Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.

Examples
time_for_milk_and_cookies(datetime.date(2013, 12, 24)) ➞ True

time_for_milk_and_cookies(datetime.date(2013, 1, 23)) ➞ False

time_for_milk_and_cookies(datetime.date(3000, 12, 24)) ➞ True
Notes
All test cases contain valid dates.
"""

from edabit.Test import Test
import datetime


def time_for_milk_and_cookies(date):
    if date.day == 24 and date.month == 12:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(time_for_milk_and_cookies(datetime.date(2013, 12, 24)), True)
    Test.assert_equals(time_for_milk_and_cookies(datetime.date(3000, 12, 24)), True)
    Test.assert_equals(time_for_milk_and_cookies(datetime.date(2013, 1, 23)), False)
    Test.assert_equals(time_for_milk_and_cookies(datetime.date(2010, 11, 2)), False)
    Test.assert_equals(time_for_milk_and_cookies(datetime.date(1980, 9, 24)), False)
