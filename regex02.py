# re.search(pattern, string, flags=0)
# Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. Return None if no position in the string matches the pattern

#KK - difference between match and search is match looks at the string from beginning ans search does for the entire string

# returns an object with several methods that give details about it.
# These methods include
# group which returns the string matched,
# start and end which return the start and ending positions of the first match, and
# span which returns the start and end positions of the first match as a tuple.

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())
