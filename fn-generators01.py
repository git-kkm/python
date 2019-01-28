# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.


# The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.

def countdown():
  i = 5
  while i > 0:
    yield i
    i -= 1

for i in countdown():
  print(i)


# Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
