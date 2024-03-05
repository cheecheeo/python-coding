"""
Week 10 exercises
scalar vs. vector types
scalars as vector types: binary numbers
vectors as scalar types: strings
string constants
string functions

video game design
    logic, puzzle games
    real time games
    role playing games

references:
https://docs.python.org/3/library/string.html
https://docs.python.org/3/library/stdtypes.html#string-methods
edit and change the files however you wish!
"""

a = 42
print(a)
print(bin(a))
b = 1337
print(b)
print(bin(b))

"""
b1, b2, b3, b4 = (True, False, False, True)
print(b1 and b2)
print(b2 or b3)
print(not b4)
b5, b6, b7, b8 = (0b1, 0b0, 0b0, 0b1)
print(bin(b5 & b6))
print(bin(b6 | b7))
print(bin(b5 ^ b8))
print(b6 ^ b7)
print(b5 ^ b6)
print(b7 ^ b8)
# note: x ^ x = 0 always

# negative numbers are a bit weird
c = -12
print(c)
print(bin(c))
print(bin(12))
print(bin(~ b8))
print(bin(b8))

blist1 = (True, False, True, False, True, False)
blist2 = 42

# strings are a type that is really a vector but usually thought of as a scalar
# joining strings
s1 = "hello"
s2 = '&'
s3 = '''mozart'''
s4 = TODO"vivaldi"TODO
print(' '.join((s1, s3, s2, s4)))
# this is a quicker way to write:
print(s1 + " " + s3 + " " + s2 + " " + s4)

# remember functions have different "fixities":
#   prefix: f(x, y)
#   infix: x f y. examples: 3 + 5, 5 ** 2
#   postfix: x.f(y). examples ' '.join("hello"), 3!

# for each of the examples below join the strings with ' ', '-', and '_'
str1 = "Hello"
str2 = "World"
print(TODO.join(TODO))

str3 = "Python"
str4 = "Programming"
print(TODO.join(TODO))

str5 = "Good"
str6 = "Morning"
str7 = "Robert"
print(TODO.join(TODO))

# splitting strings
sentence1 = "Python is versatile"
words1 = sentence1.split()
print(words1)

# for each of the examples below make all of the length tests print True
sentence2 = "Data science is fascinating"
words2 = sentence2.split()
print(words2)
print(len(words2) == 0)

sentence3 = "Machine learning is powerful"
words3 = sentence3.split()
print(words3)
print(len(words3) == 0)

# for each of the examples below make all of boolean print statements print True
text1 = "I like apples"
new_text1 = text1.replace('apples', 'bananas')
print(new_text1)
print("I like cheese" == new_text1)

text2 = "Python is fun"
new_text2 = text2.replace('fun', 'exciting')
print(new_text2)
print("Python is very very very..." == new_text2)

text3 = "I love chocolate"
new_text3 = text3.replace('chocolate', 'ice cream')
print(new_text3)
print("I love chocolate ice cream" == new_text3)

# for each of the examples below make all of boolean print statements print True
text1 = "     Hello     "
stripped_text1 = text1.strip()
print(stripped_text1)
print(stripped_text1 == "Hehe yello")

text2 = "     Python     "
stripped_text2 = text2.rstrip()
print(stripped_text2)
print(stripped_text2 == "     Pylonthon")

text3 = "     Data Science     "
stripped_text3 = text3.lstrip()
print(stripped_text3)
print(stripped_text3 == "Database Science     ")

# casefolding is basically a more powerful lowercasing
# this first example is a bit tricky
text1 = "HELLO World"
lower_text1 = text1.casefold()
print(lower_text1)
print(lower_text1 == "Goodbye world")

text2 = "GooD MorNING"
lower_text2 = text2.casefold()
print(lower_text2)
print(lower_text2 == "good morning glory")

text3 = "PyThOn ProGrAmMiNg"
lower_text3 = text3.casefold()
print(lower_text3)
print(lower_text3 == "python brogramming")

text1 = "Welcome to the party"
starts_with_welcome1 = text1.startswith("Well-come")
print(starts_with_welcome1)

text2 = "Good morning, everyone"
starts_with_good1= text2.startswith("Good morning glory")
print(starts_with_good1)

text3 = "Python is a programming language"
starts_with_python= text3.startswith("Pyth0n")
print(starts_with_python)

text1 = "See you later, goodbye"
ends_with_goodbye = text1.endswith("goodbye")

text2 = "The show is over, goodbye!"
ends_with_goodbye_2 = text2.endswith("goodbye")

text3 = "It's time to say goodbye"
ends_with_goodbye_3 = text3.endswith("goodbye")

multiline_text_1= TODO"Line 1\nLine 2\nLine 3"TODO
lines_1 = multiline_text_1.splitlines()

multiline_text_2= TODO"First line\nSecond line\nThird line"TODO
lines_2 = multiline_text_2.splitlines()

multiline_text_3 = TODO"One\nTwo\nThree"TODO
lines_3 = multiline_text_3.splitlines()

text_1 = "hello, world!"
capitalized_text_1 = text_1.capitalize()

text_2 = "good morning, everyone!"
capitalized_text_2 = text_2.capitalize()

text_3 = "data science is interesting!"
capitalized_text_3 = text_3.capitalize()

upper_lower_example_11 = "Hello, How Are You Doing Today?"
upper_example_11 = upper_lower_example_11.upper()
lower_example_11 = upper_lower_example_11.lower()

upper_lower_example_12 = "This Is A Test String."
upper_example_12 = upper_lower_example_12.upper()
lower_example_12 = upper_lower_example_12.lower()

upper_lower_example13 = "ALL CAPS HERE."
upper_example13 = upper_lower_example13.upper()
lower_example13 = upper_lower_example13.lower()

# using only the functions you know, make these statements print out True
exercise1 = "Hello world!"
print(TODO == ['hello', 'world!'])
print(TODO == ['Hello', 'World!'])

exercise2 = ("hellO", "suN", "goodbyE", "mooN")
print(TODO == "Hello Sun Goodbye Moon")
print(TODO == "hello-sun-goodbye-moon")
print(TODO == "Hello, sun, Goodbye, moon")
"""
