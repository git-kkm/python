# Define a function which can generate a list where the values are square of numbers 
# between 1 and 20 (both included). 
# Print the first 5 elements in the list.
# Print the last 5 elements in the list.

# Hint
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.

def printList():
	li = list()   # create empty list

	for i in range(1,11):
		li.append(i**2)
	
	print( "All elements are: ", li)

printList()

