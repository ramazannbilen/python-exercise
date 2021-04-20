"""

This is an introduction to how challenges on Edabit work. In the Code tab above you'll see a starter function that looks like this:

def hello():
All you have to do is type return "hello edabit.com" on the second line and then click the Check button. If you did this correctly, the button will turn red and say SUBMIT FINAL. Click it and see what happens.

Notes
The returned string must be in all lowercase letters.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""
from edabit.Test import Test


def hello():
    """
    Summary: This method returns a string
    """
    return "hello edabit.com"


if __name__ == '__main__':
    Test.assert_equals(hello(), "hello edabit.com")
