# Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
# This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.

# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test.
# - more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
# - easier to run in parallel.



# Lambdas

# Creating a function normally (using def) assigns it to a variable automatically.
# This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable.
# The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as anonymous.
# This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.

# Lambda functions aren't as powerful as named functions.
# They can only do things that require a single expression - usually equivalent to a single line of code.

# create a lambda function that returns the square of its argument, and call it for the number 8.

# a = (lambda x: x*x) (8)


# Lambda functions can be assigned to variables, and used like normal functions.
# Example:
# double = lambda x: x * 2
# print(double(7))
