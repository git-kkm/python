mylist = [1, 2, 3]
for i in mylist:
	print(i)

# These iterables are handy because you can read them as much as you wish, 
# but you store all the values in memory and it’s not always what you want 
# when you have a lot of values.

mylist = [x*x for x in range(3)]
for i in mylist:
	print(i)

# Generators
# Generators are iterators, but you can only iterate over them once. 
# It’s because they do not store all the values in memory, 
# they generate the values on the fly:

mygenerator = (x*x for x in range(3))
print("calling generator first time")
for i in mygenerator:
	print(i)

print("calling generator second time")
for j in mygenerator:
	print(j)

# It is just the same except you used () instead of []. 
# BUT, you can not perform for i in mygenerator a second time since generators 
# can only be used once: they calculate 0, then forget about it and 
# calculate 1, and end calculating 4, one by one.

# Yield
# Yield is a keyword that is used like return, except the function will return a generator.

def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
	print(i)

# Here it’s a useless example, but it’s handy when you know your function 
# will return a huge set of values that you will only need to read once.

# To master yield, you must understand that when you call the function, the 
# code you have written in the function body does not run. The function only 
# returns the generator object, this is a bit tricky 🙂

# Then, your code will be run each time the for uses the generator.

# Now the hard part:

# The first time the for calls the generator object created from your function, 
# it will run the code in your function from the beginning until it hits yield, 
# then it’ll return the first value of the loop. Then, each other call will run 
# the loop you have written in the function one more time, and return the next 
# value, until there is no value to return.

# The generator is considered empty once the function runs but does not hit 
# yield anymore. It can be because the loop had come to an end, or because 
# you do not satisfy a “if/else” anymore.