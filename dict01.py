
dict1 = {1:"one", 2:"two", 3:"three", 4:"four"}

print("Printing dict1 version 1")
for k in dict1:
	print(k,':', dict1[k])

print("Printing dict1 version 2")
for k,v in dict1.items():
	print(k,':', v)

