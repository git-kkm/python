# Define a function which can generate a list where the values are square of numbers 
# between 1 and 20 (both included). 
# Then the function needs to print the first 5 elements in the list.
# Then the function needs to print the last 5 elements in the list.
# Then the function needs to print all values except the first 5 elements in the list.

# Hint
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

def printList():
	
	li = list()   # create empty list

	for i in range(1,21):
		li.append(i**2)
	
	print( "Elements are: ", li)

	print( "------------------------------")
	print( "All elements are: ", li[:])
	print( "The first five elements are: ", li[:5])
	print( "The last five elements are: ", li[-5:])
	print( "------------------------------")

	print( "All elements are: ", li[0:-1])
	print( "The first five elements are: ", li[0:5])
	print( "The last five elements are: ", li[-5:0])


printList()
