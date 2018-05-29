def func():
	list1 = list()     # create empty list. This is the right way.
	list2 = []         # create empty list. Do not use this notation.
	list3 = [10, 20, 30, 40, 50]

	tuple1 = tuple()   # create empty tuple. This is the right way.
	tuple2 = ()        # create empty tuple. Do not use this notation.
	tuple3 = (10, 20, 30, 40, 50)

	dict1 = dict()     # create empty dict. This is the right way.
	dict2 = {}         # create empty dict. Do not use this notation.
	dict3 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}

	print('the list1 contains: ', list1)
	print('the list2 contains: ', list2)
	print('the list3 contains: ', list3)

	print('the tuple1 contains: ', tuple1)
	print('the tuple2 contains: ', tuple2)
	print('the tuple3 contains: ', tuple3)

	print('the dict1 contains: ', dict1)
	print('the dict2 contains: ', dict2)
	print('the dict3 contains: ', dict3)

def main():
	print('in main')
	func()
	# pass

if __name__ == '__main__':
	main()