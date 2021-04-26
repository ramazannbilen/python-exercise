"""
Check if objOne Is Equal to objTwo
Create a function that checks to see if two object arguments are equal to one another. Return True if the objects are equal, otherwise, return False.

Examples
# The first object parameter.

obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
➞ False
# The first object parameter.

obj_one = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
➞ True
Notes
If you have a suggestion on how to make these instructions easier to understand, please leave a comment. Your feedback is greatly appreciated.
"""

from edabit.Test import Test


def is_equal(obj_one, obj_two):
    if obj_one == obj_two:
        return True
    else:
        return False


if __name__ == '__main__':
    obj_one = {
        "name": "Benny",
        "phone": "3325558745",
        "email": "benny@edabit.com"
    }

    obj_two = {"name": "Jason", "phone": "9853759720", "email": "jason@edabit.com"}

    Test.assert_equals(is_equal(obj_one, obj_two), False)

    obj_one = {
        "name": "Jason",
        "phone": "9853759720",
        "email": "jason@edabit.com"
    }

    obj_two = {
        "name": "Jason",
        "phone": "9853759720",
        "email": "jason@edabit.com"
    }

    Test.assert_equals(is_equal(obj_one, obj_two), True)

    obj_one = {
        "names": ["Tom", "Joe", "David"],
        "fruitIds": {
            "orangeId": 77634,
            "appleId": 74323,
            "bananaId": 19487
        }
    }

    obj_two = {
        "names": ["Tom", "Joe", "Steve"],
        "fruitIds": {
            "orangeId": 77634,
            "appleId": 74323,
            "bananaId": 65970
        }
    }

    Test.assert_equals(is_equal(obj_one, obj_two), False)

    obj_one = {
        "foo": {
            "bar": {
                "baz": True
            },
            "baz": {
                "arr": [1, 2, 3]
            }
        }
    }

    obj_two = {
        "foo": {
            "bar": {
                "baz": True
            },
            "baz": {
                "arr": [3, 2, 1]
            }
        }
    }

    Test.assert_equals(is_equal(obj_one, obj_two), False)

    obj_one = {
        "foo": {
            "bar": {
                "baz": "edabit.com"
            },
            "baz": {
                "userIds": {
                    "jason": 76397,
                    "steve": 73073,
                    "joe": 21076
                }
            }
        }
    }

    obj_two = {
        "foo": {
            "bar": {
                "baz": "edabit.com"
            },
            "baz": {
                "userIds": {
                    "jason": 76397,
                    "steve": 73073,
                    "joe": 21076
                }
            }
        }
    }

    Test.assert_equals(is_equal(obj_one, obj_two), True)
