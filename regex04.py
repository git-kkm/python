# Metacharacters

# . (dot) -> This matches any character, other than a new line.
# ^       -> This matches the start of a string.
# $       -> This matches the end of a string.

# Some more metacharacters are *, +, ?, { and }.
# These specify numbers of repetitions.
# *       -> means "zero or more repetitions of the previous thing".
#            The "previous thing" can be a single character,
#            or a group of characters in parentheses.
# +        -> means "one or more repetitions"
# ?        -> means "zero or one repetitions".

# To summarize:
# * matches 0 or more occurrences of the preceding expression.
# + matches 1 or more occurrence of the preceding expression.

# |        -> means "or", so red|blue matches either "red" or "blue".

# Curly Braces
# Curly braces can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something".
# Hence {0,1} is the same thing as ?.
# If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.


import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "graybutton"):
   print("Match 3")



pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 10")

if re.match(pattern, "gray"):
   print("Match 11")

if re.match(pattern, "graybutton"):
   print("Match 12")

# The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline, and end with y.





pattern = r"egg(spam)*"

# matches strings that start with "egg" and follow with zero or more "spam"s.

if re.match(pattern, "egg"):
   print("Match 21")

if re.match(pattern, "egggg"):
   print("Match 22")

if re.match(pattern, "eggspamspamegg"):
   print("Match 23")

if re.match(pattern, "xxxxeggspamspamegg"):
   print("Match 24")

if re.match(pattern, "spam"):
   print("Match 25")



pattern2 = r"egg"

if re.match(pattern2, "egg"):
   print("Match 31")

if re.match(pattern2, "eggXXX"):
   print("Match 32")


pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 41")

if re.match(pattern, "gggggggggggggg"):
   print("Match 42")

if re.match(pattern, "agggggggg"):
   print("Match 43")



pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 51")

if re.match(pattern, "icecream"):
   print("Match 52")

if re.match(pattern, "ice--cream"):
   print("Match 53")




pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 61")

match = re.match(pattern, "grey")
if match:
   print ("Match 62")

match = re.match(pattern, "griy")
if match:
    print ("Match 63")




pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 71")

if re.match(pattern, "999"):
   print("Match 72")

if re.match(pattern, "9999"):
   print("Match 73")


# What would '([^aeiou][aeiou][^aeiou])+' match?
# Answer: One or more repetitions of a non-vowel, a vowel and a non-vowel
