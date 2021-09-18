"""
Incorrect Import Statement
When importing objects from a module in Python, the syntax usually is as follows:

from module_name import object
Given a string of an incorrect import statement, return the fixed string. All import statements will be the wrong way round.

Examples
fix_import("import object from module_name") ➞ "from module_name import object"

fix_import("import randint from random") ➞ "from random import randint"

fix_import("import pi from math") ➞ "from math import pi"
Notes
All Tests will be valid strings.
"""

from edabit.Test import Test

def fix_import(s):
    y = s.split(" ", 2)
    a = y[-1]
    y.pop(-1)
    y.insert(0, a)
    return " ".join(y)

Test.assert_equals(fix_import("import object from module_name"), "from module_name import object")
Test.assert_equals(fix_import("import randint from random"), "from random import randint")
Test.assert_equals(fix_import("import pi from math"), "from math import pi")