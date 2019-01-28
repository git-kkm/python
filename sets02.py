# Are Python sets mutable?
# Yes

# Lists, Dictionaries and Sets are mutable.

y = {1, 2, 3}
print (id(y))

y |= {4,5,6}
print (id(y))

print (y)


# Are integers mutable?
# No

z = 1
print (id(z))

z += 5
print (id(z))

print (z)


