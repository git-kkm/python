def myfunc(list_args):
	list_args.append(100)
	list_args.append(200)
	print("element contents inside function is:")
	for element in list_args:
		print(element);

def main():
	myList=[10,20,30,40]
	
	print("element contents in main is:")
	for element in myList:
		print(element);

	myfunc(myList)

	print("element contents in main is:")
	for element in myList:
		print(element);

if __name__ == '__main__':
	main()