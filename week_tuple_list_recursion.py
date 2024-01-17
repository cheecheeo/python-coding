# Week 5 exercises
# TODO
# edit and change the files however you wish!

import IPython
import math

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

def factorial(n):
    return None

def is_even(n):
    return None

def is_odd(n):
    return None

def length(tuple_list):
    return None

def construct(element, tuple_list):
    return None

def unconstruct(tuple_list):
    return (None, None)

def last(tuple_list):
    return None

def insert_end(tuple_list):
    return None

def from_list(list0):
    return () if list0 == [] else \
           (list0[0], from_list(list0[1:]))

def to_list(tuple_list):
    return [] if tuple_list[0:] == () else \
           [tuple_list[0]] + to_list(tuple_list[1:][0])

def main():
    IPython.embed()

if __name__ == "__main__":
    main()