"""
Get the Area of a Country
Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

Examples
area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"

area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"

area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"
Notes
The total world's landmass is 148,940,000 [Km^2]
Round the result to two decimal places.
If you get stuck on a challenge, find help in the Resources tab.
"""

from edabit.Test import Test


def area_of_country(name, area):
    return f"{name} is {round((area / 148940000 * 100), 2)}% of the total world's landmass"


if __name__ == '__main__':
    Test.assert_equals(area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass")
    Test.assert_equals(area_of_country("Russia", 17098242), "Russia is 11.48% of the total world's landmass")
    Test.assert_equals(area_of_country("Iran", 1648195), "Iran is 1.11% of the total world's landmass")
    Test.assert_equals(area_of_country("India", 3287590), "India is 2.21% of the total world's landmass")
    Test.assert_equals(area_of_country("China", 9706961), "China is 6.52% of the total world's landmass")
    Test.assert_equals(area_of_country("Yemen", 527968), "Yemen is 0.35% of the total world's landmass")
    Test.assert_equals(area_of_country("Switzerland", 41284), "Switzerland is 0.03% of the total world's landmass")
