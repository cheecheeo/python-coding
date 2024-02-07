"""
Week 8 exercises
https://docs.google.com/presentation/d/1zdyUYW7LCaMZtY8L-QB1NBUz5pZE3sRZt0J5YpywfGM/edit?usp=sharing
edit and change the files however you wish!
"""

import doctest

def range_john(n):
    """
    Homebrew range function
    >>> range_john(5)
    [0, 1, 2, 3, 4]
    >>> range_john(3)
    [0, 1, 2]
    >>> range_john(1)
    [0]
    >>> range_john(0)
    []
    >>> range_john(12) == list(range(12))
    True
    """
    def helper(n):
        return [] if n < 0 else helper(n-1) + [n]
    return helper(n-1)

# Exercise define another range function that takes a value n, and returns the
# list [0, 1, 2 .. n] rather than [0, 1, 2, .. (n-1)]
def range1(n):
    """
    A better range function.
    >>> range1(5)
    [0, 1, 2, 3, 4, 5]
    >>> range1(3)
    [0, 1, 2, 3]
    >>> range1(1)
    [0, 1]
    >>> range1(0)
    [0]
    >>> len(range1(12)) == len(range_john(12)) + 1
    True
    """
    return None

is_zero = lambda n: n == 0
is_one = lambda n: n == 1
increment = lambda n: n + 1
decrement = lambda n: n - 1

# Exercise complete the addition function using recursion. Using only the functions increment,
# decrement, and is_zero provided and an if-statement or if-expression.
def addition(x, y):
    """
    Addition function. You can assume that the argument `y` is always 0 or greater. x + y
    Idea:
    Decrement y and increment x until y is 0, then return x.
    See slide 11 here: https://v.gd/pKz6jl
    >>> addition(5, 3)
    8
    >>> addition(5, 0)
    5
    >>> addition(0, 5)
    5
    """
    return x + y

# Exercise complete the multiplication function using recursion. Use only the functions increment,
# decrement, is_zero, is_one, and addition provided and an if-statement or if-expression.
def multiplication(x, y):
    """
    Multiplication function. You can assume that the argument `y` is always 0 or greater. x * y
    Idea:
    Decrement y and add x to the the recursive call of multiplication with y decremented.
    Base cases:
    If y is 0 then return 0
    If y is 1 then return x
    >>> multiplication(3, 3)
    9
    >>> multiplication(5, 3)
    15
    >>> multiplication(5, 0)
    0
    >>> multiplication(0, 5)
    0
    """
    return x * y

# Exercise: write a binary function that takes a month in
# numeric form (1-12) (January = 1, December = 12) a number of days as an integer.
# If the number of days is greater than half of the number
# of days in the month then return True, otherwise return False.
def more_than_half_of_the_month(x, y):
    """
    Examples:
    >>> more_than_half_of_the_month(1, 20)
    True
    >>> more_than_half_of_the_month(2, 10)
    False
    """

    return None

# Exercise: write a unary function that takes a tuple with the form:
#   (Name, Identification number, Month, Day) with type (str, int, int, int)
# If the number of days is greater than half of the number of days in the month
# then return the Name from the tuple otherwise return None
def name_me(name_me_tuple):
    """
    Examples:
    >>> name_me(("Julie", 12345, 1, 20))
    "Julie"
    >>> name_me(("Bob", 12344, 2, 10))
    None
    """

    return None

def main():
    """
    Main function. doctest and ipython
    >>> is_zero(0)
    True
    >>> is_zero(12)
    False
    >>> increment(0)
    1
    >>> increment(12)
    13
    >>> decrement(1)
    0
    >>> decrement(12)
    11
    """

    doctest.testmod()

if __name__ == "__main__":
    main()
