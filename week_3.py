# Week 3 exercises
# https://docs.google.com/presentation/d/1jJSEq7pDfnVKXkB_WdiJ9qFXr3dCimJ_05KKrQ4odDk/edit?usp=sharing
# edit and change the files however you wish!

import IPython
import math

import week_1
import week_2

if_example_function = lambda x, y: \
    "x is big, y is small"   if x > 12 and y < 5 else \
    "x is small, y is small" if x < 5  and y < 5  else \
    "x is just right, I don't know about y"

if_example_1 = if_example_function(42, 3.1337)
if_example_2 = if_example_function(7, 3.1337)
# use `if_example_function` to define the following variable with the value
# "x is small, y is small"
if_example_3 = None

def if_example_function_advanced(x, y):
    x_and_y_are = ""
    if x > 12 and y < 5:
        x_and_y_are = "x is big, y is small"
    elif x < 5 and y < 5:
        x_and_y_are = "x is small, y is small"
    else:
        x_and_y_are = "x is just right, I don't know about y"
    return x_and_y_are

if_example_advanced_1 = if_example_function_advanced(3, 4)
# use `if_example_function_advanced` to define the following variable with the other
# two possible values from `if_example_function_advanced`
if_example_advanced_2 = None
if_example_advanced_3 = None

def match_example_function(x, y):
    x_and_y_are = ""
    match (x > 12, x < 5, y < 5):
        case (True, _, True):
            x_and_y_are = "x is big, y is small"
        case (_, True, True):
            x_and_y_are = "x is small, y is small"
        case (False, False, _):
            x_and_y_are = "x is just right, y is exactly " + str(y)
        case (_, _, _):
            x_and_y_are = "x is " + str(x) + " y is exactly " + str(y)
    return x_and_y_are

match_example_1 = match_example_function(3, 4)
# use `if_example_function_advanced` to define the following variable with the other
# two possible values from `if_example_function_advanced`
if_example_advanced_2 = None
if_example_advanced_3 = None

# improve this function to print 11 more lines when called.
def print_twelve_different_values():
    print("On the first day of Christmas my true love gave to me: a partridge in a pear tree")
    return None

# write and name a function...
#     to return the negated value of a number
#     to return the absolute value of a number using the function from above and the...
#       if *expression*
#       if *statement*
#       match *statement*

# rewrite week_2.increment_max_five_nonnegative using either an if expression or if statement
# rewrite week_2.increment_max_five_nonnegative using a match statement

# write a binary function `min_of_two` that returns the smallest of its arguments
# write a binary function `max_of_two` that returns the largest of its arguments

add_and_return_second = lambda x1, x2: (x2, x1 + x2)
tuple_to_binary = lambda function, tuple: function(tuple[0], tuple[1])

# write and name a function that takes "two steps" of add_and_return_second
# examples:
#    if I give this function the argumeents (1, 2) I should get back (3, 5)
#                                           (2, 3) I should get back (5, 8)
#                                           (13, 21) I should get back (34, 55)

def main():
    IPython.embed()
    print("Hello world!")
    print_twelve_different_values()

if __name__ == "__main__":
    main()