"""Burglary Series (03): Is It Gone?
Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lower cases representing the name of the pet (e.g. "rambo"), return:

"Rambo is gone..." if the name is on the list.
"Rambo is here!" if the name is not on the list.
Note that the first letter of the name in the return statement is capitalized.

Examples
 items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
} ➞ "Timmy is gone..."
# Timmy is in the dictionary.


 items = {
  "tv": 30,
  "stereo": 50,
} ➞ "Timmy is here!"
# Timmy is not in the  dictionary.


items = { } ➞ "Timmy is here!"
# Timmy is not in the dictionary.
Notes
N/A
"""

from edabit.Test import Test

def find_it(items, name):
    if name in items.keys():
        return f"{name.capitalize()} is gone..."
    else:
        return f"{name.capitalize()} is here!"


Test.assert_equals(find_it({}, "rambo"),"Rambo is here!")
Test.assert_equals(find_it({}, "heman"),"Heman is here!")
Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
}, "rocky"),"Rocky is here!")
Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
}, "spiderman"),"Spiderman is here!")
Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
	"julius": 100,
}, "julius"),"Julius is gone...")
Test.assert_equals(find_it({
  "tv": 30,
  "stereo": 50,
	"batman": 200,
}, "batman"),"Batman is gone...")