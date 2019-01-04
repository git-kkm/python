# coding: utf-8 
# Define a function which can generate a list where the values are square of numbers 
# between 1 and 20 (both included). 
# Then the function needs to print the first 5 elements in the list.
# Then the function needs to print the last 5 elements in the list.
# Then the function needs to print all values except the first 5 elements in the list.


def printList():
	
	li = [0,1,2,3,4,5,6,7,8,9,10]
	
	print( "li: ", li)
	print( "li[:]: ", li[:])

	print( "li[3]    : ", li[3])
	print( "li[0,3]  : ", li[0:3])

	# WHen you want to print till from/till beginnning/end use BLANK
	print( "li[:3]   : ", li[:3])
	print( "li[3:]   : ", li[3:])

	print( "li[-5:]  : ", li[-5:])
	print( "li[0:-1] : ", li[0:-1])
	print( "li[-5:0] : ", li[-5:0])

	# The index method returns the first index at which a value occurs.
	print( "li.index(4) : ", li.index(4))

	#The append method adds an element to the end of a list. This happens inplace.
	li.append(12)
	print( "li[:] : ", li[:])

	# The pop method removes an item at the index you provide. 
	# This method will also return the item you removed from the list. 
	# If you don’t provide an index, it will by default remove the item at the last index.
	print( "pop : ", li.pop())
	print( "li: ", li)

printList()
