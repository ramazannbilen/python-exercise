"""Get Students with Names and Top Notes
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
Notes
N/A"""

from edabit.Test import Test

def top_note(student):
    student["top_note"] = student["notes"]
    del student["notes"]
    student["top_note"] = max(list(student.values())[1])
    return student

Test.assert_equals(top_note({"name": "Jacek", "notes":[5, 4, 3]}), {"name": "Jacek", "top_note":5})
Test.assert_equals(top_note({"name": "Ewa", "notes":[3,3,3]}), {"name": "Ewa", "top_note":3})
Test.assert_equals(top_note({"name": "Zygmund", "notes":[1,2,3]}), {"name": "Zygmund", "top_note":3})
Test.assert_equals(top_note({"name": "Alex", "notes":[1,4,6]}), {"name": "Alex", "top_note":6})