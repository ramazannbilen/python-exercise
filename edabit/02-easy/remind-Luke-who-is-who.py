"""
Luke, I Am Your ...
Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."
"""

from edabit.Test import Test


def relation_to_luke(name):
    family = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"} # dict{} is a array that you can put a value to all index after : sign.
    return "Luke, I am your " + family.get(name) + "."


if __name__ == '__main__':
    Test.assert_equals(relation_to_luke("Darth Vader"), "Luke, I am your father.")
    Test.assert_equals(relation_to_luke("Leia"), "Luke, I am your sister.")
    Test.assert_equals(relation_to_luke("Han"), "Luke, I am your brother in law.")
    Test.assert_equals(relation_to_luke("R2D2"), "Luke, I am your droid.")
