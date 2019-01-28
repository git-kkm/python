# Reading Files

# readlines method returns a list in which each element is a line in the file.

# file = open("myfile.txt", "r")
# print(file.readlines())
# file.close()


# You can also use a for loop to iterate through the lines in the file:
file = open("myfile.txt", "r")
for line in file:
    print(line)
file.close()
