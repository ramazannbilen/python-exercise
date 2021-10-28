"""CAPS LOCK DAY is over!
October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.

Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end.

Examples
normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"

normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."

normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."
Notes
Each string is a sentence and should start with an uppercase character."""

from edabit.Test import Test

def normalize(txt):
    if txt.isupper() == True:
        return (txt.upper()).capitalize() + "!"
    else:
        return txt


Test.assert_equals(normalize("CAPS LOCK DAY IS OVER"), "Caps lock day is over!", )
Test.assert_equals(normalize("Today is not caps lock day."), "Today is not caps lock day.")
Test.assert_equals(normalize("WE WANT THIS COVID THING TO BE OVER"), "We want this covid thing to be over!")
Test.assert_equals(normalize("Let us stay calm, no need to panic."), "Let us stay calm, no need to panic.")
Test.assert_equals(normalize("DO NOT SHOUT"), "Do not shout!")
Test.assert_equals(normalize("Civilized conversation."), "Civilized conversation.")