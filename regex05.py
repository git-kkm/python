# Character Classes

# Character classes provide a way to match only one of a specific set of characters.
# A character class is created by putting the characters it matches inside square brackets.

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "axyz"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")

# What would '([^aeiou][aeiou][^aeiou])+' match?
# Answer: One or more repetitions of a non-vowel, a vowel and a non-vowel

# What would [abc][def] match?
# Answer: First letter out of "abc", second letter out of "def"

pattern = r"[abc][def]"

if re.search(pattern, "afXXXX"):
   print("Match 21")
