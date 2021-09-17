"""
International Greetings
Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
Write a function that takes in a name and returns a name tag, that should read:

"Hi! I'm [name], and I'm from [country]."
If the name is not in the dictionary, return:

"Hi! I'm a guest."
Examples
greeting("Randy") ➞ "Hi! I'm Randy, and I'm from Germany."

greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."

greeting("Monti") ➞ "Hi! I'm a guest."
Notes
N/A
"""

from edabit.Test import Test

GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}


def greeting(name):
    if name in list(GUEST_LIST.keys()):
        return "Hi! I'm {}, and I'm from {}.".format(name,GUEST_LIST[name])
    else:
        return "Hi! I'm a guest."

Test.assert_equals(greeting("Randy"), "Hi! I'm Randy, and I'm from Germany.")
Test.assert_equals(greeting("Sam"), "Hi! I'm Sam, and I'm from Argentina.")
Test.assert_equals(greeting("Monti"), "Hi! I'm a guest.")
Test.assert_equals(greeting("Trudy"), "Hi! I'm a guest.")
Test.assert_equals(greeting("Wendy"), "Hi! I'm Wendy, and I'm from Japan.")
