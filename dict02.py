# I wanted to test if a key exists in a dictionary before updating the value for the key. 
# in is the intended way to test for the existence of a key in a dict.


def main():
	print("in main function")
	dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six"}

	k = 5
	if k in dict1:
		print('key: ', k, 'found in dict')
		
	k = 10
	if k in dict1:
		print('key: ', k, 'found in dict')

	pass

if __name__ == "__main__":
	main()