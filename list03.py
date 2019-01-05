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

	print('list1  : ', list1)
	print('list2  : ', list2)
	print('list3  : ', list3)

	print('tuple1 : ', tuple1)
	print('tuple2 : ', tuple2)
	print('tuple3 : ', tuple3)

	print('dict1  : ', dict1)
	print('dict2  : ', dict2)
	print('dict3  : ', dict3)

def main():
	print('in main')
	func()
	# pass

if __name__ == '__main__':
	main()