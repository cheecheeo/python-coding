"""
Week 9 exercises
Back to basics!
edit and change the files however you wish!
"""

import math

# note: when expressions are "naked" in a python script they aren't displayed,
# they must be "print"ed
6 + 4 * 9
print(6 + 4 * 9)
print("HERE")

42
print(42/10)
print(None)

print(42 == 42)
print(42 != 41)
print(41 < 42)
print(43 > 42)
print(42 <= 42)
print(42 >= 42)

x = 1337
# Exercise. Change the value of `x` to "exercise" all the different branches
# of the two if-statements below.
if x > 122:
    print("x is greater")
else:
    print("x is less")

if x < 1000:
    print("x isn't that great")
else:
    print("x is really great")

y = 42.0
# Exercise. Change the value of `y` to "exercise" all the different branches
# of the two if-statements below.
if y < -3.0:
    print("y is small")
else:
    print("y is bigger than 0 probably")

if y > -1000:
    print("x isn't that small")
else:
    print("y is really small")

z = -42.0
if z > math.pi - 0.5 and z < math.pi + 0.5:
    print("z is close to pi")
else:
    print("i don't know much about z")

if z > math.exp(10) - 1000 and z < math.exp(10) + 1000:
    print("z is around e**10")
else:
    print("z is not around e**10")

a = 10
if a < 0:
    print("a is negative")
elif a == 0:
    print("a is zero")
else:
    print("a is positive")

b = -15
if b < -10:
    print("b is less than -10")
elif b >= -10 and b <= 10:
    print("b is between -10 and 10")
else:
    print("b is greater than 10")

c = 0.0
if c < 0.0:
    print("c is a negative float")
elif c == 0.0:
    print("c is zero")
else:
    print("c is a positive float")

d = 10.5
if d < 0:
    print("d is negative")
elif d == 0:
    print("d is zero")
else:
    print("d is positive")

e = 10.5
if e < -10:
    print("e is less than -10")
elif e >= -10 and e < 0:
    print("e is between -10 and 0")
elif e == 0:
    print("e is zero")
elif e > 0 and e <= 10:
    print("e is between 0 and 10")
else:
    print("e is greater than 10")

f = -15
if f < -20:
    print("f is less than -20")
elif f >= -20 and f < -10:
    print("f is between -20 and -10")
elif f >= -10 and f <= 0:
    print("f is between -10 and 0")
elif f > 0 and f <= 10:
    print("f is getween 0 and 10")
else:
    print("f is greater than 10")

s = "hello"
print(type(c))
print(type(f))
print(type(s))

print("length: " + str(len(s)))
t = "world"
print(s + " " + t)

if len(s) < 5:
    print("s is a short word")
elif len(s) == 5:
    print("s is a medium-length word")
else:
    print("s is a long word")

v = "Hello, World!"
if len(v) < 5:
    print("v is a very short string")
elif len(v) >= 5 and len(v) < 10:
    print("v is a short string")
elif len(v) >= 10 and len(v) < 15:
    print("v is a medium-length string")
elif len(v) >= 15 and len(v) < 20:
    print("v is a long string")
else:
    print("v is a very long string")

u = "Python"
if u[0] == 'P':
    print("u starts with 'P'")
elif u[0] == 'p':
    print("u starts with 'p'")
elif u[-1] == 'n':
    print("u ends with 'n'")
elif u[-1] == 'N':
    print("u ends with 'N'")
else:
    print("u does not start with 'P' or 'p' and does not end with 'n' or 'N'")
