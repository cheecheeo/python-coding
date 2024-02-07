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

# tuple indexing and slicing
tripleME0 = ("Frodo", 33, 35)
tripleME1 = ("Pippin", 28, 87)
tripleME2 = ("Legolas", tripleME0, tripleME1)

# Exercise:
pippin = tripleME2[len(tripleME2)-3:]

def reduce(f, xs, z):
    first = xs[:1]
    return z if list(first) == [] else \
           reduce(f, xs[1:], f(z, first[0]))

def reduce_john(f, xs, z):
    """
    This function: https://docs.python.org/3/library/functools.html#functools.reduce
    >>> reduce_john(lambda x, y: x * y, [1, 2, 3], 1)
    6
    >>> reduce_john(lambda x, y: x * y, [], 1)
    1
    >>> reduce_john(lambda x, y: x+y, [1, 2, 3, 4, 5], 0)
    15
    >>> reduce_john(lambda x, y: (x, y), [1, 2, 3, 4, 5], ())
    ((((((), 1), 2), 3), 4), 5)
    """
    first = xs[:1]
    return z if list(first) == [] else \
           reduce_john(f, xs[1:], f(z, first[0]))

def reduce(f, xs, z):
    """
    An if-statement rewrite of reduce_john.
    >>> reduce(lambda x, y: x * y, [1, 2, 3], 1)
    6
    >>> reduce(lambda x, y: x * y, [], 1)
    1
    >>> reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 0)
    15
    >>> reduce(lambda x, y: (x, y), [1, 2, 3, 4, 5], ())
    ((((((), 1), 2), 3), 4), 5)
    """
    first = xs[:1]
    if list(first) == []:
        return z
    else:
        return reduce(f, xs[1:], f(z, first[0]))


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
