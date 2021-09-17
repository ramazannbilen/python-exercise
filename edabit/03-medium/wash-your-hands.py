"""
Wash Your Hands :)
It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.

Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.

Examples
wash_hands(8, 7) ➞ "588 minutes and 0 seconds"

wash_hands(0, 0) ➞ "0 minutes and 0 seconds"

wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
Notes
Consider a month has 30 days.
Wash your hands.
"""

from edabit.Test import Test

def wash_hands(N, nM):
    totalsec = nM * 30 * N * 21   # I can use divmod() also.
    exactmin = totalsec // 60
    exactsec = totalsec % 60
    return f"{exactmin} minutes and {exactsec} seconds"

Test.assert_equals(wash_hands(8, 7),	"588 minutes and 0 seconds")
Test.assert_equals(wash_hands(20, 10), "2100 minutes and 0 seconds")
Test.assert_equals(wash_hands(7, 9),	"661 minutes and 30 seconds")
Test.assert_equals(wash_hands(0, 2),	"0 minutes and 0 seconds")
Test.assert_equals(wash_hands(13, 3), "409 minutes and 30 seconds")
Test.assert_equals(wash_hands(1, 1), "10 minutes and 30 seconds")
Test.assert_equals(wash_hands(7, 0), "0 minutes and 0 seconds")