"""Fullname and Email
Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.
Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"
Notes
The attributes firstname and lastname are already made for you.
See the Resources tab for some helpful tutorials on Python classes!
"""

from edabit.Test import Test


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = firstname.lower() + "." + lastname.lower() + "@company.com"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")
emp_4 = Employee("Joshua", "Senoron")

Test.assert_equals(emp_1.firstname, "John")
Test.assert_equals(emp_1.lastname, "Smith")
Test.assert_equals(emp_1.fullname, "John Smith")
Test.assert_equals(emp_1.email, "john.smith@company.com")
Test.assert_equals(emp_2.firstname, "Mary")
Test.assert_equals(emp_2.lastname, "Sue")
Test.assert_equals(emp_2.fullname, "Mary Sue")
Test.assert_equals(emp_2.email, "mary.sue@company.com")
Test.assert_equals(emp_3.firstname, "Antony")
Test.assert_equals(emp_3.lastname, "Walker")
Test.assert_equals(emp_3.fullname, "Antony Walker")
Test.assert_equals(emp_3.email, "antony.walker@company.com")
Test.assert_equals(emp_4.firstname, "Joshua")
Test.assert_equals(emp_4.lastname, "Senoron")
Test.assert_equals(emp_4.fullname, "Joshua Senoron")
Test.assert_equals(emp_4.email, "joshua.senoron@company.com")
