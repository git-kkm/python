# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
# Assertions are carried out through use of the assert statement.


# What is the highest number printed by this code?
# print(0)
# assert "h" != "w"
# print (1)
# assert False
# print(2)
# assert True
# print(3)


# The assert can take a second argument that is passed to the AssertionError raised if the assertion fails.

temp = -10
assert (temp >= 0), "Colder than absolute zero!"
