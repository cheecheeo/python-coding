# Week 1 exercises
# https://docs.google.com/presentation/d/12dIIoWzSk9o9POnC4bupmDM8N0ZtsyrtAFAi5qBhJDs/edit?usp=sharing
# edit and change the files however you wish!

import math

xInt = 42
xBool = True
xFloat = 0.42

# Truth tables.
# Follow the examples below for the operators and, or, and not.
# Replace the None's with a logical statement
or_bool_1 = True or True
or_bool_2 = None
or_bool_3 = None
or_bool_4 = None

and_bool_1 = True and True
and_bool_2 = None
and_bool_3 = None
and_bool_4 = None

not_bool_1 = not True
not_bool_2 = None

double = lambda x: x * 2
square = lambda x: x * x

double_then_square = lambda x: square(double(x))
# TODO
square_then_double = lambda x: None

# TODO
# if the double function is x * 2, what is the triple function?
triple = lambda x: None
# TODO
# if the square function is x * x, what is the cube function?
cube = lambda x: None

# n-ary functions
# TODO
# write a function that takes two int or float arguments, and adds
# them together after cubing the first arguent and tripling the second
# argument
exercise_1 = lambda x, y: None

# TODO
# same as above but it should multiply them instead of adding them
exercise_2 = lambda x, y: None

# TODO
# write any two 2-argument functions and describe what they do in the comments.
# Remember to write the 'lambda x, y:'
exercise_3 = None

# TODO
# write a function that takes three arguments, and adds them all together
# after cubing the first arguent, tripling the second argument, and
# doubling the third argument.
exercise_4 = None

def main():
    print("Hello world!")
    print(double(xInt))
    print(square(xInt))

if __name__ == "__main__":
    main()