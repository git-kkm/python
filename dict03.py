# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six"}

print('1. dict1: ', dict1)

if 5 in dict1:
	print('5 in dict')
else:
	print('5 not in dict')

if 10 not in dict1:
	print('10 not in dict')
else:
	print('10 in dict')


dict1[4] = "FOUR"				# Updates if 4 exists, else adds 4
print('2. dict1: ', dict1)

dict1[8] = "EIGHT"        		# Updates if 8 exists, else adds 8
print('3. dict1: ', dict1)

value = dict1.pop(1)  			# Removes the key & returns the value
print('value: ', value)
print('4. dict1: ', dict1)

dict1.clear()  					# Clears entire dictionary
print('5. dict1: ', dict1)

