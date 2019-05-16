# In C language terms, List is a pass by reference.

def myfunc(list_args):
	list_args.append(50)
	list_args.append(100)
	print("In func   : " , list_args)

def main():
	myList=[5,10,15,20]
	
	print("In main 1 : ", myList)

	myfunc(myList)

	print("In main 2 : ", myList)

if __name__ == '__main__':
	main()