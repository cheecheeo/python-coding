"""
Week 10 homework
edit and change the files however you wish!
"""

# Exercise. Change the value of `z` to "exercise" all the different branches
# of the if-elif-statements below.
z = "Microsoft"
if len(z) == 0:
    print("z is an empty string")
elif len(z) == 1:
    print("z is a single letter: " + z)
elif len(z) > 1 and len(z) < 5:
    print("z is a short word that starts with " + z[0] + " and ends with " + z[-1])
elif len(z) >= 5 and len(z) < 10:
    print("z is a medium-length word that starts with " + z[0] + " and ends with " + z[-1])
elif len(z) >= 10 and len(z) < 15:
    print("z is a long word that starts with " + z[0] + " and ends with " + z[-1])
else:
    print("z is a very long word that starts with " + z[0] + " and ends with " + z[-1])

# Exercise. Change the value of `a` to "exercise" all the different branches
# of the if-elif-statements below.
a = 42
if type(a) == int:
    print("a is an integer")
elif type(a) == float:
    print("a is a floating-point number")
elif type(a) == str:
    print("a is a string")
elif type(a) == bool:
    print("a is a boolean")
else:
    print("a is of an unknown type")

# Exercise. Change the value of `h` to "exercise" all the different branches
# of the if-elif-statements below.
h = "Boromir is a human warrior"
if h[0] == 'B' and h[1] == 'o' and h[2] == 'r' and h[3] == 'o' and h[4] == 'm':
    print("h starts with 'Borom'")
elif h[0] == 'S' and h[1] == 'a' and h[2] == 'r' and h[3] == 'u' and h[4] == 'm':
    print("h starts with 'Sarum'")
elif h[0] == 'G' and h[1] == 'i' and h[2] == 'm' and h[3] == 'l' and h[4] == 'i':
    print("h starts with 'Gimli'")
elif h[0] == 'S' and h[1] == 'a' and h[2] == 'm' and h[3] == 'w' and h[4] == 'i':
    print("h starts with 'Samwi'")
elif h[0] == 'E' and h[1] == 'o' and h[2] == 'w' and h[3] == 'y' and h[4] == 'n':
    print("h starts with 'Eowyn'")
else:
    print("h does not start with any of the specified substrings")

# Exercise. Change the value of `i` to "exercise" all the different branches
# of the if-elif-statements below.
i = "The Shire is a peaceful place"
if i[-5] == 'e' and i[-4] == 'a' and i[-3] == 'c' and i[-2] == 'e' and i[-1] == 'f':
    print("i ends with 'eacef'")
elif i[-5] == 'l' and i[-4] == 'a' and i[-3] == 'c' and i[-2] == 'e' and i[-1] == 'e':
    print("i ends with 'lacee'")
elif i[-5] == 'r' and i[-4] == 'i' and i[-3] == 'n' and i[-2] == 'g' and i[-1] == 's':
    print("i ends with 'rings'")
elif i[-5] == 'o' and i[-4] == 'r' and i[-3] == 'c' and i[-2] == 's' and i[-1] == 'e':
    print("i ends with 'orcse'")
elif i[-5] == 'e' and i[-4] == 'n' and i[-3] == 't' and i[-2] == 's' and i[-1] == 'e':
    print("i ends with 'entse'")
else:
    print("i does not end with any of the specified substrings")

# Exercise. Change the value of `j` to "exercise" all the different branches
# of the if-elif-statements below.
j = "Merry is a brave hobbit"
if j[10] == 'a' and j[11] == ' ' and j[12] == 'b' and j[13] == 'r' and j[14] == 'a':
    print("j has 'a bra' in the middle")
elif j[10] == 'i' and j[11] == 's' and j[12] == ' ' and j[13] == 'a' and j[14] == ' ':
    print("j has 'is a ' in the middle")
elif j[10] == 'a' and j[11] == ' ' and j[12] == 's' and j[13] == 'c' and j[14] == 'a':
    print("j has 'a sca' in the middle")
elif j[10] == 'a' and j[11] == ' ' and j[12] == 'l' and j[13] == 'o' and j[14] == 'y':
    print("j has 'a loy' in the middle")
elif j[10] == 'a' and j[11] == ' ' and j[12] == 'f' and j[13] == 'r' and j[14] == 'i':
    print("j has 'a fri' in the middle")
else:
    print("j does not have any of the specified substrings in the middle")

