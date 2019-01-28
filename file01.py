# You can specify the mode used to open a file by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.

# file = open("myfile.txt", "r")
# cont = file.read()
# print(type(cont))
# print(cont)
# file.close()



# To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.

file = open("myfile.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

#
