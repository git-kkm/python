# Raising Exceptions
# You can raise exceptions by using the raise statement.

# print(1)
# raise ValueError
# print(2)


# name = "123"
# raise NameError("Invalid name!")


# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.

try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
