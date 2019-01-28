# map

# The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).
# The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)




# filter

# The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
