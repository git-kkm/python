# coding: utf-8

def main():
	print("in main function")
	dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six"}

	print("Printing dict1 fashion 1")
	for k in dict1:
		print(k,':', dict1[k])
		
	print("Printing dict1 fashion 2")
	for k,v in dict1.items():
		print(k,':', v)

	pass

if __name__ == "__main__":
	main()
