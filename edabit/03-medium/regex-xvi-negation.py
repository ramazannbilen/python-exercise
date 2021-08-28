"""RegEx XVI: Negation
The caret ^, when found at the start of a characer set, is the equivalent to "not" in RegEx. The regular expression [^a-c] matches any characters except "a", "b" and "c". Write the regular expression that matches any characters except letters, digits and spaces. You must use a negated character set in your expression.

Examples
txt = " alice15@gmail.com "
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["@", "."]
Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
Find more info on RegEx and negation in Resources.
You can find all the challenges of this series in my Basic RegEx collection."""

from edabit.Test import Test

import re

pattern = "[^a-w,^0-9,^ ]" #RegEx mean Regular Expression and has a lots of diff examples, look for it.

txt = ' alice15@gmail.com '

Test.assert_equals('[^' in pattern, True)
Test.assert_equals(re.findall(pattern, txt), ['@', '.'])

# Note from the original:
# Credits to https://javascript.info/regexp-character-sets-and-ranges

# Translated from JavaScript.
# The RegEx series was originally posted by Isaac Pak.
