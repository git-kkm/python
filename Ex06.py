def myfunc(list_args):
	list_args.append(50)
	list_args.append(100)
	print("element contents inside function is:")
	for element in list_args:
		print(element);

def main():
	myList=[5,10,15,20]
	
	print("element contents in main is:")
	for element in myList:
		print(element);

	myfunc(myList)

	print("element contents in main is:")
	for element in myList:
		print(element);

if __name__ == '__main__':
	main()