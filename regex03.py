# Search & Replace

# re.sub(pattern, repl, string, max=0)

# This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless max provided. This method returns the modified string.

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
