# Trying to index a key that isn't part of the dictionary returns a KeyError.

# dict1 = {1:"one", 2:"two", 3:"three", 4:"four"}
# print(dict1[1])
# print(dict1[3])
# print(dict1[5])


# Only immutable objects can be used as keys to dictionaries.
# Immutable objects are those that can't be changed.
# So far, the only mutable objects you've come across are lists and dictionaries.
# Trying to use a mutable object as a dictionary key causes a TypeError.

bad_dict = {
  [1, 2, 3]: "one two three",
}
