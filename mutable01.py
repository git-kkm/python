# Python strings are immutable.

# First a pointed to the string "Dog". 
# Then you changed the variable a to point at a new string "Dog eats treats". 
# You didn't actually mutate the string "Dog". 
# Strings are immutable, variables can point at whatever they want.


def funcAssign(a1, b1, c1):
	a1 = 200
	b1 = "new string funcAssign"
	c1 = [10,20,30,40]
	
	print("----------------------")
	print("inside func a1 : ", a1)
	print("inside func b1 : ", b1)
	print("inside func c1 : ", c1)
	print("----------------------")

def funcAdd(a1, b1, c1):
	a1 += 50
	b1 += " add funcAdd"
	c1.append(1000);        # KK: THIS IS IMPORTANT

	print("----------------------")
	print("inside func2 a1 : ", a1)
	print("inside func2 b1 : ", b1)
	print("inside func2 c1 : ", c1)
	print("----------------------")

def main():
	a = 100;
	b = "This is the original string"
	c = [1,2,3,4,5,6,7,8,9,10]

	print("in main (before) a : ", a)
	print("in main (before) b : ", b)
	print("in main (before) c : ", c)

	funcAssign(a, b, c)

	print("in main (after) a : ", a)
	print("in main (after) b : ", b)
	print("in main (after) c : ", c)

	funcAdd(a, b, c)

	print("in main (final) a : ", a)
	print("in main (final) b : ", b)
	print("in main (final) c : ", c)

if __name__ == '__main__':
	main()