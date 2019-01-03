# When the Python interpreter reads a source file, it executes all of the code found in it.

# Before executing the code, it will define a few special variables. 
# For example, if the python interpreter is running that module (the source file) as 
# the main program, it sets the special __name__ variable to have a value "__main__". 
# If this file is being imported from another module, __name__ will be set to the 
# module's name.

# One reason for doing this is that sometimes you write a module (a .py file) 
# where it can be executed directly. Alternatively, it can also be imported 
# and used in another module. 
# By doing the main check, you can have that code 
# only execute when you want to run the module as a program and not have it 
# execute when someone just wants to import your module and call your functions 
# themselves.

def main():
	print ("My name is %s and weight is %d kg!" % ('Krishna', 50) )

	print("In main function:")
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	tuple1 = (2, 4, 6, 8, 10)
	dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six"}

	print('list1:' , list1)
	print('tuple1:', tuple1)
	print('dict1:' , dict1)


if __name__ == '__main__':
	main()