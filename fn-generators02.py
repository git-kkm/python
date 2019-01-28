# Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.

# In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.


# Finite generators can be converted into lists by passing them as arguments to the list function.

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))