# Let's define some strings
gandalf = "Gandalf the Grey"
frodo = "Frodo Baggins"
sauron = "Sauron the Deceiver"

# String indexing allows you to access individual characters in a string
# Python uses zero-based indexing, so the first character is at index 0
print(gandalf[0])  # Output: 'G'

# You can use negative indexing to access characters from the end of the string
print(frodo[-1])  # Output: 's'

# Some more examples:
print(frodo[1])  # Output: 'r'
print(sauron[2])  # Output: 'u'
print(gandalf[-1])  # Output: 'y'
print(frodo[-2])  # Output: 'n'

# String slicing allows you to access a range of characters in a string
# The syntax is string[start:stop], where 'start' is inclusive and 'stop' is exclusive
print(sauron[0:6])  # Output: 'Sauron'

# If you omit the 'start', it defaults to the beginning of the string
# If you omit the 'stop', it defaults to the end of the string
print(gandalf[:7])  # Output: 'Gandalf'
print(frodo[6:])  # Output: 'Baggins'

# Some more examples:
print(sauron[7:11])  # Output: 'the '
print(gandalf[8:12])  # Output: 'the '
print(frodo[0:5])  # Output: 'Frodo'
print(sauron[-9:-1])  # Output: ' Deceive'
print(gandalf[-4:])  # Output: 'Grey'
print(frodo[:])  # Output: 'Frodo Baggins' (whole string)
print(sauron[7:])  # Output: 'the Deceiver'

# Exercise. Change the value of `e` to "exercise" all the different branches
# of the if-elif-statements below.
e = "Gandalf the Grey is wise"
if e[:5] == "Ganda":
    print("e starts with 'Ganda'")
elif e[:5] == "Frodo":
    print("e starts with 'Frodo'")
elif e[:5] == "Sauron":
    print("e starts with 'Sauron'")
elif e[:5] == "Bilbo":
    print("e starts with 'Bilbo'")
elif e[:5] == "Arago":
    print("e starts with 'Arago'")
else:
    print("e does not start with any of the specified substrings")

# Exercise. Change the value of `f` to "exercise" all the different branches
# of the if-elif-statements below.
f = "The One Ring to rule them all"
if f[-5:] == "em all":
    print("f ends with 'em all'")
elif f[-5:] == "Shire":
    print("f ends with 'Shire'")
elif f[-5:] == "Mordor":
    print("f ends with 'Mordor'")
elif f[-5:] == "Gollum":
    print("f ends with 'Gollum'")
elif f[-5:] == "Hobbit":
    print("f ends with 'Hobbit'")
else:
    print("f does not end with any of the specified substrings")

# Exercise. Change the value of `g` to "exercise" all the different branches
# of the if-elif-statements below.
g = "Legolas is an elf prince"
if g[10:15] == "is an":
    print("g has 'is an' in the middle")
elif g[10:15] == "of th":
    print("g has 'of th' in the middle")
elif g[10:15] == "the k":
    print("g has 'the k' in the middle")
elif g[10:15] == "a hob":
    print("g has 'a hob' in the middle")
elif g[10:15] == "a wiz":
    print("g has 'a wiz' in the middle")
else:
    print("g does not have any of the specified substrings in the middle")

# Exercise. Change the value of `b` to "exercise" all the different branches
# of the if-elif-statements below.
b = "Artificial Intelligence is fun"
if b[:5] == "Artif":
    print("b starts with 'Artif'")
elif b[:5] == "Intel":
    print("b starts with 'Intel'")
elif b[:5] == "Micro":
    print("b starts with 'Micro'")
elif b[:5] == "Pytho":
    print("b starts with 'Pytho'")
elif b[:5] == "Hello":
    print("b starts with 'Hello'")
else:
    print("b does not start with any of the specified substrings")

# Exercise. Change the value of `c` to "exercise" all the different branches
# of the if-elif-statements below.
c = "I love programming in Python"
if c[-5:] == "ython":
    print("c ends with 'ython'")
elif c[-5:] == "Java":
    print("c ends with 'Java'")
elif c[-5:] == "C++":
    print("c ends with 'C++'")
elif c[-5:] == "Ruby":
    print("c ends with 'Ruby'")
elif c[-5:] == "Perl":
    print("c ends with 'Perl'")
else:
    print("c does not end with any of the specified substrings")

# Congratulaions!!! You made it.
# "Well, I'm back," - Bilbo Baggins
