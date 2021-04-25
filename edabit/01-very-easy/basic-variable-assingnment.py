"""
Basic Variable Assignment
A student learning Python was trying to make a function. His code should concatenate a passed string name with string "Edabit" and store it in a variable called result. He needs your help to fix this code.

Examples
name_string("Mubashir") ➞ "MubashirEdabit"

name_string("Matt") ➞ "MattEdabit"

name_string("python") ➞ "pythonEdabit"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test

def name_string(name):
	b = "Edabit"        #default was "==" and I correct it.
	result = name + b   #default was "==" and I correct it.
	return result


if __name__ == '__main__':
    Test.assert_equals(name_string("Mubashir"), "MubashirEdabit")
    Test.assert_equals(name_string("Matt"), "MattEdabit")
    Test.assert_equals(name_string("python"), "pythonEdabit")
    Test.assert_equals(name_string("Airforce"), "AirforceEdabit")