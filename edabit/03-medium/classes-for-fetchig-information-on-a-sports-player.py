"""
Classes For Fetching Information on a Sports Player
Create a class that takes the following four arguments for a particular football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"
Examples
 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"
Notes
name will be passed in as a string and age, height, weight will be integers.
"""

from edabit.Test import Test


class player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"
    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"


player1 = player('Patrick Mahomes', 24, 188, 104)
player2 = player('Jimmy Garoppolo', 28, 188, 102)
player3 = player('Julio Jones', 31, 191, 100)

Test.assert_equals(player1.get_age(), 'Patrick Mahomes is age 24')
Test.assert_equals(player1.get_height(), 'Patrick Mahomes is 188cm')
Test.assert_equals(player1.get_weight(), 'Patrick Mahomes weighs 104kg')

Test.assert_equals(player2.get_age(), 'Jimmy Garoppolo is age 28')
Test.assert_equals(player2.get_height(), 'Jimmy Garoppolo is 188cm')
Test.assert_equals(player2.get_weight(), 'Jimmy Garoppolo weighs 102kg')

Test.assert_equals(player3.get_age(), 'Julio Jones is age 31')
Test.assert_equals(player3.get_height(), 'Julio Jones is 191cm')
Test.assert_equals(player3.get_weight(), 'Julio Jones weighs 100kg')
