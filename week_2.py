"""
Week 2 exercises
https://docs.google.com/presentation/d/1gHHt_LSXOmigaETN11ub2eJX0QpC1ooak0oDJd--XLA/edit?usp=sharing
edit and change the files however you wish!
"""

import IPython

import week_1

# like saying
# tithe(x) = let one_tenth...
#            in one_tenth
def tithe(x):
    one_tenth = x/10
    return one_tenth

def times_ten(x):
    product_of_10 = x * 10
    return product_of_10

tithe_lambda = lambda x: x/10
# rewrite times_ten using the lambda keyword
times_ten_lambda = None

# the `min` function always returns the minimum of two values
# assign the `min` of 12 and 5 to the following variable
min_12_5 = None
# assign the `min` of 42 and 5 to the following variable
min_42_5 = None
# follow the pattern according the variable names
min_0_negative_1 = None
min_5_5 = None
min_5_3 = None
min_5_3_0 = min(5,min(3,0)) # pylint: disable=nested-min-max
min_5_3_12 = None
min_5_30_12 = None

increment = lambda x: x + 1
# write a function that takes a number, increments it and then returns it or
# 5, whichever is smallest. use the 'increment' function provided.
def increment_max_five(x):
    return None

# write a function that takes a number, increments it and then returns it or
# 5, whichever is smallest. return a minimum of 0. use the `increment_max_five`
# function in your solution
def increment_max_five_nonnegative(x):
    return None

# write the above function using the lambda keyword, don't use the
# `increment_max_five_nonnegative` function
increment_max_five_nonnegative_lambda = None

# write and name the python function that corresponds to the math function
# f(x) = 5x + 7
# and its inverse function

# write and name the python function that corresponds to the math function
# f(x) = 12x + 5
# and its inverse function

# write and name the python function that corresponds to the math function
# f(x, y) = 12x + 5y + 3

# write and name the python function that corresponds to the math function
# f(x) = xe^x
# hint: math.exp(12) = e^12
# hint: math.log(exp(x)) = x

def main():
    IPython.embed()
    print("Hello world!")
    print(tithe(week_1.xInt))
    print(week_1.xInt)
    print(week_1.double(week_1.xInt))

if __name__ == "__main__":
    main()