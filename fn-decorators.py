# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

print_text  = decor(print_text)
print_text ()


# The below code has the same effect as the above one
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

@decor
def print_text():
  print("Hello world!")

print_text ()

# A single function can have multiple decorators.
