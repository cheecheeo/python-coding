"""
Week 6 exercises
https://docs.google.com/presentation/d/1BNARjfGXtRCFCsGdxFB-c6XXUyrkgVsWAE2e4rA7kuA/edit?usp=sharing
also read, familiarize, get some questions ready from:

edit and change the files however you wish!
"""

import doctest
import IPython

# The `if` expression looks like:
#
# EXPRESSION if BOOLEAN EXPRESSION else EXPRESSION

# The `if` statement looks like:
#
# if BOOLEAN EXPRESSION:
#     STATEMENTS_1        # Executed if condition evaluates to True
# else:
#     STATEMENTS_2        # Executed if condition evaluates to False

# Exercise: Write and name 3 functions that each return a string based upon the following tables:
#
# string argument|string response
# ---------------+------------------------------------------------
# Elf            |Welcome, Elf! You are wise and immortal.
# Dwarf          |Welcome, Dwarf! You are sturdy and great at crafting.
# Hobbit         |Welcome, Hobbit! You are brave and have a love for comfort.
# Human          |Welcome, Human! You can excel in many disciplines, choose one!
#
# string argument|string response
# ---------------+--------------------------------------------
# Sword          |You chose a sword. Good for close combat.
# Bow            |You chose a bow. Good for ranged combat.
# Staff          |You chose a staff. Best for casting spells.
#
# string argument|string response
# ---------------+--------------------------------------------
# Moria          |You chose to go through Moria. Beware of the Balrog!
# Caradhras      |You chose to cross Caradhras. Beware of the snowstorm!
# Gap of Rohan   |You chose to pass through the Gap of Rohan. Beware of the Uruk-hai!

# for each triple of the format (name, int, float) assume that the int value is an identification
# and the float value is an age
hobbits = (("Frodo", 1, 33.7), ("Sam", 2, 35.4), ("Pippin", 3, 28.9))
fellows = (("Aragorn", 4, 87.0), ("Legolas", 5, 2931.5), ("Gimli", 6, 139.1))
wizards = (("Gandalf", 7, 2019.0), ("Saruman", 8, 2025.0), ("Radagast", 9, 1980.0))

# Exercise: Name and assign variables with the following attributes
# 1. a triple with the ages of all the hobbits
# 2. a 9-tuple with all ages
# 3. a triple with the ages of Pippin, Gimli, and Radagast
# 4. a sum of the ages of all the wizards
# 5. a string with all the names of the fellows concatenated together, with a space in between
#    each name

x = 42
y = "John"
z = 73.7

t = (x, y, z)
t0 = (t, z, y)
t1 = (t0, t)
t2 = (t, t1, z)

left = 1
right = 3
tree0 = (2, left, right)
right_left = 5
right_right = 7
tree1 = (6, right_left, right_right)
# tree2 has depth 3
tree2 = (4, tree0, tree1)
# Exercise: define a variable `tree3` with depth 3 holding both int and
# float values

treeME0 = ("Frodo", 33, 35)
treeME1 = ("Pippin", 28, 87)
treeME2 = ("Legolas", treeME0, treeME1)

treeME3 = ("Gimli", 139, 2019)
treeME4 = ("Saruman", 2025, 1980)
treeME5 = ("Gandalf", treeME3, treeME4)

treeME6 = ("Middle Earth", treeME2, treeME5)

"""
Exercise: Name and assign variables with the following values from treeME6 (tuples):
1. "Middle Earth"
2. 1980
3. "Frodo"
4. 35
5. 33
6. "Legolas"
7. 2025
"""

example_pippin = treeME6[1][2][0]

def main():
    """
    Some tests that should pass for this module:
    >>> tree2[1][1]
    1
    >>> treeME6[1][2][2]
    87
    >>> example_pippin
    'Pippin'
    """

    doctest.testmod()
    IPython.embed()

if __name__ == "__main__":
    main()
