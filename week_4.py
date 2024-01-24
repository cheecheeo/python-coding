"""
Week 4 exercises
https://docs.google.com/presentation/d/1MT80l7w4i3x0oK6uXbcqqQTnPOSBLB9RCgqurdqTqQY/edit?usp=sharing
edit and change the files however you wish!
"""

import IPython

t2 = (5, "hello")
t3 = ("John", "Jacob", 25)
# create 3 more tuples of length 4, 5, and 6
t4 = None
t5 = None
t6 = None
# note: tuples can be of length 1 and 0
t1 = (42,)
t0 = ()

# Exercise
# open up a python interpreter - python or IPython and test the `len` function
# on t0, t1, ... t5

# Exercise
# name and write a nullary (no arguments) function that returns True if the
# following pattern is true otherwise False:
# the length of t0 is 1
# the length of t1 is 2
# ...
# the length of t6 is 5

# following the pattern, assign each of the variables below with their corresponding
value_first_t0 = None
value_first_t1 = t1[0]
value_first_t2 = None
value_second_t2 = t2[1]
value_third_t2 = None
# ...
value_first_t6 = None
# ...
value_sixth_t6 = None

# Exercise
# name and write a unary function that takes a tuple of arbitrary length and
# always returns the first element of the tuple

# Exercise
# name and write a function that takes a tuple of arbitrary length and always
# returns the last element of the tuple

# Exercise
# name and write a binary function that takes a tuple of arbitrary length and
# an index i and returns the value at index i (0..)

# Exercise
# write a binary function named `one_based_index` that takes a tuple of
# arbitrary length and an index i and returns the value at index i-1

# Exercise
# name and write a ternary function that takes a tuple t, an index i, and
# a value v and returns the value at index i if i < len(t) otherwise returns
# v

def main():
    IPython.embed()

if __name__ == "__main__":
    main()