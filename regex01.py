# re.match(pattern, string, flags=0)
# If the BEGINNING of string match the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern

# Regular Expressions
# Regular expressions are a powerful tool for string manipulation.
# They are useful for two main tasks:
# - verifying that strings match a pattern (ex. valid email address)
# - string substitutions (changing American spellings to British ones)

# Regular expressions can be accessed using the re module, which is part of the standard library.

# We would use raw strings as r"expression".
# Raw strings don't escape anything.

# Other functions to match patterns are re.search and re.findall.
# The function re.search finds a match of a pattern anywhere in the string.
# The function re.findall returns a list of all substrings that match a pattern.
# The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.


import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

print(re.findall(pattern, "eggspamsausagespam"))



