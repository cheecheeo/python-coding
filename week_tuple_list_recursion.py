"""
Future work exercises
https://docs.google.com/presentation/d/1BNARjfGXtRCFCsGdxFB-c6XXUyrkgVsWAE2e4rA7kuA/edit?usp=sharing
also read, familiarize, get some questions ready from:

edit and change the files however you wish!
"""

import IPython

# Exercise: write the sum_analog_of_factorial function.

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
