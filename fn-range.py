# coding: utf-8 

# range is a builtin function to create lists containing arithmetic progressions. 
# It is most often used in for loops. 
# The arguments must be plain integers. 
# If the step argument is omitted, it defaults to 1.
# If the start argument is omitted, it defaults to 0. 

# range(stop)
# range(start, stop[, step])

print( "range(10)         : ", range(10))
print( "range(1, 11)      : ", range(1, 11))
print( "range(0, 30, 5)   : ", range(0, 30, 5))
print( "range(0, 10, 3)   : ", range(0, 10, 3))
print( "range(0, -10, -1) : ", range(0, -10, -1))
print( "range(0)          : ", range(0))
print( "range(1, 0)       : ", range(1, 0))