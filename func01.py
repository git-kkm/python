def myfunc(a1, b1, c1):
	a1 = 60
	b1 = "This is new (inside function) string"
	c1 = [10,20,30,40]
	
	print("----------------------")
	print("inside func a1 : ", a1)
	print("inside func b1 : ", b1)
	print("inside func c1 : ", c1)
	print("----------------------")

def myfunc2(a1, b1, c1):
	a1 += 50
	b1 += " adding more"
	c1.append(1000);        # this is important	

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

	myfunc(a, b, c)

	print("in main (after) a : ", a)
	print("in main (after) b : ", b)
	print("in main (after) c : ", c)

	myfunc2(a, b, c)

	print("in main (final) a : ", a)
	print("in main (final) b : ", b)
	print("in main (final) c : ", c)

if __name__ == '__main__':
	main()