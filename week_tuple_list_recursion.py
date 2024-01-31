"""
Future work exercises
https://docs.google.com/presentation/d/1BNARjfGXtRCFCsGdxFB-c6XXUyrkgVsWAE2e4rA7kuA/edit?usp=sharing
also read, familiarize, get some questions ready from:

edit and change the files however you wish!
"""

import doctest
import IPython

# TODO move to xdoctest
# student REPL and development environment
# Exercise: write the sum_analog_of_factorial function.
# TODO: slicing, match statement - homework, redo ifs with the match statement
# slicing - take, drop, slice
# maximum element in a list
# count - python function

# logN function recursive

# Exercise complete the addition function using recursion. Using only the functions
# addition function recursive - provide only increment and decrement function
def addition(x, y):
    """
    Addition function. You can assume that the argument `y` is always 0 or greater. x + y
    Idea:
    Decrement y and increment x until y is 0, then return x.
    >>> addition(5, 3)
    8
    >>> addition(5, 0)
    5
    >>> addition(0, 5)
    5
    """
    return x + y

def range_week_7(n):
    """
    Homebrew range function
    >>> range_week_7(12) == list(range(12))
    True
    """
    def helper(n):
        return [] if n < 0 else helper(n-1) + [n]
    return helper(n-1)

# Exercise complete the power function using recursion.
def power(x, y):
    """
    The power function. You can assume that the argument `y` is always 0 or greater. Some examples:
    >>> power(2, 2)
    4
    >>> power(3, 2)
    9
    >>> power(3, 3)
    27
    >>> power(0, 0)
    1
    >>> power(3, 1)
    3
    >>> power(3, 0)
    1
    """
    return x ** y

def is_even(n):
    return None

def is_odd(n):
    return None

def length(tuple_list):
    return None

def construct(element, tuple_list):
    return None

def pop(tuple_list):
    return None

def unconstruct(tuple_list):
    return (None, None)

# Exercise: define pop using unconstruct

def remove(tuple_list, x):
    """
    >>> remove(from_list(range(0,5)), 3) == from_list([0,1,2,4,5]) # doctest: +SKIP
    True
    """
    return None

def last(tuple_list):
    return None

def insert_end(tuple_list):
    return None

def index(tuple_list):
    return None

def from_list(list0):
    return () if list0 == [] else \
           (list0[0], from_list(list0[1:]))

def to_list(tuple_list):
    return [] if tuple_list[0:] == () else \
           [tuple_list[0]] + to_list(tuple_list[1:][0])

def main():
    doctest.testmod()
    IPython.embed()

if __name__ == "__main__":
    main()
