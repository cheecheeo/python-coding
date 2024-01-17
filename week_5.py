# Week 5 exercises
# https://docs.google.com/presentation/d/1sXtDIGdlu_YTTsv8n7s1CibdBqHnFPXYqD32cgBD6sE/edit#slide=id.p
# also read, familiarize, get some questions ready from:
# https://openbookproject.net/thinkcs/python/english3e/tuples.html
# https://openbookproject.net/thinkcs/python/english3e/conditionals.html
# edit and change the files however you wish!

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

# write and name a function...
#     to return the negated value of a number
#     to return the absolute value of a number using the function from above and the...
#       if *expression*
#       if *statement*

def negate(n):
    return -n

def is_positive(n):
    return n > 0

# p if b else q
def absolute_value(n):
    # n if n is positive
    # negate(n) if n is negative
    return n if n > 0 else negate(n)

# if b:
#   p
# else:
#   q
def absolute_value_statement(g):
    if g > 0:
        return g
    else:
        return negate(g)

def absolute_value_statement2(n):
    the_number = 0
    if n > 0:
        the_number = n
    else:
        the_number = negate(n)
    return the_number

def min_john(x, y):
    if x < y:
        return x
    else:
        return y
    
def max_john(x,y):
    if x > y:
        return x
    else:
        return y

# rewrite week_2.increment_max_five_nonnegative using either an if expression or if statement
def increment_max_five2(max_five):
    # increment max_five
    # make sure max_five is greater than 0
    # return the smallest of 5 or max_five
    # no min or max functions
    return None

# write a binary function `min_of_two` that returns the smallest of its arguments
# write a binary function `max_of_two` that returns the largest of its arguments

# write a binary function `min_of_three` that returns the smallest of its arguments
# hint: you can use min_of_two to to solve this
# write a binary function `max_of_three` that returns the largest of its arguments
# hint: you can use max_of_two to to solve this

# Exercise: Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday
# to Saturday. Write a function which is given the day number, and it returns
# the day name (a string).

# Exercise: Write a function named `letter_grade` that takes a number (0-100)
# and returns a letter grade according to the following table as a string:
# 100           A+
# 90 or more    A
# 80 or more    B
# 70 or more    C
# 60 or more    D
# 0 or more     F

north_description = "A dark hallway with the sound of a trumpet playing."
east_description = "A wall blocks your way."
south_description = "A double door opens to the outdoors."
west_description = "A wall with a shelf in front of it blocks your way."

# Exercise: write a binary function that takes a tuple of integer coordinates
# and a string, one of ["N", "E", "S", "W"], and returns a string and tuple
# with it's coordinates transformed according to the following table.
#
# string argument|string response    |coordinate transformation
# ---------------+-------------------+-------------------------
# N              |north_description  |(+0, +1)
# E              |east_description   |(+1, +0)
# S              |south_description  |(+0, -1)
# W              |west_description   |(-1, +0)
#
# example:
# >>> function_name("N", (2, 3))
# ("A dark hallway with the sound of a trumpet playing.", (2, 4))
# 
# note, for the coordinate transformation the individual elements of the tuple
# should be modified accordingly

add_and_return_second = lambda x1, x2: (x2, x1 + x2)
tuple_to_binary = lambda function, tuple: function(tuple[0], tuple[1])

# Exercise: write and name a function that takes "two steps" of 
# add_and_return_second
#
# examples:
# >>> function_name(1, 2)
# (3, 5)
# >>> function_name(2, 3)
# (5, 8)
# >>> function_name(13, 21)
# (34, 55)

def main():
    IPython.embed()

if __name__ == "__main__":
    main()